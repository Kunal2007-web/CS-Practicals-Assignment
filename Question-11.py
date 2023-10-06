# Q.11 Create a Binary File 'employee.dat' containing records of Employee ID,
# Employee name and Employee Salary. Update a record in the file.

# Imports Pickle Module
import pickle as p

# Adds New Records
def add_records():
    f = open('employee.dat', 'wb')
    n = int(input("Enter No. of Records: "))
    for i in range(n):
        print(f"Details of Employee {i+1}:")
        empid = int(input("Enter ID: "))
        name = input("Enter Name: ")
        salary = float(input("Enter Salary: "))
        print()

        data = [empid, name, salary]
        p.dump(data, f)
    print('Done.')
    f.close()

# Displays Records
def display_records():
    f = open('employee.dat', 'rb')
    try:
        while True:
            x = p.load(f)
            print(x)
    except EOFError:
        print("Complete Data Read Successfully.")
        print()
        f.close()

# Update a Record
def update_record():
    f = open('employee.dat', 'ab+')
    f.seek(0)
    empid = int(input("Enter ID of record to update: "))
    try:
        while True:
            x = f.tell()
            l = p.load(f)

            if l[0] == empid:
                f.seek(x)
                print("Found Record:")
                newid = int(input("Update ID: "))
                name = input("Update Name: ")
                salary = float(input("Update Salary: "))
                data = [newid, name, salary]
                p.dump(data, f)
                print("Record Updated.")
                f.close()
                break
    except EOFError:
        print("Error 404: Record Not Found")
        f.close()

# Function Calls
add_records()
display_records()

update_record()
display_records()