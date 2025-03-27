# Import necessary libraries
from tkinter import *
from tkinter import messagebox

# Setup Tkinter Window
root = TK()
root.geometry("200X 200")


# Function for displating Warning Message 
# This will be called once the button is clicked
# messagebox.showwarning("Window Name", "Text to be displayed")
def msg() :
    messagebox.showwarning("Alert", "Stop! Virus Found.")

# Adding Button Widget to Window button = Button(root, text="Scan for virus", command=msg) button.place(x=40, y=80) 

# Entering main event loop
root.mainloop()   