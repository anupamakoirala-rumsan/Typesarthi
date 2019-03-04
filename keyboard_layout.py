
import tkinter as tk


import front_page

import second_page
import Test


def tutor():
    global screen3

    screen3 = tk.Frame(front_page.screen, width=400, height=50)
    screen3.pack(padx=20, pady=20)
    # second_page.seconds.pack_forget()
    screen3.focus_set()
    #screen3.pack(padx=20, pady=20)
    # main()
    keyboard()


def test():
    global screen3

    screen3 = tk.Frame(front_page.screen, width=400, height=50)
    screen3.pack(padx=20, pady=20)
    second_page.seconds.pack_forget()
    screen3.focus_set()
    #screen3.pack(padx=20, pady=20)
    # main()
    keyboard()

shift_check_bool = False

def shift_check(keyevent):
    global shift_check_bool
    if keyevent.keycode == 50 and shift_check_bool == False :
        shift()
        shift_check_bool = True

def shift_uncheck(keyevent):
    global shift_check_bool
    if keyevent.keycode == 50:
        keyboard()
        shift_check_bool = False


buttons = ['१', '२', '३', '४', '५', '६', '७', '८', '९', '॰','-', '=',
          'ट', 'ौ', 'े', 'र', 'त', 'य', 'ु', 'ि', 'ो', 'प', 'इ', 'ए',
          'BACK',
          'ा', 'स', 'द', 'उ', 'ग', 'ह', 'ज', 'क', 'ल', ';', 'ॐ',
          'SHIFT',
          'ष', 'ड', 'छ', 'व', 'ब', 'न', 'म', 'SPACE',
               ]

bottons=['१', '२', '३', '४', '५', '६', '७', '८', '९', '॰', '-','=',
         'ठ', 'ौ', ' ै', ' ृ', 'थ', 'ञ', ' ूू', 'ी', 'ओ', 'फ', 'ई','ऐ',
         'BACK',
         'आ', 'श', 'ध', 'ऊ', 'घ', 'अ', 'झ', 'ख', 'ळ', ':', 'ःः',
         'SHIFT',
         'ऋ', 'ढ', 'च', ' ँ', 'भ', 'ण', ' ं', 'ङ', 'SPACE',]


def shift():
    global b1

    varRow = 1
    varColumn = 0

    for botton    in bottons:

        # commands = lambda x=botton: key(x)

        if botton == 'SPACE' or botton == 'SHIFT' or botton == 'BACK':
            b1 = tk.Button(screen3, text=botton, width=10, padx=1, pady=1,bd=1,relief='raised',
                         )
            b1.grid(row=varRow, column=varColumn)
            # b1.bind('<KeyPress>',lambda e: commands())

        else:

            b2=tk.Button(screen3, text=botton, width=10, padx=1, pady=1, bg='WHITE', bd=1,
                         relief='raised')
            b2.grid(row=varRow, column=varColumn)
            # b2.screen3.bind('<KeyPress>',lambda e: commands(), add='+')


        varColumn += 1
        if varColumn > 11 and varRow == 1:
            varColumn = 0
            varRow += 1
        if varColumn > 12 and varRow == 2:
            varColumn = 0
            varRow += 1
        if varColumn > 11 and varRow == 3:
            varColumn = 0
            varRow += 1


def keyboard():
    varrow=1
    varcolumn=0

    for button in buttons:
        # command = lambda x=button: select(x)

        if button == 'SPACE' or button == 'SHIFT' or button == 'BACK':
            b3 = tk.Button(screen3, text=button, width=10, padx=1, pady=1, bg='GREY', bd=1, relief='raised',
                           activebackground='WHITE')
            b3.grid(row=varrow, column=varcolumn)
            # b3.screen3.bind('<KeyPress>', lambda e: command(), add='+')

        else:

            b4 = tk.Button(screen3, text=button, width=10, padx=1, pady=1,bg='GREY', bd=1, relief='raised',
                         activebackground='WHITE')
            b4.grid(row=varrow, column=varcolumn)
            # b4.screen3.bind('<KeyPress>',lambda e: command(), add='+')


        varcolumn += 1
        if varcolumn > 11 and varrow == 1:
            varcolumn = 0
            varrow += 1
        if varcolumn > 12 and varrow == 2:
            varcolumn = 0
            varrow += 1
        if varcolumn > 11 and varrow == 3:
            varcolumn = 0
            varrow += 1


# def main():
#     # tk.Label(screen3, text='   ').grid(row=0, columnspan=20)
#     global entry
#     # entry = tk.Entry(screen3, width=90)
#     # entry.grid(row=0, columnspan=20)


