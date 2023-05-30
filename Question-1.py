# Q.1: Write a python program to search first occurrence of an element in
# a list by using Linear search and display frequency of each element
# present in list.

input_lst = eval(input("Enter a List: "))
search_ele = input("Enter the element to search: ")

# Searches for an element in list
def list_search(lst, search):
    ele_found = False
    for i in lst:
        if str(i) == search:
            ele_found = True
            print(f"{i} first occurred in list at index: {lst.index(i)}")
            break
    
    if ele_found == False:
        print("Element Not Found")

# Checks frequency of all elements in list
def list_freq_ele(lst):
    checked = []
    for i in lst:
        if i not in checked:
            print(f"Frequency of {i}: {lst.count(i)}")
            checked.append(i)

# Function Calls
list_search(input_lst, search_ele)
print()
list_freq_ele(input_lst)