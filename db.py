import mysql.connector
from flask import Flask

def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="komolika$2715",  # put your password here
        database="ewaste_management"
    )
    return connection
