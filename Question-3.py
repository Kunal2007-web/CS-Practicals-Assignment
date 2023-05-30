# Q.3: Write a python program using function to pass list to a function
# and double the odd values and half even values of a list and
# display list element after changing.

input_lst = eval(input("Enter a list of integers: "))

# Function to double odd values and half even values
def list_manipulate(lst):
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            lst[i] //= 2
        elif lst[i] % 2 != 0:
            lst[i] *= 2

    print("Modified List:", lst)

# Function Call
print("Original List:", input_lst)
list_manipulate(input_lst)