
# 📝 Healthcare Backend 
## Project Description

The **Healthcare API** is a backend system built using **Django Rest Framework (DRF)** with **JWT Authentication**. It provides a structured and secure way to manage healthcare data, including **users, patients, doctors, and their relationships (mappings)**.

This project simulates a **basic healthcare management system**, where:

* Users can **register and authenticate** using JWT.
* Admins or authenticated users can **create and manage patient and doctor records**.
* Patients can be **assigned to doctors** through a mapping system, making it possible to track which doctor is responsible for which patient.

The API is fully **REST-compliant**, supporting **CRUD operations** (Create, Read, Update, Delete) for patients and doctors, and also includes endpoints for **assigning, retrieving, and removing patient-doctor relationships**.

It is designed as a **learning and demonstration project** to showcase:
✅ User authentication with JWT
✅ REST API development with DRF
✅ Database modeling for healthcare use-cases
✅ CRUD operations for patients & doctors
✅ Many-to-many relationship handling with mappings
✅ Secure API endpoints with permissions
✅ Admin panel support for data management

This backend system can serve as the **foundation for a larger healthcare application**, such as:

* A **patient-doctor appointment booking system**
* A **medical record management platform**
* A **hospital or clinic management system**

---




````markdown
# 🏥 Healthcare API (Django + DRF + JWT)

A simple **Healthcare Management Backend** built with **Django Rest Framework (DRF)** and **JWT Authentication**.  
It supports managing **Users, Patients, Doctors, and Patient-Doctor Mappings**.

## 🚀 Features
- ✅ User registration & JWT login
- ✅ Patient management (CRUD)
- ✅ Doctor management (CRUD)
- ✅ Patient ↔ Doctor mapping (assign, retrieve, delete)
- ✅ JWT-protected APIs
- ✅ Admin panel support
````

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd healthcare

2. **Create virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```


4. **Create `.env` file** in the root folder and add:
   ```env
   SECRET_KEY=healthcare_secret
   DEBUG=True
   ALLOWED_HOSTS=127.0.0.1,localhost

   DB_NAME=healthcare_db
   DB_USER=postgres
   DB_PASSWORD=postgres
   DB_HOST=localhost
   DB_PORT=5432
   ```

5. **Apply migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser (admin)**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the server**

   ```bash
   python manage.py runserver
   ```

API will be available at:
👉 `http://127.0.0.1:8000/`

---

## 🔐 Authentication

This project uses **JWT Authentication**.

* **Obtain token**

  ```http
  POST /api/token/
  ```

  **Request:**

  ```json
  {
    "username": "rohit",
    "password": "mypassword"
  }
  ```

  **Response:**

  ```json
  {
    "refresh": "eyJhbGciOiJIUzI1NiIs...",
    "access": "eyJhbGciOiJIUzI1NiIs..."
  }
  ```

* **Use the token in headers**

  ```
  Authorization: Bearer <access_token>
  ```

---

## 📌 API Endpoints

### 1. Auth APIs

| Method | Endpoint              | Description          |
| ------ | --------------------- | -------------------- |
| POST   | `/api/auth/register/` | Register a new user  |
| POST   | `/api/auth/login/`    | Login user & get JWT |


#### 🔹 Register User

**Endpoint**

```http
POST /api/auth/register/
```

**Request**

```json
{
  "username": "rohit",
  "email": "rohit@example.com",
  "password": "mypassword"
}
```

**Response**

```json
{
  "id": 1,
  "username": "rohit",
  "email": "rohit@example.com"
}
```

---

#### 🔹 Login User (JWT)

**Endpoint**

```http
POST /api/auth/login/
```

**Request**

```json
{
  "username": "rohit",
  "password": "mypassword"
}
```

**Response**

```json
{
  "refresh": "eyJhbGciOiJIUzI1NiIs...",
  "access": "eyJhbGciOiJIUzI1NiIs..."
}
```

---

---

### 2. Patient APIs

| Method | Endpoint              | Description                         |
| ------ | --------------------- | ----------------------------------- |
| POST   | `/api/patients/`      | Add a new patient *(Auth required)* |
| GET    | `/api/patients/`      | Get all patients                    |
| GET    | `/api/patients/<id>/` | Get patient details                 |
| PUT    | `/api/patients/<id>/` | Update patient                      |
| DELETE | `/api/patients/<id>/` | Delete patient                      |

#### 🔹 Create Patient

**Endpoint**

```http
POST /api/patients/
```

**Request**

```json
{
  "age": 25,
  "contact_number": "9876543210",
  "medical_history": "Allergic to penicillin"
}
```

**Response**

```json
{
  "id": 1,
  "user": 2,
  "age": 25,
  "contact_number": "9876543210",
  "medical_history": "Allergic to penicillin"
}
```

---

#### 🔹 Get All Patients

**Endpoint**

```http
GET /api/patients/
```

**Response**

```json
[
  {
    "id": 1,
    "user": 2,
    "age": 25,
    "contact_number": "9876543210",
    "medical_history": "Allergic to penicillin"
  }
]
```

---

#### 🔹 Get Patient by ID

**Endpoint**

```http
GET /api/patients/1/
```

**Response**

```json
{
  "id": 1,
  "user": 2,
  "age": 25,
  "contact_number": "9876543210",
  "medical_history": "Allergic to penicillin"
}
```

---

#### 🔹 Update Patient

**Endpoint**

```http
PUT /api/patients/1/
```

**Request**

```json
{
  "age": 26,
  "contact_number": "9876543210",
  "medical_history": "No known allergies"
}
```

**Response**

```json
{
  "id": 1,
  "user": 2,
  "age": 26,
  "contact_number": "9876543210",
  "medical_history": "No known allergies"
}
```

---

#### 🔹 Delete Patient

**Endpoint**

```http
DELETE /api/patients/1/
```

**Response**

```
204 No Content
```

---

---

### 3. Doctor APIs

| Method | Endpoint             | Description                        |
| ------ | -------------------- | ---------------------------------- |
| POST   | `/api/doctors/`      | Add a new doctor *(Auth required)* |
| GET    | `/api/doctors/`      | Get all doctors                    |
| GET    | `/api/doctors/<id>/` | Get doctor details                 |
| PUT    | `/api/doctors/<id>/` | Update doctor                      |
| DELETE | `/api/doctors/<id>/` | Delete doctor                      |

#### 🔹 Create Doctor

**Endpoint**

```http
POST /api/doctors/
```

**Request**

```json
{
  "specialization": "Cardiologist",
  "years_of_experience": 10,
  "contact_number": "9999999999"
}
```

**Response**

```json
{
  "id": 2,
  "specialization": "Cardiologist",
  "years_of_experience": 10,
  "contact_number": "9999999999"
}
```

---

#### 🔹 Get All Doctors

**Endpoint**

```http
GET /api/doctors/
```

**Response**

```json
[
  {
    "id": 2,
    "specialization": "Cardiologist",
    "years_of_experience": 10,
    "contact_number": "9999999999"
  }
]
```

---

#### 🔹 Get Doctor by ID

**Endpoint**

```http
GET /api/doctors/2/
```

**Response**

```json
{
  "id": 2,
  "specialization": "Cardiologist",
  "years_of_experience": 10,
  "contact_number": "9999999999"
}
```

---

#### 🔹 Update Doctor

**Endpoint**

```http
PUT /api/doctors/2/
```

**Request**

```json
{
  "specialization": "Neurologist",
  "years_of_experience": 12,
  "contact_number": "9999999999"
}
```

**Response**

```json
{
  "id": 2,
  "specialization": "Neurologist",
  "years_of_experience": 12,
  "contact_number": "9999999999"
}
```

---

#### 🔹 Delete Doctor

**Endpoint**

```http
DELETE /api/doctors/2/
```

**Response**

```
204 No Content
```

---

```

---

### 4. Patient-Doctor Mappings APIs

| Method | Endpoint                      | Description                  |
| ------ | ----------------------------- | ---------------------------- |
| POST   | `/api/mappings/`              | Assign doctor to patient     |
| GET    | `/api/mappings/`              | Get all mappings             |
| GET    | `/api/mappings/<patient_id>/` | Get doctors of a patient     |
| DELETE | `/api/mappings/<id>/`         | Remove a doctor from patient |


#### 🔹 Assign Doctor to Patient

**Endpoint**

```http
POST /api/mappings/
```

**Request**

```json
{
  "patient": 1,
  "doctor": 2
}
```

**Response**

```json
{
  "id": 1,
  "patient": 1,
  "doctor": 2
}
```

---

#### 🔹 Get All Mappings

**Endpoint**

```http
GET /api/mappings/
```

**Response**

```json
[
  {
    "id": 1,
    "patient": 1,
    "doctor": 2
  }
]
```

---

#### 🔹 Get Doctors Assigned to Patient

**Endpoint**

```http
GET /api/mappings/1/
```

**Response**

```json
[
  {
    "id": 1,
    "patient": 1,
    "doctor": 2,
    "doctor_details": {
      "id": 2,
      "specialization": "Cardiologist",
      "years_of_experience": 10,
      "contact_number": "9999999999"
    }
  }
]
```

---

#### 🔹 Remove Mapping

**Endpoint**

```http
DELETE /api/mappings/1/
```

**Response**

```
204 No Content
```





---

## 📖 Example Workflow

1. Register → Login → Get JWT
2. Use JWT to create a Patient
3. Add Doctors
4. Map Patients ↔ Doctors
5. Retrieve mappings to see which doctor is assigned to which patient

---

## 👨‍⚕️ Author

* **Rohit Kumar**
  Healthcare API Assignment using Django Rest Framework
