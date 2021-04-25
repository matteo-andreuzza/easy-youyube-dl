import tkinter as tk
import requests
import subprocess
import os
from random import *
from pickle import *
window = tk.Tk()
window.geometry("900x550")
window.title("cocnfigurazione di easy youtube-dl")
window.grid_columnconfigure(0, weight=1)

def config():
    print(text_input.get())
    percorso = text_input.get()
    print(percorso)
    f = open("records.dat", "wb")           # apre il file in scrittura ...
    dump(percorso, f)                       #carica il percorso
    f.close()
    text_response = "configurazioe completata! ora puoi chiudere il programma"
    textwidget = tk.Text()
    textwidget.insert(tk.END, text_response)
    textwidget.grid(row=3, column=0, sticky="WE", padx=10, pady=10)


text_response = 'ora eseguiremo la configurazione del programma. basta solamente che tu inserisca nel campo di testo qui sopra il percorso della cartella in cui vorrai salvare i video che scaricherai da youtube'
textwidget = tk.Text()
textwidget.insert(tk.END, text_response)
textwidget.grid(row=3, column=0, sticky="WE", padx=10, pady=10)
welcome_label = tk.Label(window,
                         text="ciao! benvenuto in easy youtube-dl!",
                         font=("Helvetica", 15))
welcome_label.grid(row=0, column=0, sticky="N", padx=20, pady=10)


text_input = tk.Entry()
text_input.grid(row=1, column=0, sticky="WE", padx=10)
download_button = tk.Button(text="configura", command=config)
download_button.grid(row=2, column=0, sticky="WE", pady=10, padx=10)


if __name__ == "__main__":
    window.mainloop()