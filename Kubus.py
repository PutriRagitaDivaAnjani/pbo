import tkinter as tk 
from tkinter import Frame, Label, Entry, Button, END, W

def hitung_luas():
    r = float(txtrusuk.get())

    L = 6 * r * r
    txtLuas.delete(0, END)
    txtLuas.insert(END,L)

def hitung_volume():
    r = float(txtrusuk.get())


    v = r * r* r
    
    txtvolume.delete(0,END)
    txtvolume.insert(END,v)

def hitung():
    hitung_luas()
    hitung_volume()

# Create tkinter object app = tk.Tk()
app = tk.Tk()

# Tambahkan judul
app.title("Menghitung Luas Permukaan dan Volume Kubus")

# windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Nama
nama = Label(frame, text="PUTRI RAGITA DIVA ANJANI")
nama.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Label Rusuk
rusuk = Label(frame, text="Rusuk")
rusuk.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Textbox Rusuk
txtrusuk = Entry(frame)
txtrusuk.grid(row=1, column=1)

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

# Output Textbox Keliling
txtvolume = Entry(frame)
txtvolume.grid(row=6, column=1, sticky=W, padx=5, pady=5)

app.mainloop()