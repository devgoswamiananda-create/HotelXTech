# 🏨 Hotel Management System

A polished desktop hotel-management project built with **Python, Tkinter, MySQL and Pillow**. It provides customer management, room-booking workflows and automatic billing calculations through a simple GUI.

## ✨ Highlights

- Customer registration and database storage
- Room booking workflow
- Customer lookup from room booking
- Automatic stay-duration calculation
- Room + meal pricing and 10% tax calculation
- MySQL persistence with parameterized queries
- Environment-based database credentials
- Dependency management with `requirements.txt`
- Database setup with `schema.sql`
- No hard-coded Windows paths or database passwords

## 📁 Structure

```text
hotel-management-system/
├── app.py
├── schema.sql
├── requirements.txt
├── .env.example
└── .gitignore
```

## 🚀 Run locally

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Configure the database using the variables in `.env.example` (or your OS environment):

```text
HOTEL_DB_HOST=localhost
HOTEL_DB_USER=root
HOTEL_DB_PASSWORD=your_local_mysql_password
HOTEL_DB_NAME=management
```

Create the database:

```bash
mysql -u root -p < schema.sql
```

Start the application:

```bash
python app.py
```

## 🧪 Validation

```bash
python -m py_compile app.py
```

## 🛠️ Stack

- Python
- Tkinter / ttk
- MySQL
- mysql-connector-python
- Pillow

## 🔐 Security

Never commit real database credentials. `.env` is ignored by Git and `.env.example` contains placeholders only.

## 🔭 Roadmap

- Real-time room availability
- Reservation history
- PDF invoices
- Dashboard analytics
- Authentication and roles
- Automated tests and CI
- Better separation into service/repository layers

## 👨‍💻 Author

**Ananda Devgoswami**  
B.Tech CSE — Artificial Intelligence & Machine Learning
