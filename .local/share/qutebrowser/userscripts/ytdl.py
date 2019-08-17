#!/usr/bin/env python3
from os import environ

def send_command_to_qute(command):
    with open(environ.get("QUTE_FIFO"), "w") as f:
        f.write(command)
        
def main():
    title = environ.get("QUTE_TITLE")
    url = environ.get("QUTE_URL")
    url = "".join("{:02x}".format(ord(c)) for c in url)
    send_command_to_qute("spawn emacsclient -e '(progn (youtube-dl (hex-to-string \"{}\")) (message \"{}\"))'".format(url,"Downloading \"{}\" from qutebrowser".format(title)))
    
if __name__ == "__main__":
    main()
