import tkinter as tk 
from tkinter import Frame, Label, Entry, Button, END, W

def hitung_luas():
    psa = float(txtpanjang_sisi_alas.get())
    ts  = float(txttinggi_segitiga.get())
    la = float(txtluas_alas.get())
    tl = float(txttinggi_limas.get())
    
    L = 0.5 * psa * ts

    txtLuas.delete(0, END)
    txtLuas.insert(END,L)

def hitung_volume():
    la = float(txtluas_alas.get())
    tl = float(txttinggi_limas.get())
    psa = float(txtpanjang_sisi_alas.get())
    ts  = float(txttinggi_segitiga.get())


    v = (1/3) * la *tl
    
    txtvolume.delete(0,END)
    txtvolume.insert(END,v)

def hitung():
    hitung_luas()
    hitung_volume()

# Create tkinter object app = tk.Tk()
app = tk.Tk()

# Tambahkan judul
app.title("Menghitung Luas Permukaan dan Volume Limas Segitiga")

# windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Nama
nama = Label(frame, text="PUTRI RAGITA DIVA ANJANI")
nama.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Label Panjang_Sisi_Alas
sisi_alas = Label(frame, text="Panjang_Sisi_Alas")
sisi_alas.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Label Tinggi_Segitiga
tinggi_segitiga = Label(frame, text="Tinggi_Segitiga")
tinggi_segitiga.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Label Tinggi_Limas
tinggi_limas = Label(frame, text="Tinggi_Limas")
tinggi_limas.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Label Luas_Alas
luas_alas = Label(frame, text="Luas_Alas")
luas_alas.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Textbox Panjang_Sisi_Alas
txtpanjang_sisi_alas = Entry(frame)
txtpanjang_sisi_alas.grid(row=1, column=1)

# Textbox Tinggi_Segitiga
txttinggi_segitiga = Entry(frame)
txttinggi_segitiga.grid(row=2, column=1)

# Textbox Tinggi_Limas
txttinggi_limas = Entry(frame)
txttinggi_limas.grid(row=3, column=1)

# Textbox Luas_Alas
txtluas_alas = Entry(frame)
txtluas_alas.grid(row=4, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas = Label(frame, text="Luas Permukaan: ")
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