#!/usr/bin/env python3
from os import environ

def send_command_to_qute(command):
    with open(environ.get("QUTE_FIFO"), "w") as f:
        f.write(command)
        
def main():
    title = ""
    if environ.get("QUTE_MODE") != "hints":
        title = environ.get("QUTE_TITLE")
        title = "".join("{:02x}".format(ord(c)) for c in title)
    url = environ.get("QUTE_URL")
    url = "".join("{:02x}".format(ord(c)) for c in url)
    send_command_to_qute("spawn emacsclient -e '(progn (youtube-dl (hex-to-string \"{}\")) (message (format \"Downloading from qutebrowser: %s\" (hex-to-string \"{}\"))))'".format(url,title))
    
if __name__ == "__main__":
    main()
