import subprocess
import sys

from Helper_Functions import FileIO, MapillaryOperations

FileIO.directory_generator()

while True:
    subprocess.run(["clear"])
    print("    (0) Import Images")
    print("    (1) Delete Thumbnail Images")
    print("    (2) Process Images")
    print("    (3) Sort Images")
    print("    (4) Delete Duplicated Images")
    print("    (5) Delete Uploaded Images")
    print("    (6) Upload Images")
    print("    (7) Archive Image Coordinates")
    print("    (-1) Quit")
    userOperation = input("Please Input Your Desired Operation: ")
    if userOperation == "0":
        FileIO.move_directory(
            input("Please Input The Directory Of The Captured Images You Would Like To Import: "))
    elif userOperation == "1":
        FileIO.delete_thumbnails()
    elif userOperation == "2":
        MapillaryOperations.process_images()
    elif userOperation == "3":
        MapillaryOperations.post_process_images()
    elif userOperation == "4":
        FileIO.delete_directory('/Captured Images/duplicates/')
    elif userOperation == "5":
        if FileIO.get_uploaded_images_metadata():
            FileIO.delete_directory('/Captured Images/uploaded/')
        else:
            print("Unable to delete images as not all metadata was successfully added into the database")
    elif userOperation == "6":
        MapillaryOperations.upload_images()
    elif userOperation == "7":
        FileIO.get_uploaded_images_metadata()
    elif userOperation == "-1":
        sys.exit(0)
