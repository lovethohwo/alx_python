import MySQLdb

# Connect to the MySQL server
db = MySQLdb.connect(host="localhost", user="root", passwd="Judyloveth@2023", db="mysql")
cursor = db.cursor()

create = '''  
    CREATE TABLE IF NOT EXISTS states (
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
        name VARCHAR(256) UNIQUE NOT NULL
        )
 '''
cursor.execute(create)
db.commit()

def insert_entry():
    # Attempt to insert the entry into the table
    sel= '''
        SELECT * FROM states ORDER BY id ASC
    '''
    cursor.execute(sel)
    found_rows = cursor.fetchall()
    num_rows = len(found_rows)
    if num_rows < 2:
        qry = 'INSERT INTO states (name) VALUES ("California"), ("Arizona")'
        cursor.execute(qry)
        db.commit()
       # results = cursor.fetchall()

# Print the results
        for row in found_rows:
            print(row)
    else:
        print("")
insert_entry()
  # This will result in a duplicate entry error


# Execute the query to retrieve states


# Fetch all the results


# Close the cursor and the database connection
cursor.close()
db.close()
