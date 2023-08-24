import MySQLdb

# Connect to the MySQL server
db = MySQLdb.connect(host="localhost", user="root", passwd="Judyloveth@2023", db="mysql")
cursor = db.cursor()

create = '''  
    CREATE TABLE IF NOT EXISTS states (
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
        name VARCHAR(256) NOT NULL
        )
 '''
cursor.execute(create)
db.commit()

def insert_entry():
    try:
        # Attempt to insert the entry into the table
        qry = 'INSERT INTO states (name) VALUES ("California"), ("Arizona")'
        cursor.execute(qry)
        db.commit()
        
    except MySQLdb.IntegrityError as e:
        print("Error:", e)
        
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
