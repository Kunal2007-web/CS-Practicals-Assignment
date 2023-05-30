# Q.8: Write a Python program to remove duplicates from a list.

input_lst = eval(input("Enter a List: "))

# Function to remove duplicates
def rm_duplicates(lst):
    unique_lst = []

    for i in lst:
        if i not in unique_lst:
            unique_lst.append(i)

    print("List after removing duplicates:", unique_lst)

# Function Call
rm_duplicates(input_lst)