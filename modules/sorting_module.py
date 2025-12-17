from datetime import date
from db import get_db_connection

def save_sorted_device(device_id, category, sorted_by, remarks):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    # Check if sorting already exists
    cursor.execute("SELECT * FROM SortingResults WHERE DeviceID = %s", (device_id,))
    existing = cursor.fetchone()
    
    if existing:
        # Update existing record
        cursor.execute("""
            UPDATE SortingResults
            SET SortingDate = %s, Category = %s, SortedBy = %s, Remarks = %s
            WHERE DeviceID = %s
        """, (date.today(), category, sorted_by, remarks, device_id))
    else:
        # Insert new record
        cursor.execute("""
            INSERT INTO SortingResults (DeviceID, SortingDate, Category, SortedBy, Remarks)
            VALUES (%s, %s, %s, %s, %s)
        """, (device_id, date.today(), category, sorted_by, remarks))
    
    conn.commit()
    cursor.close()
    conn.close()
