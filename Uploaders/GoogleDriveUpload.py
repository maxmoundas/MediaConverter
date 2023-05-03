from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
# For using listdir()
import os


# find a folder in the Google Drive with the name passed to directory_path
# works for root folders or nested folders
# directory_path format: "parentFolder/NestedFolder/SecondNestedFolder"
def findFolder(directory_path):
    folder_names = directory_path.strip('/').split('/')
    folder_id = 'root'

    # Iterate through all folder names in the directory path
    for folder_name in folder_names:
        query = "mimeType='application/vnd.google-apps.folder' and trashed=false and title='{}' and '{}' in parents".format(folder_name, folder_id)
        folder_list = drive.ListFile({'q': query}).GetList()

        if folder_list:
            # Folder exists, update folder_id to the new folder's ID
            folder_id = folder_list[0]['id']
            print(f"Folder named '{folder_name}' found!")
        else:
            # Folder doesn't exist, create the folder and update folder_id to the new folder's ID
            folder = drive.CreateFile({'title': folder_name, 'parents': [{'id': folder_id}], 'mimeType': 'application/vnd.google-apps.folder'})
            folder.Upload()
            folder_id = folder['id']
            print(f"Folder named '{folder_name}' not found, created new folder.")

    # Return the final folder object
    final_folder = drive.CreateFile({'id': folder_id})
    return final_folder

# Below code does the authentication
# part of the code
gauth = GoogleAuth()
# Creates local webserver and auto
# handles authentication.
gauth.LocalWebserverAuth()       
drive = GoogleDrive(gauth)

# replace the value of this variable
# with the absolute path of the directory

# absolute path
path = r"/Users/maxmoundas/PersonalProjects/MediaConverter/DownloadedAudio"

# path in project
# path = "DownloadedAudio"


folder = findFolder("Testing/NestedTesting/SecondNestedTesting")
# folder = findFolder("Testing")

# iterating thought all the files/folder
# of the desired directory
for file in os.listdir(path):
    
    print(f"Uploading {file} to folder!")
    f = drive.CreateFile({'title': file, 'parents': [{'id': folder['id']}]})
    f.SetContentFile(os.path.join(path, file))
    f.Upload()
    print("File uploaded!")
    f = None
