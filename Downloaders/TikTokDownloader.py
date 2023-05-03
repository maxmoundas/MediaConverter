import os
import requests
from tiktok_scraper import TikTokScraper

# url input from user
# video_url = input("Enter the URL of the TikTok video you want to download: ")
video_url = "https://www.tiktok.com/@sp3dupsongssx/video/7210514451399937326?_r=1&_t=8bZmZsL7rkQ"

# create instance of TikTokScraper and pass the video URL
scraper = TikTokScraper()
video_data = scraper.get_video_by_url(video_url)

# check for destination to save file
# print("Enter the destination (leave blank for current directory)")
# destination = str(input(">> ")) or '.'

# local download location
# destination = "./DownloadedAudio"
destination = r"/Users/maxmoundas/PersonalProjects/MediaConverter/DownloadedAudio"

if (os.path.isdir(destination)):
    print("Directory exists")
else:
    print("Invalid directory")

# get the filename
filename = video_data['id'] + '.mp3'

# download the file
audio_url = video_data['music']['playUrl']
response = requests.get(audio_url)
with open(os.path.join(destination, filename), 'wb') as f:
    f.write(response.content)

# result of success
print(filename + " has been successfully downloaded.")
