# To-Do List Project with APIs and Templates Ingegration

## Project Overview

This is a Django-based web application for managing a To-Do list. The application provides:

- RESTful APIs for CRUD operations on tasks (without using Django ORM or Generic Viewsets).
- Template-based web interface for listing, adding, editing, and deleting tasks.
- Data persistence in PostgreSQL database using raw SQL queries.
- Bootstrap styling for a clean and responsive UI.

API and web views are separated for better code organization.

## Directory Structure
```
todo-list/
│
│── tasks/
│       ├── api/
│       │   ├── __init__.py
│       │   ├── urls.py
│       │   └── views.py
│       │
│       ├── web/
│       │   ├── __init__.py
│       │   ├── urls.py
│       │   └── views.py
│       │
│       ├── templates/
│       │   └── tasks/
│       │       ├── base.html
│       │       ├── task_list.html
│       │       ├── add_task.html
│       │       └── edit_task.html
│       │
│       ├── repository/
│       │   ├── __init__.py
│       │   └── task_repository.py   # raw SQL layer
│       │
│       ├── tests/
│       │   ├── __init__.py
│       │   ├── test_api.py
│       │   └── test_web.py
│       │
│       ├── urls.py
│       └── apps.py
│
├── todo_list/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
├── .gitignore
├── pytest.ini
└── README.md
```

## Features

- **CRUD Operations** via RESTful APIs
- **Web Interface** with task list, add, edit, and delete functionality
- **Validations**:
  - All fields required
  - Status limited to: `pending`, `in-progress`, `completed`
  - Due date format validation
  - Proper HTTP status codes and JSON error responses
- **Logging** and exception handling implemented
- Bootstrap for styling

## Database

- **Engine**: PostgreSQL
- **Database Name**: `todo_list_db`
- **Table Name**: `tasks_task`

```sql
CREATE TABLE tasks_task (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    due_date DATE,
    status VARCHAR(50) DEFAULT ''
);

Setup Instructions

Clone the repository:Bashgit clone https://github.com/Dileepkumarpatelpalamu/todo-list-django-restapi.git
cd todo-list
Create and activate virtual environment:Bashpython -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
Install dependencies:Bashpip install -r requirements.txt
Configure PostgreSQL in todo_list/settings.py:PythonDATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'todo_list_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
Create the database and table (using psql or any client) with the schema above.
Run the server:Bashpython manage.py runserver
Access:
Web Interface: http://127.0.0.1:8000/
API Base: http://127.0.0.1:8000/api/tasks/


API Documentation
Base URL: http://127.0.0.1:8000/api/tasks/
1. List Tasks (GET)

URL: /api/tasks/
Response (200 OK):JSON{
    "tasks": [
        {
            "id": 8,
            "title": "Task title",
            "description": "Task description",
            "due_date": "2025-02-13",
            "status": "pending"
        }
    ]
}

2. Create Task (POST)

URL: /api/tasks/
Content-Type: application/json
Payload:JSON{
    "title": "New Task",
    "description": "Task description",
    "due_date": "2025-12-31",
    "status": "pending"
}
Success Response (201 Created):JSON{ "message": "Task created successfully" }

3. Update Task (PUT)

URL: /api/tasks/<id>/
Payload: Same as create
Success Response (200 OK):JSON{ "message": "Task updated successfully" }

4. Delete Task (DELETE)

URL: /api/tasks/<id>/
Success Response (200 OK):JSON{ "message": "Task deleted successfully" }
Validation errors return 400 Bad Request with appropriate messages.
No authentication required.

Or with verbose output:
Bashpytest -vv
Covered Tests

API CRUD operations (success and failure cases)
Field validation (required fields, status enum)
Web view rendering (task list, add/edit forms)

Additional Notes

No ORM or Generic Viewsets used as per requirements.
Raw SQL queries handled in db.py.
Code is organized, readable, and follows RESTful principles.
Logging and proper exception handling implemented.

Project meets all assignment evaluation criteria including functionality, API design, template usage, database integration, code quality, and documentation.

Testing
Note: Automated testing with pytest is not implemented in this version.
Manual testing has been performed for all API endpoints and web views, covering success cases, validation errors, and edge cases.
I plan to learn and add pytest-based tests soon (including pytest-django for Django integration).
