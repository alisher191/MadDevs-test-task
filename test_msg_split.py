import unittest

from msg_split import split_message, CustomHTMLParser

MAX_LEN = 14


class SplitMessageTest(unittest.TestCase):
    def setUp(self):
        self.parser = CustomHTMLParser(MAX_LEN)

    def test_split_message(self):
        html = "<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>"
        expected_fragments = [
            "<p>Lorem ipsum</p>",
            "<p>dolor sit</p>",
            "<p>amet,</p>",
            "<p>consectetur</p>",
            "<p>adipiscing</p>",
            "<p>elit.</p>"
        ]
        fragments_generator = split_message(html)
        fragments = list(fragments_generator)
        self.assertEqual(fragments, expected_fragments)
        

if __name__ == '__main__':
    unittest.main()