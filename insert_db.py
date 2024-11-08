import mysql.connector
def insert_image(file_path):
    # Connect to the database
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='2011',
        database='image_db'
    )
    cursor = conn.cursor()
    # Read the image file
    with open(file_path, 'rb') as file:
        binary_data = file.read()
    # Insert the image into the database
    sql = "INSERT INTO images (image) VALUES (%s)"
    cursor.execute(sql, (binary_data,))
    conn.commit()
    print("Image inserted successfully!")
    cursor.close()
    conn.close()

