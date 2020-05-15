import ast
import datetime
import glob
import os
import shutil
import subprocess

from PIL import Image
from PIL.ExifTags import TAGS

from Helper_Functions import TextFormatter, DatabaseIO


def delete_images(image_validity):
    subprocess.run(["clear"])
    if image_validity:
        print("Deleting Valid Images")
        image_directory = os.path.dirname(os.path.dirname(__file__)) + '/Captured Images/uploaded/**/*.jpg'
    else:
        print("Deleting Invalid Images")
        image_directory = os.path.dirname(os.path.dirname(__file__)) + '/Captured Images/duplicates/**/*.jpg'
    image_directory_list = glob.glob(image_directory, recursive=True)
    for image in image_directory_list:
        data = extract_image_exif(image, image_validity)
        if DatabaseIO.insert_captured_images(data):
            try:
                os.remove(image_directory)
            except OSError as error_message:
                print(TextFormatter.RED + "Failed To Delete Image: " + TextFormatter.UNDERLINED + "{0}".format(
                    error_message) + TextFormatter.RESET)


def extract_image_exif(image_directory, image_validity):
    image_file = Image.open(image_directory)
    image_exif_data = image_file._getexif()
    exif_data = {}
    for tag, value in image_exif_data.items():
        decoded = TAGS.get(tag, tag)
        exif_data[decoded] = value
    exif_gps_data = ast.literal_eval(exif_data['ImageDescription'])
    latitude = exif_gps_data['MAPLatitude']
    longitude = exif_gps_data['MAPLongitude']
    time = datetime.datetime.strptime(exif_gps_data['MAPCaptureTime'], '%Y_%m_%d_%H_%M_%S_%f')
    data = (time, latitude, longitude, image_validity)
    return data


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

