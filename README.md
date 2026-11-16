Python program that connects to a PostgreSQL database and performs Create, Read, Update and Delete operations on a students table.

__Video__: Paste your video link here

## Requirements
- PostgreSQL with pgAdmin 4
- Python 3
- `psycopg2` library 

## Setup

### 1. Get the code

```bash
git clone https://github.com/sobbing333/Assignment3.git
cd Assignment3
```

### 2. Create the database and table
```bash
psql -d students_db -f database/create_table.sql
psql -d students_db -f database/insert_data.sql
```
> __NOTE__: The -h flag can be added to specify host and -U for the user. Alternatively, this can also be done from pgAdmin

### 3. Install psycopg2

```bash
pip install -r requirements.txt
```

### 4. Set your database password

Open `app/main.py` and configure the database conenction settings according to your setup

```python
DB_USER = "user"
DB_PASSWORD = "password"
DB_HOST = "host"
```

## Run

```bash
python3 app/main.py
```

> **Note**: Make sure your running from the root project directory

## Functions

__1. Show all students -> getAllStudents()__
Takes in no arguments and **READS** all students from db (ordering by student id)

__2. Add student -> addStudent(first_name, last_name, email, enrollment_date)__
Takes in students first name, last name, email and optionally enrollment date then **INSERTS** into db

__3. Update student email -> updateStudentEmail(student_id, new_email)__
Takes in students first name, last name, email and optionally enrollment date then **UPDATES** into db

__4. Delete student -> deleteStudent(student_id)__
Takes in student id then **DELETES** that student if they exist
