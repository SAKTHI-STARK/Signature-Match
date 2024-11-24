import mysql.connector
from PIL import Image
from io import BytesIO
def retrieve_image(image_id, output_path):
    # Connect to the database
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='2011',
        database='image_db'
    )
    cursor = conn.cursor()
    # Retrieve the image data
    sql = "SELECT image FROM images WHERE id = %s"
    cursor.execute(sql, (image_id,))
    result = cursor.fetchone()
    if result:
        image_data = result[0]
        image = Image.open(BytesIO(image_data))
        image.save(output_path)
        print(f"Image saved at: {output_path}")
    else:
        print("Image not found.")
    cursor.close()
    conn.close()
