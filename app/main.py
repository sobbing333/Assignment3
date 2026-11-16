import psycopg2


# Database connection settings
DB_NAME = "students_db"
DB_USER = ""
DB_PASSWORD = ""
DB_HOST = ""
DB_PORT = "5432"

def connect():
    # Connection to db
    connection = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
    )
    return connection

# READ all students
def getAllStudents():
    connection = connect()
    cur = connection.cursor()

    # show all records from students table
    try:
        cur.execute("SELECT * FROM students ORDER BY student_id;")

        rows = cur.fetchall()

        if len(rows) == 0:
            print("There are no students in the table.")
        else:
            print()
            print("ID | First Name | Last Name | Email | Enrolment Date")

            for row in rows:
                student_id, first_name, last_name, email, enrollment_date = row
                print(f"{student_id} | {first_name} | {last_name} | {email} | {enrollment_date}")
            print()
    except psycopg2.Error as error:
        print("Could not get students: ", error)

    cur.close()
    connection.close()


# CREATE a new student
def addStudent(first_name, last_name, email, enrollment_date):
    connection = connect()
    cur = connection.cursor()

    # Insert new student record into student table
    try:
        sql = "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);"
        values = (first_name, last_name, email, enrollment_date)
        cur.execute(sql, values)
        connection.commit()
        print()
        print("Student added")
        print()
    except psycopg2.Error as error:
        connection.rollback()
        print("Could not add student:", error)

    cur.close()
    connection.close()

# UPDATE a students email
def updateStudentEmail(student_id, new_email):
    connection = connect()
    cur = connection.cursor()
    print()
    # Update email of student with specefied student_id
    try:
        sql = "UPDATE students SET email = %s WHERE student_id = %s;"
        cur.execute(sql, (new_email, student_id))
        connection.commit()


        # Check how many orws changed
        if cur.rowcount == 0:
            print("Student not found with that id", student_id)
        else:
            print("Email updated")
    except psycopg2.Error as error:
        connection.rollback()
        print("Email not updated: ", error)
    print()

    cur.close()
    connection.close()


# DELETE a student
def deleteStudent(student_id):
    # Delete student with specefied student_id
    connection = connect()
    cur = connection.cursor()
    print()
    try:
        sql = "DELETE FROM students WHERE student_id = %s;"
        cur.execute(sql, (student_id,))
        connection.commit()

        if cur.rowcount == 0:
            print("No student found with id", student_id)
        else:
            print("Student deleted")
    except psycopg2.Error as error:
        connection.rollback()
        print("Could not delete student:", error)

    print()
    cur.close()
    connection.close()





def main():
    # Connect to db
    try:
        connection = connect()
        connection.close()
        print("Connected to the database")
    except psycopg2.Error as error:
        print("Could not connect to the database: ", error)
        return

    # Loop menu until user choses to exit
    while True:
        print("Student Database Menu")
        print("1. Show all students")
        print("2. Add student")
        print("3. Update student email")
        print("4. Delete student")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")


        if choice == "1":
            getAllStudents()

        elif choice == "2":
            # Get required input for addStudent function
            first_name = input("First name: ")
            last_name = input("Last name: ")
            email = input("Email: ")
            enrollment_date = input("Enrollment date (YYYY-MM-DD or leave blank): ")

            # Save no date as null
            if enrollment_date == "":
                enrollment_date = None
            addStudent(first_name, last_name, email, enrollment_date)

        elif choice == "3":
            # Get required input for updateStudentEmail function
            student_id = input("Student ID: ")
            new_email = input("New email: ")

            updateStudentEmail(student_id, new_email)

        elif choice == "4":
            # Get required input for deleteStudent Function
            student_id = input("Student ID to delete: ")
            deleteStudent(student_id)

        elif choice == "5":
            print("Exiting")
            break

        else:
            print("Invalid choice. Enter number from 1 to 5")

main()
