import psycopg2
from psycopg2 import OperationalError

    # Connect to the PostgreSQL database
dataBase = psycopg2.connect(
        host='localhost',        # Replace with your host
        user='postgres',             # Replace with your PostgreSQL username
        password='123'     # Replace with your PostgreSQL password
)

# Set autocommit mode to True
#This setting ensures that the CREATE DATABASE command is executed outside of a transaction block. 
# This is necessary because PostgreSQL does not allow the creation of a database inside a transaction.
dataBase.autocommit = True    
# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE testing")

print("ALL DONE!")

