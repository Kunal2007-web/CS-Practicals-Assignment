# Q.5: Write a menu driven program in python to delete name of a
# student from dictionary and to search phone no of a student by
# student name. Create menu as below:
# ******MENU*******
# 1. Delete from Dictionary
# 2. Search Phone number using name from Dictionary
# 3. Exit

# Dictionary Creation and Inputs
student_dict = {}
n = int(input("Enter Number of Students: "))
for i in range(n):
    print(f"Enter Details of Student {i+1}:")
    name = input(f"Name of Student {i+1}: ")
    phone_no = int(input(f"Phone Number of Student {i+1}: "))
    student_dict[name.lower()] = phone_no
    print()

# Menu
while True:
    print("""******MENU*******
1. Delete From Dictionary
2. Search Phone Number using Name from Dictionary
3. Exit
""")
    option = input("Choose Action [1/2/3]: ")

    if option == "1":
        del_name = input("Which students details do you want to delete: ")
        print(f"Deleting {del_name.lower()} Details...")
        print(student_dict.pop(del_name.lower(), "Student Not Found! Try Again."))
        print()
    elif option == "2":
        search_name = input("Which students number do you want to search: ")
        print("Searching...")
        print(student_dict.get(search_name.lower(), "Student Not Found! Try Again."))
        print()
    elif option == "3":
        print("Exiting...")
        break
    else:
        print("Invalid Action! Please Enter Valid Action.")
        print()
