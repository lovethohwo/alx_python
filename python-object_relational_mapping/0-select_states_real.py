import MySQLdb
#Database parameters
host="localhost"
user="root"
passwd="Judyloveth@2023"
db="mysql"
port=3306

# Connect to the MySQL server
db = MySQLdb.connect(host=host, user=user, passwd=passwd, port=port, db=db)
cursor = db.cursor()

create = "CREATE TABLE IF NOT EXISTS states (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256) NOT NULL)"
cursor.execute(create)

# Insert
qry = 'INSERT INTO states (name) VALUES ("California"), ("Arizona")'
cursor.execute(qry)

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
