# Write a python program to create a binary file with name and roll number. 
# Search for a given roll number and display name,
# if not found display appropriate message.
import pickle as p

with open('stu-details.dat', 'wb') as f:
    n = int(input("Enter No. of Students to add: "))
    for i in range(n):
        print(f"Details of Student {i+1}:")
        roll = int(input("Enter Roll No.: "))
        name = input("Enter Name: ")
        print()
        data = [roll, name]
        p.dump(data, f)
    print("Done.")

with open('stu-details.dat', 'rb') as f:
    roll = int(input("Enter Roll No. to search: "))
    try:
        while True:
            l = p.load(f)
            if l[0] == roll:
                print("Found:", l[1])
                break
    except EOFError:
        print("Roll No. not found.")