#!/usr/bin/env python3
# Download all songs from a YouTube playlist directly as MP3 (audio only)

import os
import subprocess
import sys

# Folder where songs will be saved
DOWNLOAD_DIR = './Songs/'
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# Ask the user for the playlist link
playlist_url = input("Enter the YouTube playlist link you want to download: ").strip()
if not playlist_url:
    print("❌ No link provided. Exiting...")
    exit(1)

print(f"🎵 Downloading all songs from playlist: {playlist_url}")

# yt-dlp command to download audio only and convert to MP3
cmd = [
    sys.executable, "-m", "yt_dlp",
    "-f", "bestaudio/best",                   # best available audio format (no video)
    "-x",                                     # extract audio only
    "--audio-format", "mp3",                  # convert to MP3
    "--embed-thumbnail",                      # embed thumbnail (optional)
    "--add-metadata",                         # add metadata (title, artist, etc.)
    "-o", os.path.join(DOWNLOAD_DIR, "%(playlist_index)s - %(title)s.%(ext)s"),
    playlist_url
]

try:
    subprocess.run(cmd, check=True)
    print("✅ All songs from playlist downloaded successfully as MP3!")
except subprocess.CalledProcessError:
    print("❌ Download failed. Check the playlist link and try again.")
