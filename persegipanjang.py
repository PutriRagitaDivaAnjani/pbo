import tkinter as tk 
from tkinter import Frame, Label, Entry, Button, END, W

def hitung_luas():
    p = float(txtpanjang.get())
    l  = float(txtlebar.get())

    L = p * l

    txtLuas.delete(0, END)
    txtLuas.insert(END,L)

def hitung_keliling():
    p = float(txtpanjang.get())
    l = float(txtlebar.get())


    k = 2 * (p + l)
    
    txtkeliling.delete(0,END)
    txtkeliling.insert(END,k)

def hitung():
    hitung_luas()
    hitung_keliling()

# Create tkinter object app = tk.Tk()
app = tk.Tk()

# Tambahkan judul
app.title("Menghitung Luas Permukaan dan Keliling Persegi Panjang")

# windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Nama
nama = Label(frame, text="PUTRI RAGITA DIVA ANJANI")
nama.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Label Panjang
panjang = Label(frame, text="Panjang")
panjang.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Label Lebar
lebar = Label(frame, text="Lebar")
lebar.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Textbox Panjang
txtpanjang = Entry(frame)
txtpanjang.grid(row=1, column=1)

# Textbox Lebar
txtlebar = Entry(frame)
txtlebar.grid(row=3, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas = Label(frame, text="Luas Permukaan: ")
luas.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output label Keliling
keliling = Label(frame, text="Keliling: ")
keliling.grid(row=6, column=0, sticky=W, padx=5, pady=5)


# Output Textbox Luas
txtLuas = Entry(frame)
txtLuas.grid(row=5, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Keliling
txtkeliling = Entry(frame)
txtkeliling.grid(row=6, column=1, sticky=W, padx=5, pady=5)

app.mainloop()