# Q.9: Write a python code using function to search an element in a list
# using Binary search method.

input_lst = eval(input("Enter a list of integers: "))
search_ele = int(input("Enter integer to search: "))

def lst_search(lst, search):
    high = len(lst) -1
    low = 0
    
    while high >= low:
        mid = (high + low)//2

        if lst[mid] < search:
            low = mid + 1
        elif lst[mid] > search:
            high = mid - 1
        else:
            return mid
    
    return -1


# Function Call
found_at = lst_search(input_lst, search_ele)
if found_at != -1:
    print(f"{search_ele} is present in the list at index: {found_at}")
else:
    print("Element Not Found!")
