import tkinter.messagebox
import sqlite3
from tkinter import *
from PIL import Image, ImageTk
from os.path import exists


# Variables for common use.
bg_colour = "#425587"
bg2_colour = "#384873"
bg3_colour = "#2f3c61"
url, lgn, pwd, eml, typ = '', '', '', '', ''
status_msg = 'App init status: RUN'
database_name = 'keyroom.db'
file_exists = exists(database_name)


class Database:
    def __init__(self, database_name):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def create_table(self, sql: str):
        self.cursor.execute(sql)
        self.connection.commit()


def new_table():
    """Creating database and table with information for user"""
    global status_msg

    popup = tkinter.messagebox.showinfo('Informacja', 'Brak bazy danych, tworzę nową!')
    db = Database(database_name)

    db.create_table('''CREATE TABLE passes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    url TEXT,
                    lgn TEXT,
                    pwd TEXT,
                    eml TEXT,
                    typ TEXT)''')

    popup2 = tkinter.messagebox.showinfo('Informacja', 'Baza danych utworzona prawidłowo!')
    popup3 = tkinter.messagebox.showinfo('Instrukcja', '1. Aby dodać do bazy wpis wprowadź dane i naciśnij WRITE\n'
                                                       '2. Aby odczytać wpis, wprwadź URL lub SHORT i naciśnij READ\n'
                                                       '3. Aby usunąć wpis, wprowadź URL lub SHORT i nacisnij DELETE\n'
                                                       '4. Aby uak\n'
                                                       '5. Przycisk CLEAR wyczyści wszystkie pola.\n'
                                                       '6. Wpisz w URL "SHOW" aby zobaczyć wszystkie SHORT w DB')


def read():
    """Reading records from database and display in entry boxes"""
    global status_msg
    global url, lgn, pwd, eml, typ

    status_msg = 'Reading record from database ...  '
    url = url_entry.get()
    typ = typ_entry.get()
    db = Database(database_name)

    if url != '' and typ == '':

        if url == 'show':
            sql = "SELECT typ FROM passes"
            db.cursor.execute(sql)
            record = db.cursor.fetchall()
            popup4 = tkinter.messagebox.showinfo('Show shorts in DB:', ' '.join(map(str, record)))
            print(record)

        sql = "SELECT * FROM passes where url = ?"
        db.cursor.execute(sql, (url, ))
        record = db.cursor.fetchall()

        if not record:
            status_msg = 'Brak wpisów pod tym URL ...'

        for data in record:
            lgn_entry.insert(0, data[2])
            pwd_entry.insert(0, data[3])
            eml_entry.insert(0, data[4])
            typ_entry.insert(0, data[5])

    elif url == '' and typ != '':
        sql = "SELECT * FROM passes where typ = ?"
        db.cursor.execute(sql, (typ,))
        record = db.cursor.fetchall()

        if not record:
            status_msg = 'Brak wpisów pod tym SHORT ...'

        for data in record:
            url_entry.insert(0, data[1])
            lgn_entry.insert(0, data[2])
            pwd_entry.insert(0, data[3])
            eml_entry.insert(0, data[4])

    elif url != '' and typ != '':
        status_msg = 'Wpisz URL lub SHORT ...'

    else:
        status_msg = 'Nie wpisano URL ani SHORT ...'

    db.connection.close()
    status_update()


def clear():
    """Clearing all entry boxes"""
    global status_msg, url_entry, lgn_entry, pwd_entry, eml_entry, typ_entry
    url_entry.delete(0, "end")
    lgn_entry.delete(0, "end")
    pwd_entry.delete(0, "end")
    eml_entry.delete(0, "end")
    typ_entry.delete(0, "end")
    status_msg = 'Wipe entry boxes...  '
    status_update()


def update():
    global status_msg
    global url, lgn, pwd, eml, typ
    print("Update button active")
    status_msg = 'Updating record database...  '
    status_update()


def write():
    """Creating new record from form, inserting in table."""
    global status_msg
    global url, lgn, pwd, eml, typ
    sql = "INSERT INTO passes(url, lgn, pwd, eml, typ) VALUES (?,?,?,?,?)"
    data = (url_entry.get(), lgn_entry.get(), pwd_entry.get(), eml_entry.get(), typ_entry.get(),)

    # Check if form is not empty:
    if url_entry.get().strip() and lgn_entry.get().strip() and typ_entry.get().strip() != '':
        db = Database(database_name)
        db.cursor.execute(sql, data)
        db.connection.commit()
        db.connection.close()
        status_msg = 'Write record to database... '
        status_update()
        
    else:
        status_msg = 'No data to write in database... '
        status_update()


def delete():
    """Delete record from database"""
    global status_msg
    global url, lgn, pwd, eml, typ

    url = url_entry.get().strip()
    typ = typ_entry.get().strip()
    db = Database(database_name)

    # Check if URL or SHORT is entered:
    if url != '':
        sql = "DELETE from passes WHERE url = ?"
        db.cursor.execute(sql, (url,))
        status_msg = 'Deleting record in database... '

    elif typ != '':
        sql = "DELETE from passes WHERE typ = ?"
        db.cursor.execute(sql, (typ,))
        status_msg = 'Deleting record in database... '

    else:
        status_msg = 'Need URL or SHORT to delete record... '

    db.connection.commit()
    db.connection.close()
    status_update()


def status_update():
    status_lbl = Label(frame1, text=status_msg, bd=1, fg='white', bg=bg_colour, relief=GROOVE, anchor='e')
    status_lbl.grid(row=5, column=0, columnspan=4, pady=15, sticky='we')


# Init app.
root = Tk()
root.title('KeyRoom')

# Load and resize logo1 and convert to TkImage.
logo1 = Image.open('assets/lock.png')
logo1 = logo1.resize((180, 180))
logo1 = ImageTk.PhotoImage(logo1)

# Create app body from 'frame'.
frame1 = Frame(root, width=720, height=220, bg=bg_colour)
frame1.grid(row=0, column=0, columnspan=4, sticky='nesw')
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
typ_lbl = Label(frame1, text='SHORT: ', bg=bg_colour, fg='white', font=('bold', 14))
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
status_update()

# Check if DB existing.
if not file_exists:
    new_table()

# Only for console test.
print('Init: OK.')

root.mainloop()
