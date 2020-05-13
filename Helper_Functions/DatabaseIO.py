import os
import sqlite3


def check_database_connection():
    try:
        database_directory = directory = os.path.dirname(os.path.dirname(__file__)) + '/SQL/MapillaryDatabase.db3'
        script_directory = os.path.dirname(os.path.dirname(__file__)) + '/SQL/InitializeSchema.sql'
        if os.path.isfile(directory):
            database_connection = sqlite3.connect(database_directory)
            database_connection.close()
            return True
        else:
            database_connection = sqlite3.connect(database_directory)
            database_connection.execute(script_directory)
            database_connection.close()
            return True
    except sqlite3.Error as error_message:
        print("Database Error: {0}".format(error_message))
    except Exception as error_message:
        print("Error: {0}".format(error_message))


def insert_uploaded_images(data):
    try:
        directory = os.path.dirname(os.path.dirname(__file__)) + '/SQL/MapillaryDatabase.db3'
        database_connection = sqlite3.connect(directory)
        database_connection.executemany("INSERT or IGNORE INTO Captured_Images (Captured_Time_UTC, Latitude, "
                                        "Longitude, Valid_Image) VALUES ( ?, ?, ?, ?)", data)
        database_connection.commit()
        database_connection.close()
    except sqlite3.Error as error_message:
        print("Database Error: {0}".format(error_message))
    except Exception as error_message:
        print("Error: {0}".format(error_message))
