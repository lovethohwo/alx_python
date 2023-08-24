import MySQLdb
#Database parameters
host="localhost"
user="root"
passwd="Judyloveth@2023"
db="mysql"
port=3306

# Connect to the MySQL server
db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db)
cursor = db.cursor()

create = "CREATE TABLE IF NOT EXISTS states (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256) NOT NULL)"
cursor.execute(create)

def insert_entry():
    try:
        # Insert
        qry = 'INSERT INTO states (name) VALUES ("California"), ("Arizona")'
        cursor.execute(qry)
        # Attempt to insert the entry into the table
        '''
        insert_query = 
            INSERT INTO my_table (name)
            VALUES ("Texas"),("Arizona")
        
        cursor.execute(insert_query)
        conn.commit()
        print("Entry inserted successfully.")
        '''
    except MySQLdb.IntegrityError as e:
        print("Error:", e)
        print("Duplicate entry detected. Entry not inserted.")
        
# Example usage
insert_entry()
  # This will result in a duplicate entry error


# Execute the query to retrieve states
query = "SELECT * FROM states ORDER BY id ASC"
cursor.execute(query)

# Fetch all the results
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)

# Close the cursor and the database connection
cursor.close()
db.close()
