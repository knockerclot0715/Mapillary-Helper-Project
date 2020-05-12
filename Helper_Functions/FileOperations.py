import ast
import datetime
import glob
import os
import shutil
import subprocess

from PIL import Image
from PIL.ExifTags import TAGS

from Helper_Functions import TextFormatter, DatabaseInterface


def delete_directory(directory):
    subprocess.run(["clear"])
    try:
        directory = os.path.dirname(os.path.dirname(__file__)) + directory
        if os.path.exists(directory):
            shutil.rmtree(directory)
        print(TextFormatter.GREEN + "Successfully Deleted Directory: " + TextFormatter.UNDERLINED + "{0}".format(
            directory) + TextFormatter.RESET)
    except OSError as errorMessage:
        print(TextFormatter.RED + "Failed To Delete Directory: " + TextFormatter.UNDERLINED + "{0}".format(
            errorMessage) + TextFormatter.RESET)
    finally:
        input(TextFormatter.YELLOW + TextFormatter.BLINK + "Press ENTER To Return..." + TextFormatter.RESET)
        return None


def move_directory(source_directory):
    subprocess.run(["clear"])
    try:
        shutil.move(source_directory, os.path.dirname(os.path.dirname(__file__)) + '/Captured Images/Source Images')
        print(TextFormatter.GREEN + "Successfully Moved Directory: " + TextFormatter.UNDERLINED + "{0}".format(
            source_directory) + TextFormatter.RESET)
    except OSError as errorMessage:
        print(TextFormatter.RED + "Failed To Move Directory: " + TextFormatter.UNDERLINED + "{0}".format(
            errorMessage) + TextFormatter.RESET)
    finally:
        input(TextFormatter.YELLOW + TextFormatter.BLINK + "Press ENTER To Return..." + TextFormatter.RESET)
        return None


def delete_thumbnails():
    subprocess.run(["clear"])
    try:
        directory = os.path.dirname(os.path.dirname(__file__)) + "/Captured Images/Source Images/**/*-thumb.jpg"
        for file in glob.glob(directory, recursive=True):
            os.remove(file)
        print(TextFormatter.GREEN + "Successfully Deleted All Thumbnails: " + TextFormatter.UNDERLINED + "{0}".format(
            directory) + TextFormatter.RESET)
    except OSError as errorMessage:
        print(TextFormatter.RED + "Failed To Delete Thumbnail: " + TextFormatter.UNDERLINED + "{0}".format(
            errorMessage) + TextFormatter.RESET)
    finally:
        input(TextFormatter.YELLOW + TextFormatter.BLINK + "Press ENTER To Return..." + TextFormatter.RESET)
        return None


def directory_generator():
    try:
        directory = os.path.dirname(os.path.dirname(__file__)) + '/Captured Images/Source Images'
        if not os.path.exists(directory):
            os.makedirs('Captured Images/Source Images')
    except OSError as errorMessage:
        print(TextFormatter.RED + "Failed To Create Necessary Directories: " + TextFormatter.UNDERLINED + "{0}".format(
            errorMessage) + TextFormatter.RESET)
    finally:
        return None


def get_uploaded_images_metadata():
    directory = os.path.dirname(os.path.dirname(__file__)) + '/Captured Images/uploaded/**/*.jpg'
    images_path = glob.glob(directory, recursive=True)

    if DatabaseInterface.check_database_connection():
        bulk_data = []
        for image_path in images_path:
            image_file = Image.open(image_path)
            meta_data = image_file._getexif()
            EXIF_data = {}
            for tag, value in meta_data.items():
                decoded = TAGS.get(tag, tag)
                EXIF_data[decoded] = value
            exif_gps = ast.literal_eval(EXIF_data['ImageDescription'])
            GPSLatitude = exif_gps['MAPLatitude']
            GPSLongitude = exif_gps['MAPLongitude']
            UTCTime = datetime.datetime.strptime(exif_gps['MAPCaptureTime'], '%Y_%m_%d_%H_%M_%S_%f')
            bulk_data.append((UTCTime, GPSLatitude, GPSLongitude))
        if DatabaseInterface.check_database_connection():
            if DatabaseInterface.insert(bulk_data):
                print("Yes")
