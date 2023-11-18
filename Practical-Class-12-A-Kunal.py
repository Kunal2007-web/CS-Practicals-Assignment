# Create a Menu-Driven Program which does CRUD operation on the database table Students(StudentID, Name, Course)
import mysql.connector as c
password = input("Enter Password to SQL server: ")
db = c.connect(host="localhost", username="root", passwd=password, database="KunalKumarPractical")
cursor = db.cursor()

# Create Database and Tables
# cursor.execute("SHOW DATABASES;")
# if ("KunalKumarPractical",) in cursor:
#     cursor.execute("CREATE DATABASE KunalKumarPractical;")
#     db.database = "KunalKumarPractical"
# cursor.execute("SHOW TABLES;")
# if ("Students",) in cursor:
#     cursor.execute("CREATE TABLE Students (StudentID INTEGER PRIMARY KEY, Name VARCHAR(50) NOT NULL, Course VARCHAR(50) NOT NULL);")


# CRUD Functions
def add_data():
    print("Adding Row to Table: Students")
    stu_id = int(input("Enter Student ID: "))
    name = input("Enter Student Name: ")
    course = input("Enter Student Course: ")

    query = "INSERT INTO Students VALUES({}, '{}', '{}')".format(stu_id, name, course)
    cursor.execute(query)
    db.commit()
    print("Added Row")


def update_data():
    print("Updating Row in Table: Students")
    stu_id = int(input("Enter Student ID to Update: "))

    to_update = input("""Choose Field to Update:
1. Name
2. Course
Choose [1/2]: """)
    
    if to_update == "1" or to_update.lower() == "name":
        name = input("Enter Updated Name: ")
        query = "UPDATE Students SET Name = '{}' WHERE StudentID = {} ;".format(name, stu_id)
        cursor.execute(query)
        print("Data Updated")
    elif to_update == "2" or to_update.lower() == "course":
        course = input("Enter Updated Course: ")
        query = "UPDATE Students SET Course = '{}' WHERE StudentID = {} ;".format(course, stu_id)
        cursor.execute(query)
        print("Data Updated")
    else:
        print("Choose Correct Option!")

    db.commit()
        
def delete_data():
    print("Deleting Row from Table: Students")
    stu_id = int(input("Enter StudentID to delete: "))

    query = "DELETE FROM Students WHERE StudentID = {} ;".format(stu_id)
    cursor.execute(query)
    db.commit()
    print("Row Deleted")

def read_data():
    print("Reading Data from Table: Students")
    cursor.execute("SELECT * FROM Students;")
    data = cursor.fetchall()
    print(f"Reading from {cursor.rowcount} rows.")
    print(data)

# Menu
while True:
    print("""Choose from the following operations:
1. Add New Row
2. Update Existing Row
3. Delete Existing Row
4. Read All Rows
5. Exit
""")
    choice = input("Choose [1/2/3/4/5]: ")
    print()

    if choice == "1":
        add_data()
        print()
    elif choice == "2":
        update_data()
        print()
    elif choice == "3":
        delete_data()
        print()
    elif choice == "4":
        read_data()
        print()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Please Enter Correct Option!")
        print()
