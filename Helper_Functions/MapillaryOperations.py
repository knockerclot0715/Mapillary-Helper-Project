import os
import subprocess

from Helper_Functions import TextFormatter


def process_images():
    try:
        subprocess.run(["clear"])
        subprocess.run(
            [os.path.dirname(os.path.dirname(__file__)) + "/Mapillary Program/mapillary_tools", "process",
             "--import_path", os.path.dirname(os.path.dirname(__file__)) + "/Captured Images/Source Images",
             "--user_name", "knockerclot0715"])
    except OSError as errorMessage:
        print("Failed!", errorMessage)
    finally:
        input(TextFormatter.YELLOW + TextFormatter.BLINK + "Press ENTER To Return..." + TextFormatter.RESET)
        return None


def post_process_images():
    try:
        subprocess.run(["clear"])
        subprocess.run(
            [os.path.dirname(os.path.dirname(__file__)) + "/Mapillary Program/mapillary_tools", "post_process",
             "--move_all_images", "--advanced", "--import_path",
             os.path.dirname(os.path.dirname(__file__)) + "/Captured Images/"])
    except OSError as errorMessage:
        print("Failed!", errorMessage)
    finally:
        input(TextFormatter.YELLOW + TextFormatter.BLINK + "Press ENTER To Return..." + TextFormatter.RESET)
        return None


def upload_images():
    try:
        subprocess.run(["clear"])
        subprocess.run(
            [os.path.dirname(os.path.dirname(__file__)) + "/Mapillary Program/mapillary_tools", "upload",
             "--import_path", os.path.dirname(os.path.dirname(__file__)) + "/Captured Images/to_be_uploaded"])
    except OSError as errorMessage:
        print("Failed!", errorMessage)
    finally:
        input(TextFormatter.YELLOW + TextFormatter.BLINK + "Press ENTER To Return..." + TextFormatter.RESET)
        return None
