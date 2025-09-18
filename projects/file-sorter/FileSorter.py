import os
import shutil

def organize_files(source_folder):
    # Get a list of all files in the source folder
    files = os.listdir(source_folder)

    for file in files:
        # Check if the item in the source folder is a file
        if os.path.isfile(os.path.join(source_folder, file)):
            # Extract the file extension
            file_extension = os.path.splitext(file)[1]
            # Create the destination folder path based on the file extension
            destination_folder = os.path.join(source_folder, file_extension[1:])
            
            # Check if the destination folder exists, if not, create it
            if not os.path.exists(destination_folder):
                os.mkdir(destination_folder)
            
            # Move the file to the destination folder
            shutil.move(os.path.join(source_folder, file), os.path.join(destination_folder, file))

# Specify the path to the source folder you want to organize
source_folder = "C:/Users/Carte/Desktop/Coding"

# Call the organize_files function with the specified source folder
organize_files(source_folder)
