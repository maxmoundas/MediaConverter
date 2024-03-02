from pytube import YouTube
import os

# yt = YouTube(str(input("Enter the URL of the YouTube video you want to download: ")))
yt = YouTube("https://www.youtube.com/watch?v=zJfiBBomv8A")

# extract only audio
video = yt.streams.filter(only_audio=True).first()

# local download location
destination = "./DownloadedAudio" # relative path
# destination = r"/Users/username/folder/folder/folder" # absolute path

# Check if the directory exists, if not, create it
if not os.path.exists(destination):
    os.makedirs(destination)
    print(f"Directory {destination} created to save the file.")

# download the file
out_file = video.download(output_path=destination)

# save the file
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

# result of success
print(yt.title + " has been successfully downloaded.")
