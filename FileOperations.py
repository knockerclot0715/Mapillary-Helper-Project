import glob
import os
import shutil
import subprocess

import TextFormatter


def delete_directory(directory):
    subprocess.run(["clear"])
    try:
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
        shutil.move(source_directory, 'Mapillary Program/Source Images')
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
