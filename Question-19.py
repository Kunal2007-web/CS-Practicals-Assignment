# Write a Menu driven program in python to count 
# spaces, digits, words and lines from text file try.txt
f = open('try.txt', 'r')

while True:
    x = input("""Menu
1. Count Spaces              
2. Count Digits
3. Count Words
4. Count Lines              
5. Exit
              
Enter Option [1/2/3/4/5]: """)
    print()

    if x == "1":
        r = f.read()
        print("No. of Spaces:", r.count(" "))
        f.seek(0)
        print()
    elif x == "2":
        r = f.read()
        d_count = 0
        for i in r:
            if i.isdigit():
                d_count += 1
        print("No. of Digits:", d_count)
        f.seek(0)
        print()
    elif x == "3":
        r = f.read().split()
        print("No. of Words:", len(r))
        f.seek(0)
        print()
    elif x == "4":
        r = f.readlines()
        print("No. of Lines:", len(r))
        f.seek(0)
        print()
    elif x == "5":
        print("Exiting...")
        f.close()
        break
    else:
        print("Enter Valid Option")
        print()