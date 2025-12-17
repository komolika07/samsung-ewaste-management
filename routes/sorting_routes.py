from flask import Blueprint, render_template, request, redirect, url_for, flash
from modules.sorting_module import save_sorted_device
from db import get_db_connection
sorting_bp = Blueprint('sorting', __name__, url_prefix='/admin')

@sorting_bp.route('/sort-device', methods=['GET', 'POST'])
def sort_device():
    if request.method == 'POST':
        device_id = request.form.get('device_id')
        category = request.form.get('category')
        sorted_by = "admin"  # or fetch from session
        remarks = request.form.get('remarks')

        save_sorted_device(device_id, category, sorted_by, remarks)
        flash("Device sorted successfully!", "success")
        return redirect(url_for('sorting.sort_device'))

    # GET request: fetch all registered devices
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM devices")
    devices = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('admin/sorting.html', devices=devices)

