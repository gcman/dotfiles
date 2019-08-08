#!/usr/bin/env python3
import clipboard
import urllib3
from os import environ

def send_command_to_qute(command):
    with open(environ.get("QUTE_FIFO"), "w") as f:
        f.write(command)

        
url = environ.get("QUTE_URL")
if "github.com" in url:
    filename = url.replace("https://github.com/", "")
    url = url.replace("github", "raw.githubusercontent", 1).replace("/blob/", "/", 1)
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    data = response.data.decode('utf-8')
    clipboard.copy(data)
    send_command_to_qute("message-info 'copied to clipboard: {}'".format(filename))
else:
    send_command_to_qute("message-error 'Not in a github domain!")
