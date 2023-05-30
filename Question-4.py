# Q.4: Write a Python program input n numbers in tuple and count how
# many even and odd numbers are entered.

input_tup = eval(input("Enter a tuple of integers: "))

# Function to count the number of even and odd numbers in tuple
def even_odd_count(tup):
    even_count = 0
    odd_count = 0

    for i in tup:
        if i % 2 == 0:
            even_count += 1
        elif i % 2 != 0:
            odd_count += 1

    print("Even numbers in tuple:", even_count)
    print("Odd numbers in tuple:", odd_count)

# Function Calls
even_odd_count(input_tup)