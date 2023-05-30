# Q.2: Write a python program to sort elements of a list in ascending and
# descending order by using bubble sort. Write user defined function.

input_lst = eval(input("Enter a list of integers: "))

# Function to sort list in ascending order through bubble sort
def bubble_sort_asc(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

# Function to srt list in descending order through bubble sort
def bubble_sort_desc(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

# Function Calls
print("Original list:", input_lst)
bubble_sort_asc(input_lst)
print("Ascending order:", input_lst)
bubble_sort_desc(input_lst)
print("Descending order:", input_lst)