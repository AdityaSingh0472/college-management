# College Student Management System

## Description
This project is a backend system built using Django (without Django REST Framework) to manage students and colleges. It provides REST APIs for performing CRUD operations and additional features like search, pagination, and filtering.

---

## Features

### Student APIs
- Create Student
- Get All Students (with search & pagination)
- Get Single Student
- Update Student
- Delete Student

### College APIs
- Create College
- Get All Colleges
- Get Single College
- Update College
- Delete College

### Additional Features
- Input Validation
- Error Handling
- Search Functionality
- Pagination
- Filtering by College

---

## Technologies Used
- Python
- Django
- SQLite

---

## API Endpoints

### Student APIs
- GET /api/students/
- POST /api/students/create/
- GET /api/students/{id}/
- PUT /api/students/update/{id}/
- DELETE /api/students/delete/{id}/

### College APIs
- GET /api/colleges/
- POST /api/colleges/create/
- GET /api/colleges/{id}/
- PUT /api/colleges/update/{id}/
- DELETE /api/colleges/delete/{id}/

---

## Setup Instructions
1. Clone the Repository
git clone https://https://github.com/AdityaSingh0472/college-management.git
cd your-repo-name

2. Create Virtual Environment
python -m venv venv

Activate it:

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Configure Environment Variables

Create a .env file and add:

SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_password

5. Apply Migrations
python manage.py makemigrations
python manage.py migrate

6. Run Server
python manage.py runserver

Server will run at:
http://127.0.0.1:8000/