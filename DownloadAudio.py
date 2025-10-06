# #! /usr/bin/python
# #Made to ease the download process. No copyright infringement intended.
# import re
# import os

# __DIR__ = './songs/' # Enter the directory in which you want to download the songs, make sure to give '/' at the end
# if not os.path.exists(__DIR__):
#     os.makedirs(__DIR__)

# p= re.compile('https:*')
# FilePointer = open("README.md")
# lines=[]
# for i in FilePointer.readlines():
#     lines.append(i[:-1]) # -1 to remove the '\n' that comes along

# for i in lines:
#     m = p.search(i)
#     if(m is not None):
#         url = i[m.start():-1] # -1 to remove the ')' present in end of line 
#         args = '-o "' + __DIR__ + '%(title)s.%(ext)s" --extract-audio --audio-format mp3 --prefer-ffmpeg -w ' + url
#         os.system("youtube-dl "+args)


#!/usr/bin/env python3
# Made to ease the download process. No copyright infringement intended.

import re
import os
import subprocess

# Folder where songs will be saved
DOWNLOAD_DIR = './Songs/'

# Create the folder if it doesn't exist
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# Compile a regex pattern to find YouTube URLs
url_pattern = re.compile(r'(https?://[^\s)]+)')

# Read all lines from README.md
with open("README.md", "r", encoding="utf-8") as file:
    lines = [line.strip() for line in file.readlines()]

# Loop through each line and extract URLs
for line in lines:
    match = url_pattern.search(line)
    if match:
        url = match.group(1)
        print(f"\n🎵 Downloading: {url}")

        # Command for yt-dlp
        cmd = [
            "yt-dlp",
            "-o", os.path.join(DOWNLOAD_DIR, "%(title)s.%(ext)s"),
            "--extract-audio",
            "--audio-format", "mp3",
            "--prefer-ffmpeg",
            url
        ]

        try:
            subprocess.run(cmd, check=True)
            print("✅ Download completed.")
        except subprocess.CalledProcessError:
            print("❌ Download failed for:", url)
