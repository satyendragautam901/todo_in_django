# 📝 Django TODO API

A simple and clean Django-based TODO application built for practice and learning. This project covers essential CRUD operations, authentication, and user-specific data access using Django and may be Django REST Framework (DRF).

---

## ✅ Features

| Feature | Description |
|--------|-------------|
| 🔐 **Register** | Create a new user using a registration form |
| 🔐 **Login** | Token-based login using DRF Token Auth or JWT |
| 📝 **Create Task** | Authenticated users can create personal tasks |
| 📋 **List Tasks** | Fetch all tasks for the logged-in user |
| 🔍 **Task Detail** | View details of a specific task |
| ✏️ **Update Task** | Edit task title, description, or status |
| ❌ **Delete Task** | Delete a specific task |
| ✅ **Mark Complete** | Mark a task as complete/incomplete |
| 🔎 **Filter Tasks** | (Optional) Filter tasks by `is_completed=True/False` |

---

## 🏗️ Tech Stack

- **Backend:** Django + Django REST Framework
- **Authentication:** Token django built-in 
- **Database:** SQLite (for development)
- **Frontend:** Simple Tailwind-styled HTML templates

---

## 🚀 Getting Started

1. **Clone the repository**
```bash
git clone https://github.com/satyendragautam901/todo_in_django.git
cd todo_in_django
```
2. **Create and activate virtual environment**

```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```
pip install -r requirements.txt

```

4. **Run migrations**
```
python manage.py migrate

```

5. **Run the development server**

```
python manage.py runserver

```

### API Endpoints (Planned)

| Method      | Endpoint                    | Description         |
| ----------- | --------------------------- | ------------------- |
| `POST`      | `/register/`                | User registration   |
| `POST`      | `/login/`                   | Login and get token |
| `GET`       | `/tasks/`                   | List user tasks     |
| `POST`      | `/tasks/`                   | Create new task     |
| `GET`       | `/tasks/<id>/`              | Task detail         |
| `PUT/PATCH` | `/tasks/<id>/`              | Update task         |
| `DELETE`    | `/tasks/<id>/`              | Delete task         |
| `GET`       | `/tasks/?is_completed=true` | Filter tasks        |


### 📁 Folder Structure

    ├── todo/
    │   ├── settings.py
    │   └── urls.py
    ├── main/
    │   ├── models.py
    │   ├── views.py
    │   └── urls.py
    ├── templates/
    │   ├── register.html
    │   └── login.html
    └── README.md
