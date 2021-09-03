#!/usr/bin/env python3
import subprocess
import sys
import time
from os import environ
import urllib.request
import shutil

def send_command_to_qute(command):
    with open(environ.get("QUTE_FIFO"), "w") as f:
        f.write(command)

def main():
    mode = environ.get("QUTE_MODE")
    id_arr = []
    if len(sys.argv) == 1:
        html = environ.get("QUTE_HTML")
        with open(html, "r") as f:
            for line in f:
                if "https://stanford-pilot.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=" in line:
                    id_arr.append(line.split("?id=",1)[1].split("\"",1)[0])
        for i,url in enumerate(id_arr):
            send_command_to_qute("open -t https://stanford-pilot.hosted.panopto.com/Panopto/Podcast/Social/{}.mp4".format(url))
            time.sleep(3)
            send_command_to_qute("spawn --userscript panopto-dl.py lecture{}".format(i+1))
            time.sleep(0.25)
            send_command_to_qute("tab-close")
            time.sleep(0.25)
    else:
        title = sys.argv[1]
        url = environ.get("QUTE_URL").split("?invocation",1)[0]
        filename = "/home/gautam/Downloads/{}.mp4".format(title)
        with open("/home/gautam/Downloads/dl-list.txt", "a") as f:
            f.write("{}.mp4 {}\n".format(title, url))

if __name__ == "__main__":
    main()
