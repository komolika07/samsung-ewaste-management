from flask import Blueprint, render_template, redirect, url_for, flash, request
from datetime import date
import mysql.connector
from forms import DeviceForm

admin_bp = Blueprint('admin', __name__)

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="komolika$2715",
    database="ewaste_management"
)

@admin_bp.route('/register', methods=['GET', 'POST'])
def register_device():
    form = DeviceForm()
    form.received_date.data = date.today()

    if form.validate_on_submit():
        cursor = db.cursor()

        # Map device condition to StatusID
        status_map = {"Working": 1, "Partially Working": 2, "Not Working": 3}
        status_id = status_map.get(form.device_condition.data)

        # Map center to CollectionPointID
        center_map = {"Andheri": 1, "Bandra": 2, "Navi Mumbai": 3}
        collection_point_id = center_map.get(form.center.data)

        # Insert into devices table
        query = """
        INSERT INTO devices 
        (SerialNumber, DeviceType, Brand, Model, ManufactureDate, CollectionPointID, StatusID, ReceivedDate)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            form.serial_number.data,
            form.device_type.data,
            form.brand.data,
            form.model.data,
            form.manufacture_date.data,
            collection_point_id,
            status_id,
            form.received_date.data
        )

        try:
            cursor.execute(query, values)
            db.commit()
            flash("Device registered successfully!", "success")
        except Exception as e:
            db.rollback()
            flash(f"Error: {str(e)}", "danger")
        finally:
            cursor.close()

        return redirect(url_for('admin.register_device'))

    return render_template('admin/deviceRegister.html', form=form, today=date.today())
