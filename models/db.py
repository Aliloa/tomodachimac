import mysql.connector
# for .env : 
import os
from dotenv import load_dotenv

load_dotenv()

# informations of the database depend on local .env
mydb = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
)