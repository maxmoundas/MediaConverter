from pytube import YouTube
import os

# url input from user
yt = YouTube(str(input("Enter the URL of the YouTube video you want to download: ")))
# yt = YouTube("https://www.youtube.com/watch?v=gB6uYQ4KPPs")

# extract only audio
video = yt.streams.filter(only_audio=True).first()

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

# download the file
out_file = video.download(output_path=destination)

# save the file
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

# result of success
print(yt.title + " has been successfully downloaded.")

