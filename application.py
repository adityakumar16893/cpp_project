import os
import sys

from flask import Flask, render_template, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

base_path = os.path.dirname(__file__)
api_path = os.path.join(base_path, "api/")
models_path = os.path.join(base_path, "models/")

sys.path.insert(0, base_path)
sys.path.insert(1, api_path)
sys.path.insert(2, models_path)

import services

class CppMain:
    def __init__(self, app):
        self.app = app
        self.srvc = services.register_services(self.app)

# creating application
application = Flask(__name__)
CORS(application)

@application.route('/')
def index():
    return render_template('app.html')

application.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:python123@database-4.cvmkcdhwam9i.us-east-1.rds.amazonaws.com:5432/student"
db = SQLAlchemy(application)

if __name__ == '__main__':
    app = CppMain(application)
    application.run(host='0.0.0.0', port=7000, debug=True)
