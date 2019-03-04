import tkinter as tk
import tkinter.font as tkfont
import front_page
# import second_page
import time

import keyboard_layout

inc = 0
start=0
stop=0
# global errmssg


def update_time(keyevent):
    global inc, start, stop
    if inc == 1:
        start = time.time()

    # elif inc == len(data):
    # elif inc == len(data):
    else:
        stop = time.time()
        s = ((len(data) / 5) / ((stop - start) / 60))
        # s = stop-start
        # # a=int(s)
        # a=s/len(data)
        time_label.config(text=s)

        # screen4.after(5, update_time())
        # # print(keyevent.keycode)
        # print(s)


def main():
    global errmssg
    global time_label
    global screen4
    global typ
    global t
    screen4 = tk.Frame(front_page.screen, width=40, height=50)
    screen4.pack()
    # second_page.seconds.pack_forget()
    # keyboard_layout.screen3.pack()
    # screen4.pack()

    customFont = tkfont.Font(family='preeti', size=17)
    vcmd = (screen4.register(validate_data), '%S')
    invcmd = (screen4.register(invalid_data), '%S')

    t = tk.Text(screen4, height=5, width=40, fg='BlUE')
    t.insert(0.0, data)
    t.config(state='disabled')
    t.pack()

    typ = tk.Entry(screen4, validate="key", validatecommand=vcmd, invalidcommand=invcmd, font=customFont)
    typ.pack()
    typ.focus_set()

    errmssg = tk.Label(screen4, text=" ")
    errmssg.pack()
    keyboard_layout.test()

    typ.bind('<KeyPress>', keyboard_layout.shift_check)
    typ.bind('<KeyRelease>', keyboard_layout.shift_uncheck)
    time_label=tk.Label(screen4, text='')
    time_label.pack()
    typ.bind('<KeyRelease>', update_time, add='+')


with open('text', 'r', encoding="utf-8") as file:
    data = file.read()
file.close()


def validate_data(S):
    global inc
    if data[inc] == S:
        errmssg.config(text=" ")
        inc += 1
        # update_time()
        return True
    else:
        return False


def invalid_data(S):
    errmssg.config(text='Please try again ', fg='red')



