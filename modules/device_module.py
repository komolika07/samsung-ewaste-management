import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="komolika$2715",   # your MySQL password
        database="ewaste_management"
    )

def save_device(form):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO device_registration
        (name, phone, email, device_type, brand,
         device_condition, center, manufacturing_date,
         received_date, notes)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    data = (
        form.get('name'),
        form.get('phone'),
        form.get('email'),
        form.get('device_type'),
        form.get('brand'),
        form.get('device_condition'),
        form.get('center'),
        form.get('manufacturing_date'),
        form.get('received_date'),
        form.get('notes')
    )

    cursor.execute(query, data)
    conn.commit()

    cursor.close()
    conn.close()
