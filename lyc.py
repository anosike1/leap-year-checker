# this is LEAP YEAR CHECKER - designed to tell you if a year is leap year or not
# import tkinter
from tkinter import *

# define the window title
window = Tk()
window.title ("LEAP YEAR CHECKER")

# define the label
label1 = Label (text="Insert Year Here:")
label1.grid (column=0,row=1)
# this will be an empty label where it'll give the report
label2 = Label ()
label2.grid (column=1, row=3)

# define the entry where the user will insert the year to be checked
entry = Entry ()
entry.grid (column=1, row=1)

# create a fucntion called CHECK which assigns the user input to varaiable called x
def check():
    x = int(entry.get())
# if the year is not evenly divisible by 4, it is NOT a leap year
    if x%4==0:
        # if the year is divisble by 4 and NOT divisible by 100, it IS a leap year
        if x%100==0:
    # if the year is divisible by 4,100, and 400, it IS a leap year
            if x%400==0:
                y = "Leap Year!"
            else:
                y = "Not a Leap Year!"
        else:
            y = "Leap Year!"
    else:
        y = "Not a Leap Year!"
# The report will be stored in the 'y' variable
# anc the empty label will be configured with the text
    label2.config (text=y)

# create a button named CHECK which will call the check function when clicked
buttn = Button (text="CHECK",command=check)
buttn.grid (row=2, column=1)

# activate the program
mainloop()