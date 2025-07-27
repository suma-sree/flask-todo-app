
# Flask To-Do App

A simple web-based **To-Do application** built using **Flask** and **SQLAlchemy**, performing full **CRUD operations** to manage your daily tasks.

🔗 **Live Demo**: [View on Render](https://flask-todo-app-n2pp.onrender.com/)  

---

## 📌 Features

- 📝 Add new tasks
- 🔍 Search for tasks
- 🗑️ Delete tasks
- 🛠️ Update existing tasks
- 🗂️ View all tasks in a clean interface

---

## 🧱 Tech Stack

| Component   | Technology       |
|-------------|------------------|
| Backend     | Flask (Python)   |
| Database    | SQLite + SQLAlchemy |
| Frontend    | HTML, Bootstrap  |
| ORM         | Flask-SQLAlchemy |
| Deployment  | Render           |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/suma-sree/flask-todo-app.git
cd flask-todo-app
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask app locally

```bash
python app.py
```

Go to `http://localhost:5000` to view the app.

---

## 📂 Project Structure

```
flask-todo-app/
├── app.py
├── table.py
├── templates/
│   ├── index.html
│   └── update.html
|   └── base.html
├── static/
│   └── style.css
├── requirements.txt
└── README.md
```

---

## 🛠️ CRUD Operations Summary

| Operation | Route           | Method |
|-----------|------------------|--------|
| Create    | `/`           | POST   |
| Read      | `/`              | GET    |
| Update    | `/update/<id>`     | POST   |
| Delete    | `/delete/<id>`   | GET    |

---

## 🙋‍♀️ Author

- [Vankayalapati Sai Suma Sree](https://github.com/suma-sree)

---


## 🌟 Acknowledgments

- Flask documentation: https://flask.palletsprojects.com/
- SQLAlchemy ORM: https://www.sqlalchemy.org/
