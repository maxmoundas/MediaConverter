# MediaConverter

This code repository contains two Python scripts that allow you to download YouTube and TikTok videos as MP3 files and upload them to a Google Drive folder. The scripts can be run from the terminal, and they use the pytube and tiktok-scraper libraries to download the videos, and the pydrive library to upload the MP3 files to Google Drive.

# Requirements
- Python 3
- pytube library (can be installed via pip: pip install pytube)
- tiktok-scraper library (can be installed via pip: pip install tiktok-scraper)
- pydrive library (can be installed via pip: pip install pydrive)
- A Google account with access to Google Drive and a Google Drive API key (instructions for setting up the API key can be found here: https://developers.google.com/drive/api/v3/quickstart/python)

# Configuration
Before using the scripts, you need to configure the Google Drive API key. Follow the instructions in the link above to set up the API key, and then save the credentials.json file to the same directory as the scripts. You also need to create (or specify) a folder in your Google Drive that you want the files uploaded to. Lastly, edit the config.py file and enter your Google Drive folder IDs.
