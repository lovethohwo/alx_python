import MySQLdb
#Database parameters
host="localhost"
user="root"
passwd="Judyloveth@2023"
db="hbtn_0e_0_usa"
# Connect to the MySQL server
db = MySQLdb.connect(host, user, passwd, db)
cursor = db.cursor()

# Execute the query to retrieve states
query = "SELECT * FROM states ORDER BY states.id ASC"
cursor.execute(query)

# Fetch all the results
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)

# Close the cursor and the database connection
cursor.close()
db.close()
