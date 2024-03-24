#!/usr/bin/python3

import sys
import re
import hashlib

def convert_md5(match):
    content = match.group(1)
    return hashlib.md5(content.encode('utf-8')).hexdigest()

def remove_letter_c(match):
    content = match.group(1)
    return content.replace('c', '').replace('C', '')

def convert_bold(match):
    content = match.group(1)
    return f'<b>{content}</b>'

def convert_italic(match):
    content = match.group(1)
    return f'<em>{content}</em>'

def markdown_to_html(markdown_content):
    # Handle [[...]] syntax
    md5_pattern = re.compile(r'\[\[(.*?)\]\]')
    markdown_content = md5_pattern.sub(convert_md5, markdown_content)

    # Handle ((...)) syntax
    remove_c_pattern = re.compile(r'\(\((.*?)\)\)')
    markdown_content = remove_c_pattern.sub(remove_letter_c, markdown_content)

    # Handle **...** syntax for bold
    bold_pattern = re.compile(r'\*\*(.*?)\*\*')
    markdown_content = bold_pattern.sub(convert_bold, markdown_content)

    # Handle __...__ syntax for italic
    italic_pattern = re.compile(r'__(.*?)__')
    markdown_content = italic_pattern.sub(convert_italic, markdown_content)

    return markdown_content

def main():
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py input_file output_file")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(input_file, 'r') as f:
        markdown_content = f.read()

    html_content = markdown_to_html(markdown_content)

    with open(output_file, 'w') as f:
        f.write(html_content)

if __name__ == "__main__":
    main()
