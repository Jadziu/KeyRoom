from tkinter import *
from PIL import Image, ImageTk

# Variables for common use.
bg_colour = "#425587"
bg2_colour = "#384873"
bg3_colour = "#2f3c61"
url = ''
lgn = ''
pwd = ''
eml = ''
typ = ''
status_msg = 'Init: OK'


def read():
    global status_msg
    status_msg = 'Reading from database'
    print("Read button active")
    return status_msg


def clear():
    print("Clear button active")


def update():
    print("Update button active")


def write():
    print("Write button active")


def delete():
    print("Delete button active")


# Init app.
root = Tk()
root.title('KeyRoom')

# Load and resize logo1 and convert to TkImage.
logo1 = Image.open('assets/lock.png')
logo1 = logo1.resize((180, 180))
logo1 = ImageTk.PhotoImage(logo1)

# Create app body from 'frame'.
frame1 = Frame(root, width=720, height=225, bg=bg_colour)
frame1.grid(row=0, column=0, sticky='nesw')
frame1.grid_propagate(False)

# Create image widget (Logo).
logo1_lbl = Label(frame1, image=logo1, bg=bg_colour)
logo1_lbl.grid(row=0, rowspan=5, column=0)

# Creating labels and entry in frame1 grid:
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

# Type section (Only for making fifth row =)).
typ_msg = StringVar()
typ_msg.set(typ)
typ_lbl = Label(frame1, text='TYPE: ', bg=bg_colour, fg='white', font=('bold', 14))
typ_lbl.grid(row=4, column=1)
typ_entry = Entry(frame1, textvariable=typ_msg, fg='white', bg=bg_colour, bd=1, width=30, font=12)
typ_entry.grid(row=4, column=2)

# Creating buttons in frame1 grin:
# Read button.
read_bt = Button(frame1, text='Read', font=14, width=15, fg='white', bg=bg2_colour,
                 activebackground=bg3_colour, command=lambda: read())
read_bt.grid(row=0, column=3, padx=20)

# Clear button.
clear_bt = Button(frame1, text='Clear', font=14, width=15, fg='white', bg=bg2_colour,
                  activebackground=bg3_colour, command=lambda: clear())
clear_bt.grid(row=1, column=3, padx=20)

# Write button.
write_bt = Button(frame1, text='Write', font=14, width=15, fg='white', bg=bg2_colour,
                  activebackground=bg3_colour, command=lambda: write())
write_bt.grid(row=2, column=3, padx=20)

# Update button.
update_bt = Button(frame1, text='Update', font=14, width=15, fg='white', bg=bg2_colour,
                   activebackground=bg3_colour, command=lambda: update())
update_bt.grid(row=3, column=3, padx=20)

# Delete button.
delete_bt = Button(frame1, text='Delete', font=14, width=15, fg='white', bg=bg2_colour,
                   activebackground=bg3_colour, command=lambda: delete())
delete_bt.grid(row=4, column=3, padx=20)


# Creating status bar.
status_lbl = Label(frame1, text=status_msg, bd=1, fg='white', bg=bg_colour, relief=GROOVE, anchor='e')
status_lbl.grid(row=5, column=0, columnspan=4, sticky='we', pady=20)

# Only for console test.
print('Init: OK.')

root.mainloop()
