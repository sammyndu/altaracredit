from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

app = Flask(__name__, instance_relative_config=True)

app.config.from_pyfile('config.py', silent=False)

db=SQLAlchemy(app)

csrf = CSRFProtect()
csrf.init_app(app)

from cbtpackage import view_admin, view_user