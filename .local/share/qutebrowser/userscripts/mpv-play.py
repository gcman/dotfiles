#!/usr/bin/env python3
import subprocess
from youtube_dl import YoutubeDL
from os import environ

def send_command_to_qute(command):
    with open(environ.get("QUTE_FIFO"), "w") as f:
        f.write(command)

def main():
    mode = environ.get("QUTE_MODE")
    url = environ.get("QUTE_URL")
    if mode == "hints":
        with YoutubeDL() as ydl:
            info_dict = ydl.extract_info(url, download=False)
            title = info_dict.get('title', None)
    else:
        title = environ.get("QUTE_TITLE")
    title = "".join("{:02x}".format(ord(c)) for c in title)
    command = "".format(url,title)
    send_command_to_qute("spawn emacsclient -e '(gm/play-with-mpv \"{}\" (hex-to-string \"{}\"))'".format(url,title))

if __name__ == "__main__":
    main()
