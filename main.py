from tkinter import *

# Creating main window.
root = Tk()
root.title('KeyRoom')
root.geometry('500x300')

# Creating test label.
lbl = Label(root, text='Welome PJ in your app.')

# Place in window
lbl.grid(row=0, column=0)


# Only for console test.
print('Project KeyRoom start.')

root.mainloop()
