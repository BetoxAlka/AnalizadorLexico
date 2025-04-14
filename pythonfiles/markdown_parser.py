import re

class MarkdownParser:
    def __init__(self):
        self.rules = [
            (r'###### (.*)', r'<h6>\1</h6>'),
            (r'##### (.*)', r'<h5>\1</h5>'),
            (r'#### (.*)', r'<h4>\1</h4>'),
            (r'### (.*)', r'<h3>\1</h3>'),
            (r'## (.*)', r'<h2>\1</h2>'),
            (r'# (.*)', r'<h1>\1</h1>'),
            (r'\*\*(.*?)\*\*', r'<strong>\1</strong>'),
            (r'\*(.*?)\*', r'<em>\1</em>'),
            (r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>'),
            (r'`([^`]+)`', r'<code>\1</code>'),
            (r'^> (.*)', r'<blockquote>\1</blockquote>'),
            (r'^[-+*] (.*)', r'<li>\1</li>'),
        ]

    def parse_line(self, line):
        original = line
        for pattern, repl in self.rules:
            line = re.sub(pattern, repl, line)
        return line

    def parse(self, text):
        lines = text.split('\n')
        html = []
        inside_list = False
        for line in lines:
            stripped = line.strip()
            if re.match(r'^[-+*] ', stripped):
                if not inside_list:
                    html.append('<ul>')
                    inside_list = True
                html.append(self.parse_line(stripped))
            else:
                if inside_list:
                    html.append('</ul>')
                    inside_list = False
                html.append(self.parse_line(stripped))
        if inside_list:
            html.append('</ul>')
        return '\n'.join(html)


def test_parser():
    markdown = """# Welcome to Markdown
This is **bold** and this is *italic*.

## Links and Code
Here's a [link](http://example.com) and some `inline code`.

### List Example
* Item 1
* Item 2
* Item 3

> This is a quote."""
    
    parser = MarkdownParser()
    html = parser.parse(markdown)
    print("Markdown input:")
    print(markdown)
    print("\nConverted HTML:")
    print(html)


if __name__ == "__main__":
    test_parser()
