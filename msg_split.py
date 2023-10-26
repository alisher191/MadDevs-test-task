from html.parser import HTMLParser

MAX_LEN = 14


class CustomHTMLParser(HTMLParser):
    def __init__(self, max_len):
        super().__init__()
        self.max_len = max_len
        self.fragments = []
        self.current_fragment = ""
        self.open_tags = []

    def handle_starttag(self, tag, attrs):
        self.open_tags.append(tag)

    def handle_endtag(self, tag):
        if self.open_tags and tag == self.open_tags[-1]:
            self.open_tags.pop()
            if self.current_fragment:
                self.fragments.append(self.current_fragment)
                self.current_fragment = ""

    def handle_data(self, data):
        if self.open_tags:
            words = data.split()
            for word in words:
                if len(self.current_fragment) + len(word) <= self.max_len:
                    self.current_fragment += word + " "
                else:
                    if self.current_fragment:
                        self.fragments.append(self.current_fragment)
                        self.current_fragment = ""
                    while len(word) > self.max_len:
                        self.fragments.append(word[:self.max_len])
                        word = word[self.max_len:]
                    if word:
                        self.current_fragment += word + " "

    def close_tags(self):
        while self.open_tags:
            tag = self.open_tags.pop()
            self.current_fragment += f"</{tag}>"

        if self.current_fragment:
            self.fragments.append(self.current_fragment)
            self.current_fragment = ""


def split_message(html, max_len=MAX_LEN):
    parser = CustomHTMLParser(max_len)
    parser.feed(html)
    parser.close_tags()

    fragments = parser.fragments

    for fragment in fragments:
        formatted_fragment = f"<p>{fragment.strip()}</p>"
        yield formatted_fragment

html = "<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>"
fragments = split_message(html)
for fragment in fragments:
    print(fragment)
