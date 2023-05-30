# Q.10: Create an application using Tkinter to enter your personal details
# and marks in 5 subjects. Calculate the total marks & percentage and
# display it on clicking a button

# Imports TKinter and TTK
from tkinter import *
from tkinter import ttk

# Sets root window, changes theme, adds title and makes the window un-resizable
root = Tk()
ttk.Style().theme_use('default')
root.title("Percentage Calculator")
root.resizable(False, False)

# Creates Labeled Frame
frame = LabelFrame(root, text="Enter Your Marks")
frame.grid(row=0, column=0, rowspan=5, columnspan=6, ipadx=10, ipady=10, padx=5, pady=5)

# Creates Indicator Labels
Label(frame, text="Subjects", justify='center', padx=2, pady=2).grid(row=0, column=0)
Label(frame, text="Obtained", justify='center', padx=2, pady=2).grid(row=0, column=1)
Label(frame, text="Total", justify='center', padx=2, pady=2).grid(row=0, column=2)

# Physics Marks
phy_obtained = Entry(frame, relief='flat', width=25, justify='center')
phy_total = Entry(frame, relief='flat', width=25, justify='center')
Label(frame, text='Physics', justify='left', padx=2, pady=2).grid(row=1, column=0)
phy_obtained.grid(row=1, column=1, padx=2, pady=2)
phy_total.grid(row=1, column=2, padx=2, pady=2)

# Chemistry Marks
chem_obtained = Entry(frame, relief='flat', width=25, justify='center')
chem_total = Entry(frame, relief='flat', width=25, justify='center')
Label(frame, text='Chemistry', justify='left', padx=2, pady=2).grid(row=2, column=0)
chem_obtained.grid(row=2, column=1, padx=2, pady=2)
chem_total.grid(row=2, column=2, padx=2, pady=2)

# Maths Marks
maths_obtained = Entry(frame, relief='flat', width=25, justify='center')
maths_total = Entry(frame, relief='flat', width=25, justify='center')
Label(frame, text='Maths', justify='left', padx=2, pady=2).grid(row=3, column=0)
maths_obtained.grid(row=3, column=1, padx=2, pady=2)
maths_total.grid(row=3, column=2, padx=2, pady=2)

# English Marks
eng_obtained = Entry(frame, relief='flat', width=25, justify='center')
eng_total = Entry(frame, relief='flat', width=25, justify='center')
Label(frame, text='English', justify='left', padx=2, pady=2).grid(row=4, column=0)
eng_obtained.grid(row=4, column=1, padx=2, pady=2)
eng_total.grid(row=4, column=2, padx=2, pady=2)

# CS Marks
cs_obtained = Entry(frame, relief='flat', width=25, justify='center')
cs_total = Entry(frame, relief='flat', width=25, justify='center')
Label(frame, text='CS', justify='left', padx=2, pady=2).grid(row=5, column=0)
cs_obtained.grid(row=5, column=1, padx=2, pady=2)
cs_total.grid(row=5, column=2, padx=2, pady=2)

# Percentage Calculation
# Creates Error Frame
error_label = Label(frame, text="Please Enter Numbers in all Input Fields.", justify='center')

# Calculation Function
def calculate():
    obtained_lst = [phy_obtained, chem_obtained, maths_obtained, eng_obtained, cs_obtained]
    total_lst = [phy_total, chem_total, maths_total, eng_total, cs_total]
    obtained = 0
    total = 0
    no_error = True

    # Checks if all entries input are digits
    for i in obtained_lst:
        if i.get().isdigit():
            obtained += int(i.get())
        else:
            error_label.grid(row=6, column=1, columnspan=2, padx=10, pady=5)
            no_error = False
            break

    if no_error:
        for i in total_lst:
            if i.get().isdigit():
                total += int(i.get())
            else:
                error_label.grid(row=6, column=1, columnspan=2, padx=10, pady=5)
                no_error = False
                break

    # Creates new window showing result, only if there were no errors before
    if no_error:
        result_window = Toplevel(root)
        result_window.title("Results")
        result_window.resizable(False, False)
        percentage = (obtained/total)*100
        Label(result_window, text=f"You got {obtained} marks out of {total}").grid(row=0, column=0, padx=10, pady=10)
        Label(result_window, text=f"Your percentage is {percentage}%").grid(row=1, column=0, padx=10, pady=10)

# Creates Calculate Button
Button(frame, justify='center', text="Calculate", command=calculate ,padx=5, pady=5).grid(row=6, column=0)

root.mainloop()