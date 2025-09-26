#  Flask REST API with MySQL

This project is a fully functional REST API built using Flask and MySQL. It supports CRUD operations for managing user data and is designed for interview demos, automation tasks, and scalable backend development.

##  Tech Stack
- Python 3.x
- Flask
- Flask-SQLAlchemy
- MySQL
- Postman / Curl (for testing)

##  Features
- `POST /users` → Create a new user
- `GET /users` → Retrieve all users
- `GET /users/<id>` → Retrieve a specific user
- `PUT /users/<id>` → Update user details
- `DELETE /users/<id>` → Delete a user

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Brahma6303/flask-user-api.git
cd flask-user-api

## 2.Create Virtual Environment

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3. Install Dependencies
    pip install -r requirements.txt

4. Configure MySQL
   Create a database named flask_users in MySQL:
   CREATE DATABASE flask_users;

   Update config.py with your MySQL credentials.

5. Run the App
   python app.py

Responses and Requests
1.Get All Users (GET /users)
<img width="1920" height="1200" alt="Screenshot 2025-09-26 125127" src="https://github.com/user-attachments/assets/51d40578-0df7-4ed2-bf91-d2479e4b1364" />

2.Create User (POST /users)
<img width="1920" height="1200" alt="Screenshot 2025-09-26 125529" src="https://github.com/user-attachments/assets/5e68c272-75d8-4e03-8d08-b3b7bd1254c7" />

3.Update User (PUT /users/1)
<img width="1920" height="1200" alt="Screenshot 2025-09-26 130416" src="https://github.com/user-attachments/assets/e835e44e-d5ec-41ed-9c5e-886beff866cd" />

4.Delete User (DELETE /users/1)
<img width="1920" height="1200" alt="Screenshot 2025-09-26 130532" src="https://github.com/user-attachments/assets/6f6c41a6-bae6-4dc1-adb5-e899190f2834" />









