#!/usr/bin/env python3
import os
import html
import re
import sys
import xml.etree.ElementTree as ET
try:
    import pyperclip
except ImportError:
    PYPERCLIP = False
else:
    PYPERCLIP = True


def parse_text_content(element):
    root = ET.fromstring(element)
    text = ET.tostring(root, encoding="unicode", method="text")
    text = html.unescape(text)
    return text


def send_command_to_qute(command):
    with open(os.environ.get("QUTE_FIFO"), "w") as f:
        f.write(command)


def get_code_text(arg=None):
    delimiter = sys.argv[1] if len(sys.argv) > 1 else ";"
    # For info on qute environment vairables, see
    # https://github.com/qutebrowser/qutebrowser/blob/master/doc/userscripts.asciidoc
    element = os.environ.get("QUTE_SELECTED_HTML")
    code_text = parse_text_content(element)
    if PYPERCLIP:
        pyperclip.copy(code_text)
    else:
        # Qute's yank command  won't copy accross multiple lines so we
        # compromise by placing lines on a single line seperated by the
        # specified delimiter
        code_text = re.sub("(\n)+", delimiter, code_text)
        code_text = code_text.replace("'", "\"")
    return code_text
