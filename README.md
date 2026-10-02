# Student Management API

A simple RESTful Student Management API built with FastAPI to practice CRUD operations, data validation, filtering, and sorting.

**Features**

- Create and read students
- Read a student by ID (UUID-based)
- Update student information
- Delete a student
- Filter and sort students by major, GPA, and graduation date
- Automatic interactive API documentation (Swagger UI)
- Input validation using Pydantic

**Technologies**

- Python 3.13
- FastAPI
- Pydantic
- Uvicorn

# Installation

1. Clone the project:

   ```bash
   git clone https://github.com/nima82rasouli-wq/student-management-api.git

2. Move into the project directory:
```bash
   cd student-management-api

3. Create a virtual environment:
```bash
   python -m venv .venv

4. Activate the virtual environment:

Windows:
```bash
.venv\Scripts\activate

Linux / macOS:
```bash
source .venv/bin/activate

5. Install the dependencies:
```bash
pip install -r requirements.txt

6. Run the application:
```bash
uvicorn main:app --reload


API Documentation
Swagger UI

http://127.0.0.1:8000/docs

ReDoc

http://127.0.0.1:8000/redoc

# Purpose

This project was developed as part of my FastAPI learning journey to practice building RESTful APIs, working with Pydantic models, handling UUIDs, and implementing filtering and sorting logic.

# License

This project is licensed under the MIT License.
