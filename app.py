from flask import Flask 
from Routes.contacts import contacts
from flask_sqlalchemy import SQLAlchemy
from Utils.database import db
from Config.config import DATABASE_CONNECTION_URI

app = Flask(__name__)

app.secret_key = "mysecretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#db = SQLAlchemy(app)
db.init_app(app)

app.register_blueprint(contacts)