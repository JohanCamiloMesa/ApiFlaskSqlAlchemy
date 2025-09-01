# 🧖‍♂️ Flask Contact Manager API

A complete REST API developed with Flask to manage contacts. Includes full CRUD operations, MySQL database integration, and a clean modular architecture.

## ✨ Features

- 🚀 Complete REST API with CRUD operations
- 🗄️ MySQL database with SQLAlchemy
- 📝 Contact information management
- 🎨 Clean and responsive UI with Bootstrap
- ✅ Form validation 
- 🛡️ Centralized error handling
- 📊 Flash messages for user feedback
- 🏗️ Modular architecture (MVC)

## 🛠️ Technologies Used

- **Flask** - Web framework
- **SQLAlchemy** - Database ORM
- **MySQL** - Database
- **Bootstrap** - Frontend styling
- **python-dotenv** - Environment variables
- **Jinja2** - Template engine

## 📁 Project Structure

```
ApiFlaskSqlAlchemy/
├── Config/
│   └── config.py         # Database configuration
├── Database/
│   └── db.sql           # SQL database schema
├── Models/
│   └── contact.py       # Contact model definition
├── Routes/
│   └── contacts.py      # API endpoints
├── Templates/
│   ├── Partials/       # Reusable template components
│   └── *.html          # View templates
├── Utils/
│   └── database.py     # Database utilities
└── static/
    └── css/            # Custom styles
```

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- MySQL
- pip (Python package installer)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd ApiFlaskSqlAlchemy
```

2. Create virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
```properties
MYSQL_USER = your_user
MYSQL_PASSWORD = your_password
MYSQL_HOST = localhost
MYSQL_DB = contactos
```

5. Initialize database:
```sql
CREATE DATABASE IF NOT EXISTS contactos;
```

### 🏃‍♂️ Running the Application

```bash
python index.py
```

Visit `http://localhost:5000` in your browser.

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | View all contacts |
| POST | /new | Create contact |
| GET | /update/<id> | Get contact for editing |
| POST | /update/<id> | Update contact |
| GET | /delete/<id> | Delete contact |

## 👥 Contributing

1. Fork the project
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📝 License

This project is licensed under the MIT License

## ✍️ Author

Johan Camilo Mesa

## 🙏 Acknowledgments

- Flask Documentation
- SQLAlchemy Documentation
- Bootstrap Documentation