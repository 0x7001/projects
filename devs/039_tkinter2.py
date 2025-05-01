#!/usr/bin/env python
from tkinter import *


def main():
    genislik = Pencere.winfo_screenwidth()
    yukseklik = Pencere.winfo_screenheight()
    px = 1336  # pencere yüksekliği
    py = 768  # # pencere genişliği
    w = int((genislik / 2) - (px / 2))
    h = int((yukseklik / 2) - (py / 2))
    ekran = "{}x{}+{}+{}".format(px, py, w, h)
    Pencere.geometry(ekran)
    Pencere.mainloop()


Pencere = Tk()
Pencere.title("Tkinter denemeleri...")
Pencere.resizable(False, False)


xbutton1 = Button(Pencere, width=5, height=1, text="Buton1")
xbutton1.place(x=10, y=10)

xbutton1 = Button(Pencere, width=5, height=1, text="Buton2")
xbutton1.place(x=80, y=10)

xbutton1 = Button(Pencere, width=5, height=1, text="Buton3")
xbutton1.place(x=150, y=10)

textbox = Text(Pencere, width=60, height=45)
textbox.place(x=10, y=50)
textbox.insert(INSERT, "Deneme tetx dğzenleme vs vs ")


if __name__ == "__main__":
    main()
