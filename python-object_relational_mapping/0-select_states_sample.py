import MySQLdb

# Connect to the MySQL database
#Database parameters
host="localhost"
user="root"
passwd="Judyloveth@2023"
db="mysql"
port=3306
conn = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="Judyloveth@2023",
    db="hbtn_0c_0"
)
cursor = conn.cursor()

# Create the table if it doesn't exist
create_table_query = '''
    CREATE TABLE IF NOT EXISTS states (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) UNIQUE
    )
'''
cursor.execute(create_table_query)
conn.commit()

def insert_entry(name):
    try:
        # Attempt to insert the entry into the table
        insert_query = '''
            INSERT INTO states (name)
            VALUES (1%S)
        '''
        cursor.execute(insert_query)
        conn.commit()
        print("Entry inserted successfully.")
    except MySQLdb.IntegrityError as e:
        print("Error:", e)
        print("Duplicate entry detected. Entry not inserted.")

# Example usage
insert_entry("Texas")
  # This will result in a duplicate entry error

# Execute the query to retrieve states
query = "SELECT * FROM states ORDER BY id ASC"
cursor.execute(query)

# Fetch all the results
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)


# Close the connection
conn.close()
