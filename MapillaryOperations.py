import subprocess

import TextFormatter


def process_images():
    try:
        subprocess.run(["clear"])
        subprocess.run(
            ["Mapillary Program/mapillary_tools", "process", "--import_path", "Captured Images/Source Images",
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
            ["Mapillary Program/mapillary_tools", "post_process", "--move_all_images", "--advanced", "--import_path",
             "Captured Images/"])
    except OSError as errorMessage:
        print("Failed!", errorMessage)
    finally:
        input(TextFormatter.YELLOW + TextFormatter.BLINK + "Press ENTER To Return..." + TextFormatter.RESET)
        return None


def upload_images():
    try:
        subprocess.run(["clear"])
        subprocess.run(
            ["Mapillary Program/mapillary_tools", "upload", "--import_path", "Captured Images/Source Images"])
    except OSError as errorMessage:
        print("Failed!", errorMessage)
    finally:
        input(TextFormatter.YELLOW + TextFormatter.BLINK + "Press ENTER To Return..." + TextFormatter.RESET)
        return None
