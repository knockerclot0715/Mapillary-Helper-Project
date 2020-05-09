import glob
import os
import shutil
import subprocess

from Helper_Functions import TextFormatter


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


def delete_thumbnails(directory):
    subprocess.run(["clear"])
    try:
        directory = os.path.dirname(os.path.dirname(__file__)) + directory
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
