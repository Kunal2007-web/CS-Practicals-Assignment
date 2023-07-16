# Write a python program to create a binary file with roll number,
# name and marks. Input a roll number and update name and marks
import pickle as p

with open('stu-file.dat', 'wb') as f:
    n = int(input("Enter No. of Students to add: "))
    for i in range(n):
        print(f"Details of Student {i+1}:")
        roll = int(input("Enter Roll No.: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))
        print()
        data = [roll, name, marks]
        p.dump(data, f)
    print("Done.")

with open('stu-file.dat', 'rb+') as f:
    roll = int(input("Enter Roll No. to update: "))
    try:
        while True:
            d = p.load(f)
            t = f.tell()
            if d[0] == roll:
                name = input("Update Name: ")
                marks = float(input("Update Marks: "))
                data = [roll, name, marks]
                f.seek(t)
                p.dump(data, f)
                break
    except EOFError:
        print("Roll No. not found")
