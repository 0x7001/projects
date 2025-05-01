#!/usr/bin/env python3
from Sayi2Metin import Cevir
from tkinter import Tk, Label, Entry, Button, END
from tkinter import messagebox


def main():
	genislik = Pencere.winfo_screenwidth()
	yukseklik = Pencere.winfo_screenheight()
	px = 880
	py = 150
	w = int((genislik / 2) - (px / 2))
	h = int((yukseklik / 2) - (py / 2))
	ekran = "{}x{}+{}+{}".format(px, py, w, h)
	Pencere.geometry(ekran)
	xinput.focus()
	Pencere.mainloop()
	

def hesapla():
	veri = str(xinput.get())
	sonuc = Cevir(veri)
	mesaj = sonuc.yaz
	if "," in mesaj:
		ayir = mesaj.split(",")
		tl = ayir[0]
		kr = ayir[1]
		yenimesaj = "{} ,{}.".format(tl, kr).replace("  ", " ")
	else:
		yenimesaj = "{}.".format(mesaj)
	xinput2.delete(0, END)
	xinput2.insert(0, yenimesaj)


def hakkinda():
	messagebox.showinfo("Bilgi", "Girilen Sayıyı Metine Çeviren Uygulama")


def sil():
	xinput.delete(0, END)
	xinput2.delete(0, END)


def destroy_me():
	msg = messagebox.askyesno("Çıkış", "Çıkmak İstiyor musunuz?")
	# print(msg)  # msg true ise yes değilse no
	if msg:
		Pencere.destroy()
	else:
		pass


Pencere = Tk()

Pencere.title("Sayı > Metin")
Pencere.resizable(False, False)
Pencere.protocol('WM_DELETE_WINDOW', destroy_me)

xlabel = Label(Pencere, text="Sayı Girişi		: ")
xlabel.place(x=10, y=10)

xlabel2 = Label(Pencere, text="Sonuç		: ")
xlabel2.place(x=10, y=40)

xlabel3 = Label(Pencere, text="Yazdırmak istediğiniz değeri girin ve enter ile sonucu alın, 9 hane çevirir ")
xlabel3.place(x=10, y=125)

xinput = Entry(Pencere, bd=1, width=90)
xinput.place(x=134, y=10)

xinput2 = Entry(Pencere, bd=1, width=90)
xinput2.place(x=134, y=40)

xbuton = Button(Pencere, text="Yazdır.", command=hesapla)
xbuton.bind_all("<KP_Enter>", lambda x: hesapla())
xbuton.bind_all("<Return>", lambda x: hesapla())
# bazı linux sistemlerde Return ve KP_Enter olarak ayrı ayrı kullanılıyor
xbuton.place(x=10, y=90)

xbuton2 = Button(Pencere, text="Sil.", command=sil)
xbuton2.bind_all("<Delete>", lambda x: sil())
xbuton2.place(x=84, y=90)

xbuton3 = Button(Pencere, text="Hakkında", command=hakkinda)
xbuton3.bind_all("<F1>", lambda x: hakkinda())
xbuton3.place(x=133, y=90)

xbuton4 = Button(Pencere, text="Çıkış", command=destroy_me)
xbuton4.bind_all("<Escape>", lambda x: destroy_me())
xbuton4.place(x=222, y=90)


if __name__ == "__main__":
	main()
