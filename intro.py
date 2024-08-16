import mysql.connector
from mysql.connector import Error



#We need to install mysql connector package for python
#use pip install

# TO establish a connection to our databaser we are gonna need some parameters
#Database name 

db_name = 'ecom'   #database name 
user = 'root'
password = '!?12ABpp'
host = 'localhost'  # = from my PC - can also be an IP address '127.0.0.1'

#Now we are gonna establish a connection to our database
#We need to use the connect() function of the mysql.connector package
try: 
    conn= mysql.connector.connect(
        database = db_name,
        user = user,
        password = password,
        host = host
        )

    if conn.is_connected():
        print('Connected to MySQL database')
    cursor = conn.cursor() # creating a cursor to act as a middle man between python and mysql
    query = 'SELECT * FROM customer;'
    cursor.execute(query)   # passing our query over to cursor and executing it 
#fetching the result
    for row in cursor.fetchall():
        print(row)    #Prints each row - end on the TRY block 

except Error as e:
    print(f"Error{e}")

finally:    # Makes it work no matter what 
    if conn and conn.is_connected ():
        cursor.close()
        conn.close()  # Make sure you close your connections when finished with query
        print('MySQL connection is closed')

#Make a function for this db_connection.py





