from tkinter import *

bg_colour = "#3d6466"

# Init app.
root = Tk()
root.title('KeyRoom')


# Create app body from 'frame'.
frame1 = Frame(root, width=500, height=300, bg=bg_colour)
frame1.grid(row=0, column=0)
frame1.grid_propagate(False)

# Creating test label and grid in frame1 (maybe use pack()?).
lbl = Label(frame1, text='Welome PJ in your app.', bg=bg_colour, fg='white')
lbl.grid(row=0, column=0)
lbl1 = Label(frame1, text='Welome PJ in your app.', bg=bg_colour, fg='white')
lbl1.grid(row=1, column=1)


# Only for console test.
print('Project KeyRoom start.')

root.mainloop()
