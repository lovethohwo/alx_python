import MySQLdb

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
