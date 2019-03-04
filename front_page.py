import tkinter as tk

from tkinter import ttk

import os

import second_page


# Function to create the user file and store their details

def write():
    username_info = username.get()
    password_info = password.get()

    list_of_file = os.listdir()
    if username_info in list_of_file:
        tk.Label(screen1, text='Sorry!! Username already exist', fg='red').pack()
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

    else:
        # To open the user's file and store their  detail
        file = open(username_info, 'w')
        file.write(username_info + "\n")
        file.write(password_info)
        file.close()

# Delete the text written in the entry box
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        second_page.second()


# Function to check the login details
def check():
    username1 = username_verify.get()
    password1 = password_verify.get()

# list the created user's file

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            second_page.second()
        else:
            tk.Label(screen2, text='Invalid password!!').pack()
            password_entry1.delete(0, tk.END)

    else:
        tk.Label(screen2, text='Invalid username!!!').pack()
        username_entry1.delete(0, tk.END)
        password_entry1.delete(0, tk.END)


def login():
    front.pack_forget()
    screen1.pack_forget()
    screen2.pack(padx=20, pady=20)

    global username_verify
    global password_verify
    global username_entry1
    global password_entry1

    username_verify = tk.StringVar()
    password_verify = tk.StringVar()

    tk.Label(screen2, text='UserName*').pack()
    username_entry1 = tk.Entry(screen2, textvariable=username_verify)
    username_entry1.pack()

    tk.Label(screen2, text='Password*').pack()
    password_entry1 = tk.Entry(screen2, textvariable=password_verify, show='*')
    password_entry1.pack()

    b = tk.Button(screen2, text="LOGIN", command=check)
    b.pack()
    b.bind('<Return>', lambda dummy=0: check(), add='+')


def signup():

    front.pack_forget()
    screen2.pack_forget()
    screen1.pack()

    global username
    global password
    global username_entry
    global password_entry

    username = tk.StringVar()
    password = tk.StringVar()

    tk.Label(screen1, text="UserName:").pack()
    username_entry = tk.Entry(screen1, textvariable=username)
    username_entry.pack()
    tk.Label(screen1, text="Password:").pack()

    password_entry = tk.Entry(screen1, textvariable=password, show='*')
    password_entry.pack()
    '''if len(password.get()) < 5:
        Label(screen1,text='Must contain at least 6 letters', fg='red').grid()'''
    b3 = tk.Button(screen1, text="SIGNUP", command=write)
    b3.pack(expand=tk.YES)
    b3.bind('<Return>', lambda dummy=0: write(), add='+')


def mainscreen():

    front.pack()

    tk.Label(front, text='Typesarthi', font=('Arial',20)).pack(padx=0, pady=0)
    b1 = tk.Button(front, text='LOGIN', width=20, height=1, command=login)
    b1.pack(padx=0, pady=0, expand=True)

    b1.bind('<Return>', lambda dummy=0: login())

    b2 = tk.Button(front, text='SIGNUP', width=20, height=1, command=signup)
    b2.pack(side=tk.LEFT)
    # Event handling user can hit enter button when signup button is focused instead of mouse click
    b2.bind('<Return>', lambda dummy=0: signup(), add='+')


screen = tk.Tk()
screen.geometry("2000x1000")
screen.title('Typesarthi')
screen.configure(background='silver')

front = tk.Frame(screen, width=400, height=250)
screen1 = tk.Frame(screen, width=400, height=250 )
screen2 = tk.Frame(screen, width=400,height=250 )

s = ttk.Style()
s.theme_use('classic')

mainscreen()
screen.mainloop()

