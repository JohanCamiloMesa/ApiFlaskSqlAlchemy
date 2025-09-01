from app import app
from Utils.database import db
import Config.config  # Ensure config is loaded

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)