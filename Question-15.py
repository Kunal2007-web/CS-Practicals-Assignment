# Write a python program to remove all the lines that contain
# the character ‘a’ in a file and write it to another file.
f = open('yes-a.txt', 'r')
f1 = open('no-a.txt', 'w')
r = f.readlines()

def remove_a(l):
    for i in l:
        if 'a' not in i:
            f1.write(i)

remove_a(r)
f.close()
f1.close()