from dotenv import load_dotenv
import mysql.connector
import os

load_dotenv(dotenv_path=".env")

conn = mysql.connector.connect(
    host = os.getenv("host"),
    user = os.getenv("user"),
    password = os.getenv("password"),
    database = os.getenv("database")
)

cursor = conn.cursor()