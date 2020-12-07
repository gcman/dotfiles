#!/usr/bin/env python3
import sys
import urllib.request
import shutil

def main():
    with open(sys.argv[1], "r") as f:
        for line in f:
            arr = line.split(" ")
            filename = arr[0]
            url = arr[1]
            with urllib.request.urlopen(url) as response, open(filename, 'wb') as out_file:
                print("Downloading {}...".format(filename))
                shutil.copyfileobj(response, out_file)

if __name__ == "__main__":
    main()
