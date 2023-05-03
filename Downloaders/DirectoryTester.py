import os

destination = "./DownloadedAudio"

print(destination)
if (os.path.isdir(destination)):
    print("Directory exists")
else:
    print("Invalid directory")