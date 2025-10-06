#!/usr/bin/env python3
# Download a single YouTube song as MP3 (interactive version)

import os
import subprocess
import sys

# Folder where songs will be saved
DOWNLOAD_DIR = './Songs/'
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# Ask the user for the YouTube link
youtube_url = input("Enter the YouTube link of the song you want to download: ").strip()
if not youtube_url:
    print("❌ No link provided. Exiting...")
    exit(1)

print(f"🎵 Downloading: {youtube_url}")

# Use the same Python interpreter running this script
cmd = [
    sys.executable, "-m", "yt_dlp",
    "-x",
    "--audio-format", "mp3",
    "-o", os.path.join(DOWNLOAD_DIR, "%(title)s.%(ext)s"),
    youtube_url
]

try:
    subprocess.run(cmd, check=True)
    print("✅ Download completed!")
except subprocess.CalledProcessError:
    print("❌ Download failed. Check the URL and try again.")
