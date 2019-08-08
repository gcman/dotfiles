#!/usr/bin/env python3
import subprocess
from pathlib import Path

home = str(Path.home())
exec(open(home + "/.local/share/qutebrowser/userscripts/code-select-helper.py").read())

def main():
    code_text = get_code_text()
    code_text = "".join("{:02x}".format(ord(c)) for c in code_text)
    send_command_to_qute("spawn emacsclient org-protocol://capture?template=c&url='{{url}}'&title='{{title}}'&body='{}'".format(code_text))
    
if __name__ == "__main__":
    main()
