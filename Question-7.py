# Q.7: Write a program to read a list of n integers (positive as well as
# negative). Create two new lists, one having all positive numbers
# with sum and the other having all negative numbers with sum from
# the given list.

input_lst = eval(input("Enter a list of positive and negative integers: "))

# Function to create two separate lists of positive and negative integers with their sum
def positive_negative_sort(lst):
    positive_lst = []
    positive_sum = 0
    negative_lst = []
    negative_sum = 0

    for i in lst:
        if i > 0:
            positive_lst.append(i)
            positive_sum += i
        elif i < 0:
            negative_lst.append(i)
            negative_sum += i

    print("Original List:", input_lst)
    print("List of Positive Integers:", positive_lst)
    print("Sum of Positive Integers:", positive_sum)
    print("List of Negative Integers:", negative_lst)
    print("Sum of Negative Integers:", negative_sum)

# Function Call
positive_negative_sort(input_lst)
