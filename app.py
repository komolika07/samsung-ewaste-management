from flask import Flask
from flask_wtf import CSRFProtect
from routes.admin_routes import admin_bp
from routes.sorting_routes import sorting_bp
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, 'templates'),
    static_folder=os.path.join(BASE_DIR, 'static')
)

app.secret_key = "secret-key"

csrf = CSRFProtect(app) 
# register blueprint
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(sorting_bp)

if __name__ == '__main__':
    app.run(debug=True)
