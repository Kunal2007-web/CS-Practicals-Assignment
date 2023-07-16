# Write a menu driven python program to create a CSV file by entering 
# dept-id, name and city, read and search the record for given dept-id.
# MENU
# 1. Create csv
# 2. Search
# 3.Exit
import csv

def create_csv():
    with open('dept.csv', 'w') as f:
        n = int(input("Enter No. of Departments to add: "))
        w = csv.writer(f)
        for i in range(n):
            print(f"Details of Department {i+1}:")
            dept_id = int(input("Enter Department ID: "))
            name = input("Enter Dept Name: ")
            city = input("Enter City Name: ")
            print()
            data = [dept_id, name, city]
            w.writerow(data)
        print("Done.")

def search(dept_id):
    with open('dept.csv', 'r') as f:
        r = csv.reader(f)
        for i in r:
            if i[0] == dept_id:
                print('Found Record:', i)
                break
        else:
            print("Department Not Found.")

while True:
    x = input("""MENU
1. Create CSV
2. Search
3. Exit
            
Enter Option [1/2/3]: """)
    print()
    
    if x == "1":
        create_csv()
        print()
    elif x == "2":
        s = input("Enter Dept ID to search: ")
        search(s)
        print()
    elif x == "3":
        print("Exiting...")
        break
    else:
        print("Enter Valid Option")
        print()
