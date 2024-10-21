#!/usr/bin/python3
import sys
import os
import re
import hashlib

def print_usage_and_exit():
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)

def print_missing_file_and_exit(filename):
    print(f"Missing {filename}", file=sys.stderr)
    sys.exit(1)

def parse_headings(line):
    heading_level = 0
    while heading_level < len(line) and line[heading_level] == '#':
        heading_level += 1

    if 1 <= heading_level <= 6:
        return f"<h{heading_level}>{line[heading_level:].strip()}</h{heading_level}>\n"
    return None

def parse_list(lines, ordered=False):
    list_tag = "ol" if ordered else "ul"
    html = f"<{list_tag}>\n"
    for line in lines:
        html += f"<li>{line.strip()[2:]}</li>\n"
    html += f"</{list_tag}>\n"
    return html

def parse_lists(line):
    if line.startswith('- '):
        return 'unordered', line.strip()[2:]
    elif line.startswith('* '):
        return 'ordered', line.strip()[2:]
    return None, None

def parse_bold_and_emphasis(text):
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'__(.*?)__', r'<em>\1</em>', text)
    return text

def convert_md5(text):
    return hashlib.md5(text.encode()).hexdigest()

def remove_c(text):
    return re.sub(r'[cC]', '', text)

def parse_special_syntax(text):
    text = re.sub(r'\[\[(.*?)\]\]', lambda x: convert_md5(x.group(1)), text)
    text = re.sub(r'\(\((.*?)\)\)', lambda x: remove_c(x.group(1)), text)
    return text

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print_usage_and_exit()

    markdown_file = sys.argv[1]
    html_file = sys.argv[2]

    if not os.path.exists(markdown_file):
        print_missing_file_and_exit(markdown_file)

    with open(markdown_file, 'r') as md_file:
        markdown_content = md_file.readlines()

    in_list = False
    list_type = None
    list_lines = []

    with open(html_file, 'w') as html_output:
        for line in markdown_content:
            line = parse_bold_and_emphasis(parse_special_syntax(line.strip()))
            heading_html = parse_headings(line)
            list_type_current, list_item = parse_lists(line)

            if heading_html:
                if in_list:
                    html_output.write(parse_list(list_lines, ordered=(list_type == 'ordered')))
                    in_list = False
                    list_lines = []
                html_output.write(heading_html)

            elif list_type_current:
                if not in_list:
                    in_list = True
                    list_type = list_type_current
                list_lines.append(list_item)

            else:
                if in_list:
                    html_output.write(parse_list(list_lines, ordered=(list_type == 'ordered')))
                    in_list = False
                    list_lines = []
                html_output.write(f"<p>{line}</p>\n")
