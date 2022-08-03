from tkinter import *
from PIL import Image, ImageTk

# Variables for common use.
bg_colour = "#425587"
url = ''
lgn = ''
pwd = ''
eml = ''

# Init app.
root = Tk()
root.title('KeyRoom')

# Load and resize logo1 and convert to TkImage.
logo1 = Image.open('assets/lock.png')
logo1 = logo1.resize((180, 180))
logo1 = ImageTk.PhotoImage(logo1)

# Create app body from 'frame'.
frame1 = Frame(root, width=700, height=215, bg=bg_colour)
frame1.grid(row=0, column=0, sticky='nesw')
frame1.grid_propagate(False)

# Create image widget (Logo).
logo1_lbl = Label(frame1, image=logo1, bg=bg_colour)
logo1_lbl.grid(row=0, rowspan=4, column=0)

# Creating test label and grid in frame1:
# URL section.
url_msg = StringVar()
url_msg.set(url)
url_lbl = Label(frame1, text='URL: ', bg=bg_colour, fg='white', font=('bold', 14))
url_lbl.grid(row=0, column=1,)
url_entry = Entry(frame1, textvariable=url_msg, fg='white', bg=bg_colour, bd=1, width=30, font=12)
url_entry.grid(row=0, column=2)

# LOGIN section.
lgn_msg = StringVar()
lgn_msg.set(lgn)
lgn_lbl = Label(frame1, text='LOGIN: ', bg=bg_colour, fg='white', font=('bold', 14))
lgn_lbl.grid(row=1, column=1)
lgn_entry = Entry(frame1, textvariable=lgn_msg, fg='white', bg=bg_colour, bd=1, width=30, font=12)
lgn_entry.grid(row=1, column=2)

# PASS section.
pwd_msg = StringVar()
pwd_msg.set(pwd)
pwd_lbl = Label(frame1, text='PASS: ', bg=bg_colour, fg='white', font=('bold', 14))
pwd_lbl.grid(row=2, column=1)
pwd_entry = Entry(frame1, textvariable=pwd_msg, fg='white', bg=bg_colour, bd=1, width=30, font=12)
pwd_entry.grid(row=2, column=2)

# EMAIL section.
eml_msg = StringVar()
eml_msg.set(eml)
eml_lbl = Label(frame1, text='EMAIL: ', bg=bg_colour, fg='white', font=('bold', 14))
eml_lbl.grid(row=3, column=1)
eml_entry = Entry(frame1, textvariable=eml_msg, fg='white', bg=bg_colour, bd=1, width=30, font=12)
eml_entry.grid(row=3, column=2)

# Only for console test.
print('Init: OK.')

root.mainloop()
