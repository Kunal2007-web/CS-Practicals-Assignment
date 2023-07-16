# Write a python code that accepts a filename, and copies all lines 
# that do not start with a lowercase letter from the first file into the second.
filename = input("Enter Text File: ")
copy = open(filename, 'r')
paste = open('paste.txt', 'w')
copy_r = copy.readlines()

for i in copy_r:
    if i[0].islower():
        print('Copying:', i)
        paste.write(i)

copy.close()
paste.close()