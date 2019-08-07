#!/usr/bin/env python3
from pathlib import Path

home = str(Path.home())
exec(open(home + "/.local/share/qutebrowser/userscripts/code-select-helper.py").read())

code_text = get_code_text()

def main():
    if PYPERCLIP:
        send_command_to_qute(
            "message-info 'copied to clipboard: {info}{suffix}'".format(
                info=code_text.splitlines()[0],
                suffix="..." if len(code_text.splitlines()) > 1 else ""
            )
        )
    else:
        send_command_to_qute("yank inline '{code}'\n".format(code=code_text))


if __name__ == "__main__":
    main()
