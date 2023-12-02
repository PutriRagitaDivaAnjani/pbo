import tkinter as tk 
from tkinter import Frame, Label, Entry, Button, END, W

def hitung_luas():
    r = float(txtjari_jari.get())
    s  = float(txtsselimut.get())
    t = float(txttinggi.get())


    L = 2 * pi * r * t

    txtLuas.delete(0, END)
    txtLuas.insert(END,L)

def hitung_volume():
    r = float(txtjari_jari.get())
    s = float(txtselimut.get())
    t = float(txttinggi.get())


    v = pi * r ** t
    
    txtvolume.delete(0,END)
    txtvolume.insert(END,v)

def hitung():
    hitung_luas()
    hitung_volume()

# Create tkinter object app = tk.Tk()
app = tk.Tk()

# Tambahkan judul
app.title("Menghitung Luas Selimut dan Volume Tabung")

# windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Nama
nama = Label(frame, text="PUTRI RAGITA DIVA ANJANI")
nama.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Label Jari_jari
jari_jari = Label(frame, text="Jari_jari")
jari_jari.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Label Tinggi
tinggi = Label(frame, text="Tinggi")
tinggi.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Label Selimut
selimut = Label(frame, text="Luas Selimut")
selimut.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Textbox Jari_jari
txtjari_jari = Entry(frame)
txtjari_jari.grid(row=1, column=1)

# Textbox Tinggi
txttinggi = Entry(frame)
txttinggi.grid(row=2, column=1)

# Textbox Selimut
txtselimut = Entry(frame)
txtselimut.grid(row=3, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas = Label(frame, text="Luas Selimut: ")
luas.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output label Volume
volume = Label(frame, text="Volume: ")
volume.grid(row=6, column=0, sticky=W, padx=5, pady=5)


# Output Textbox Luas
txtLuas = Entry(frame)
txtLuas.grid(row=5, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtvolume = Entry(frame)
txtvolume.grid(row=6, column=1, sticky=W, padx=5, pady=5)

app.mainloop()