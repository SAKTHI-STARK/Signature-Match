import mysql.connector

# Connect to MySQL server
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='2011'
)
cursor = conn.cursor()

# Create a new database
cursor.execute("CREATE DATABASE IF NOT EXISTS image_db")

# Connect to the new database
conn.database = 'image_db'

# Create a table for storing images
cursor.execute("""
CREATE TABLE IF NOT EXISTS images (
    id INT AUTO_INCREMENT PRIMARY KEY,
    image BLOB
)
""")

print("Database and table created successfully!")

cursor.close()
conn.close()
