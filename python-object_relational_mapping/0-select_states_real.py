import MySQLdb
import sys

host="localhost"
user="root"
passwd="Judyloveth@2023"
db="mysql"
port=3306

def list_states(user, passwd, db):
    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=passwd, db=db)
        
        # Create a cursor object to interact with the database
        cursor = db.cursor()
        
        # Execute the query to retrieve states
        query = "SELECT * FROM states ORDER BY id ASC"
        cursor.execute(query)
        
        # Fetch all the results
        results = cursor.fetchall()
        
        # Display the results
        for row in results:
            print(row)
        
        # Close the cursor and database connection
        cursor.close()
        db.close()
        
    except MySQLdb.Error as e:
        print("Error:", e)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <mysql_username> <mysql_password> <database_name>")
    else:
        user = sys.argv[1]
        passwd = sys.argv[2]
        db = sys.argv[3]
        list_states(user, passwd, db)
