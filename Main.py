import subprocess
import sys

from Helper_Functions import FileIO, MapillaryOperations

FileIO.directory_generator()

while True:
    subprocess.run(["clear"])
    print("Mapillary Helper Main Menu")
    print("    (0) Import Images")
    print("    (1) Delete Thumbnail Images")
    print("    (2) Process Images")
    print("    (3) Sort Images")
    print("    (4) Delete Duplicated Images")
    print("    (5) Delete Uploaded Images")
    print("    (6) Upload Images")
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
        FileIO.delete_images(False)
    elif userOperation == "5":
        FileIO.delete_images(True)
    elif userOperation == "6":
        MapillaryOperations.upload_images()
    elif userOperation == "-1":
        sys.exit(0)
