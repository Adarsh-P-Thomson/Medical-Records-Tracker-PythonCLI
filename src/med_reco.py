import mysql.connector
import datetime
username = 'root'
password = 'rouTer'
host = 'localhost'
database = 'healthrecord'

def display(query):
    # Create a connection object
    cnx = mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=database
    )
    # Create a cursor object
    cursor = cnx.cursor()
    # Execute a query
    
    cursor.execute(query)
    # Fetch the results
    results = cursor.fetchall()
    # Print the results
    for row in results:
        for ele in row:
            
            if isinstance(ele, (int, datetime.date, datetime.datetime)):
                ele = str(ele)
            print(ele.ljust(15), end=' ')
    print()
    # Close the cursor and connection
    cursor.close()
    cnx.close()
    
def qretiever(query):
    # Define the database connection parameters
    # Create a connection object
    cnx = mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=database
        )
    # Create a cursor object
    cursor = cnx.cursor()
    # Execute a query
    cursor.execute(query)
    # Fetch the results
    results = cursor.fetchall()
    cursor.close()
    cnx.close()
    return results

def insertvalue(query):
    # Define the database connection parameters
    # Create a connection object
    cnx = mysql.connector.connect(
        user=username,
        password=password,  
        host=host,
        database=database
        )
    # Create a cursor object
    cursor = cnx.cursor()
    # Execute a query
    cursor.execute(query)
    # Commit the change
    cnx.commit()
    cursor.close()
    cnx.close()

def deletevalue(query):
    # Define the database connection parameters
    # Create a connection object
    cnx = mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=database
        )
    # Create a cursor object
    cursor = cnx.cursor()
    # Execute a query
    cursor.execute(query)
    # Commit the change
    cnx.commit()
    cursor.close()
    cnx.close()

def updatevalue(query):
    insertvalue(query)
