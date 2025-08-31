# Hospital Management System Backend

This is the backend for the Hospital Management System (HMS), built with **Django**, **Django REST Framework (DRF)**, and **JWT authentication**. It provides APIs for user authentication, managing patients, appointments, lab results, and internal messages.

---

## Features

- User authentication with JWT (Admin, Doctor, Receptionist, Patient)
- CRUD APIs for:
  - Patients
  - Appointments
  - Lab Results
  - Messages
- Role-based access control
- File uploads for lab results

---

## Technologies Used

- Python 3.10+
- Django 5.2
- Django REST Framework
- Django Filters
- djangorestframework-simplejwt
- SQLite (default database)

---

## API Endpoints

| Endpoint                  | Method    | Description                         |
|---------------------------|----------|-------------------------------------|
| `/api/auth/register/`     | POST     | Register a new user                 |
| `/api/auth/token/`        | POST     | Obtain JWT access & refresh tokens |
| `/api/auth/token/refresh/`| POST     | Refresh JWT access token            |
| `/api/patients/`          | GET/POST | List or create patients             |
| `/api/appointments/`      | GET/POST | List or create appointments         |
| `/api/lab-results/`       | GET/POST | List or create lab results          |
| `/api/messages/`          | GET/POST | List or send messages               |

**Note:** All endpoints (except register & token) require **JWT authentication**.
