import logic

import tkinter
from tkinter import ttk
import functools

plosca, igralec = logic.pripravi_igro()
koncana = False

def pritisk_gumba(n):
    global igralec

    if koncana:
        global plosca, igralec
        plosca, igralec = logic.pripravi_igro()

        for g in gumbi:
            g["text"] = ""

        global koncana
        koncana = False

        zacetek_poteze()
        
        return
    
    i, j = n//3, n%3
    logic.naredi_potezo(plosca, (i, j), igralec)

    gumbi[n]["text"] = igralec

    if logic.konec_igre(plosca):
        zmagovalec = logic.konec_igre(plosca)
        if zmagovalec == "remi":
            igralec = "remi"
        koncaj()
    else:
        igralec = logic.zamenjaj_igralca(igralec)
        zacetek_poteze()


root = tkinter.Tk()
root.title("TicTacToe")
frame = ttk.Frame(root)
frame.pack(fill='both', expand=True)

s = ttk.Style()
s.configure("my.TButton", font=("Helvetica", 30))

s2 = ttk.Style()
s2.configure("my.TLabel", font=("Helvetica", 20))

gumbi = []
for i in range(9):
    gumbi.append(ttk.Button(frame, text="", style="my.TButton", command=functools.partial(pritisk_gumba, i)))


c = 0
for i in range(3):
    for j in range(3):
        gumbi[c].grid(row=i, column=j, sticky="nswe")
        c += 1

frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_columnconfigure(2, weight=1)
frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(1, weight=1)
frame.grid_rowconfigure(2, weight=1)
frame.grid_rowconfigure(3, weight=1)

msg_label = ttk.Label(frame, text="", style="my.TLabel")
msg_label.grid(row=3, column=0, rowspan=1, columnspan=3)


def zacetek_poteze():
    msg_label["text"] = "Na vrsti je igralec {}.".format(igralec)

    
def koncaj():
    if igralec == "remi":
        msg_label["text"] = "Izenačeno!"
    else:
        msg_label["text"] = "Igralec {} je zmagal!".format(igralec)
    global koncana
    koncana = True


root.geometry("300x400")
zacetek_poteze()
root.mainloop()
