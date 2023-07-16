# Write a python program to read and display file content
# line by line with each word separated by #.
f = open('sep-file.txt', 'r')
r = f.readlines()

def sep_read():
    for i in r:
        for j in i.split():
            print(j, end="#")
        print()

sep_read()
f.close()