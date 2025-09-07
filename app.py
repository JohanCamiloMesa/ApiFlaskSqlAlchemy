from flask import Flask
from Controller.animes_controller import animes
from Utils.database import db
from Config.db_config import DATABASE_CONNECTION_URI

app = Flask(__name__)

# Configure Flask-SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "mysecretkey"

# Initialize SQLAlchemy with app
db.init_app(app)

# Register blueprints
app.register_blueprint(animes)