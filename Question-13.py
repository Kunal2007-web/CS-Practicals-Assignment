# Write a python program read a text file and display 
# the number of vowels/consonants/uppercase/lowercase alphabets in the file.
f = open('alpha-file.txt', 'r')
r = f.read()

def alpha_count(s):
    vowel_lst = ['a', 'e', 'i', 'o', 'u']
    v_count = 0
    c_count = 0
    u_count = 0
    l_count = 0
    a_count = 0
    for i in s:
        if i.isalpha():
            a_count += 1
            if i.lower() in vowel_lst:
                v_count += 1
            else:
                c_count += 1
            if i.isupper():
                u_count += 1
            elif i.islower():
                l_count += 1
    
    print('Total No. of Alphabets:', a_count)
    print('No. of Vowels:', v_count)
    print('No. of Consonants:', c_count)
    print('No. of Uppercase Alphabets:', u_count)
    print('No. of Lowercase Alphabets:', l_count)

alpha_count(r)
f.close()