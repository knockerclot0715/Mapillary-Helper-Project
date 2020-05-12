import mysql.connector
from mysql.connector import errorcode


def check_database_connection():
    try:
        database_connection = mysql.connector.connect(user='MapillaryHelper', password='test', host='localhost',
                                                      database='Mapillary_Database')
        database_connection.close()
        return True
    except mysql.connector.Error as error_message:
        if error_message.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif error_message.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(error_message)


def insert(bulk_data):
    try:
        database_connection = mysql.connector.connect(user='MapillaryHelper', password='test', host='localhost',
                                                      database='Mapillary_Database')
        database_cursor = database_connection.cursor()
        insert_command = "INSERT IGNORE INTO Uploaded_Image_Record (Captured_UTC_Timestamp, Latitude, Longitude) " \
                         "VALUES (%s, %s, %s) "
        database_cursor.executemany(insert_command, bulk_data)
        database_connection.commit()
        database_cursor.close()
        database_connection.close()
        return True
    except mysql.connector.Error as error_message:
        if error_message.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif error_message.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(error_message)
