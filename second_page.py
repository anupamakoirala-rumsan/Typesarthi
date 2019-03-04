from tkinter import *

import front_page

# import Tutor
# import game
# import keyboard_layout

import Test


def second():
    global seconds
    seconds = Frame(front_page.screen, width=400, height=250)
    seconds.pack(padx=20, pady=20)

    front_page.front.pack_forget()
    front_page.screen1.pack_forget()
    front_page.screen2.pack_forget()

    seconds.pack(padx=20, pady=20)
    l1 = Label(seconds, text='  Welcome to Typesarthi', font=('Arabic', 20))
    l1.pack()

    b1 = Button(seconds, text='Game', width=7, height=1,command=game_call)
    b1.pack(side=RIGHT, padx=10, pady=10, expand=False)

    b2 = Button(seconds, text='Tutor', width=7, height=1, command=call)
    b2.pack(side=RIGHT, padx=0, pady=10, expand=False)
    b2.bind('<Return>', lambda dummy=0: call(), add='+')

    b3 = Button(seconds,text='Test', width=7,height=1, command=testcall)
    b3.pack(side=RIGHT, padx=10, pady=10, expand=False)


def call():
    # Tutor.window()
    print('hlw')

def testcall():
    # keyboard_layout.test()
    Test.main()
def game_call():
    # game.main()
    print("hi")







