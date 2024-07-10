import mysql.connector

def connect_Server(retrievekey):
    # Define the database connection parameters
    username = 'root'
    password = 'rouTer'
    host = 'localhost'
    database = 'healthdatabase'

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
    query = "SELECT * FROM users"
    cursor.execute(query)

    # Fetch the results
    results = cursor.fetchall()

    # Print the results
    for row in results:
        print(row)

    # Close the cursor and connection
    cursor.close()
    cnx.close()