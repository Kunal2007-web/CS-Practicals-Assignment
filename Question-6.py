# Q.6: Write a menu driven program in python to do following
# MENU
# 1. Reverse String
# 2. Check Whether string is Palindrome
# 3. Make half string in Uppercase
# 4. Exit

main_str = input("Enter a String: ")

# Menu
while True:
    print("""MENU
    1. Reverse String
    2. Check Whether String is Palindrome
    3. Make Half String in Uppercase
    4. Exit
""")
    option = input("Enter Action to perform on String [1/2/3/4]: ")

    if option == "1":
        rev_str = main_str[::-1]
        print("Original String:", main_str)
        print("Reversed String:", rev_str)
        print()
    elif option == "2":
        if main_str == main_str[::-1]:
            print(f"{main_str} is a Palindrome.")
        else:
            print(f"{main_str} is not a Palindrome.")
        print()
    elif option == "3":
        half_option = input("Which half do you want to convert to uppercase [1/2]: ")
        if half_option == "1":
            upper_str = main_str[:len(main_str)//2].upper() + main_str[len(main_str)//2:]
            print("Original String:", main_str)
            print("Modified String:", upper_str)
        elif half_option == "2":
            upper_str = main_str[:len(main_str)//2] + main_str[len(main_str)//2:].upper()
            print("Original String:", main_str)
            print("Modified String:", upper_str)
        else:
            print("Invalid Option! Try Again.")
        print()
    elif option == "4":
        print("Exiting...")
        break
    else:
        print("Invalid Option! Try Again.")
        print()
