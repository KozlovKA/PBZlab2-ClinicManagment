from typing import Tuple

import mysql.connector


def create_connection(host: str = 'localhost', port: str = '3306',
                      user: str = 'root', password: str = '1104',
                      database: str = 'pbz2') -> Tuple:
    connection = mysql.connector.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )

    cursor = connection.cursor()

    return connection, cursor


def close_connection(connection, cursor):
    """
    Closes cursor and connection
    :param connection: connection to mysql database
    :param cursor: cursor for given connection
    """

    connection.close()
    cursor.close()
