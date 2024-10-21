#!/usr/bin/python3
"""Markdown to HTML"""

import sys
import os.path
import re
import hashlib

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: ./markdown2html.py README.md README.html',
              file=sys.stderr)
        exit(1)

    if not os.path.isfile(sys.argv[1]):
        print('Missing {}'.format(sys.argv[1]), file=sys.stderr)
        exit(1)

    with open(sys.argv[1]) as read:
        with open(sys.argv[2], 'w') as html:
            unordered_start, ordered_start, paragraph = False, False, False
            
            for line in read:
                line = line.rstrip()  # Remove trailing whitespace/newline

                # Replace bold and emphasis syntax
                line = line.replace('**', '<b>', 1)
                line = line.replace('**', '</b>', 1)
                line = line.replace('__', '<em>', 1)
                line = line.replace('__', '</em>', 1)

                # Convert [[text]] to MD5
                md5 = re.findall(r'\[\[.+?\]\]', line)
                md5_inside = re.findall(r'\[\[(.+?)\]\]', line)
                if md5:
                    line = line.replace(md5[0], hashlib.md5(
                        md5_inside[0].encode()).hexdigest())

                # Remove letter 'C' (case-insensitive)
                remove_letter_c = re.findall(r'\(\(.+?\)\)', line)
                remove_c_more = re.findall(r'\(\((.+?)\)\)', line)
                if remove_letter_c:
                    remove_c_more = ''.join(
                        c for c in remove_c_more[0] if c.lower() != 'c')
                    line = line.replace(remove_letter_c[0], remove_c_more)

                # Check for headings
                headings = re.match(r'^(#{1,6}) (.+)', line)
                if headings:
                    heading_level = len(headings.group(1))
                    content = headings.group(2)
                    html.write('<h{}>{}</h{}>\n'.format(
                        heading_level, content, heading_level))
                    continue  # Skip to next line after processing heading

                # Check for unordered list (-)
                if line.startswith('- '):
                    if not unordered_start:
                        html.write('<ul>\n')
                        unordered_start = True
                    html.write('<li>{}</li>\n'.format(line[2:].strip()))
                    continue  # Skip to next line after processing unordered list item

                if unordered_start and not line.startswith('- '):
                    html.write('</ul>\n')
                    unordered_start = False

                # Check for ordered list (*)
                if line.startswith('* '):
                    if not ordered_start:
                        html.write('<ol>\n')
                        ordered_start = True
                    html.write('<li>{}</li>\n'.format(line[2:].strip()))
                    continue  # Skip to next line after processing ordered list item

                if ordered_start and not line.startswith('* '):
                    html.write('</ol>\n')
                    ordered_start = False

                # Handle paragraphs (if it's not a heading or list)
                if len(line.strip()) > 0:  # Non-empty line
                    if not paragraph:
                        html.write('<p>\n')
                        paragraph = True
                    html.write('{}\n'.format(line.strip()))
                else:
                    if paragraph:  # Close paragraph on empty line
                        html.write('</p>\n')
                        paragraph = False

            # Close any open tags at the end of the file
            if unordered_start:
                html.write('</ul>\n')
            if ordered_start:
                html.write('</ol>\n')
            if paragraph:
                html.write('</p>\n')
    exit(0)
