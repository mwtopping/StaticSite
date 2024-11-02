import unittest

from extract_markdown import extract_markdown_links, extract_markdown_images

class TestExtractMarkdown(unittest.TestCase):
    def test1(self):
        text = "this is text with a ![rick roll](https://i.imgur.com/akaoqih.gif) and ![obi wan](https://i.imgur.com/fjrm4vk.jpeg)"
        result = extract_markdown_images(text)
        expected = [("rick roll", "https://i.imgur.com/akaoqih.gif"), ("obi wan", "https://i.imgur.com/fjrm4vk.jpeg")]
        self.assertEqual(result, expected)
 

    def test2(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_links(text)
        expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(result, expected)
 

if __name__ == "__main__":
    unittest.main()
