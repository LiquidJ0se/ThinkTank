import sqlite3

# Create a connection to the database.
conn = sqlite3.connect('books.db')

# Execute a query to select all columns from the table.
cur = conn.cursor()
cur.execute('SELECT * FROM book')

# Use the with statement to open a file in write mode.
with open('90xdatabase.txt', 'w') as f:

    # Write the results of the query to the file.
    for row in cur.fetchall():
        for column in row:
            f.write(str(column)+ ',')
        f.write('\n')

# Close the file.
f.close()