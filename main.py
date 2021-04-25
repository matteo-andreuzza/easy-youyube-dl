import tkinter as tk
import requests
import subprocess
import os
from random import *
from pickle import *


window = tk.Tk()
window.geometry("900x550")
window.title("easy youtube-dl")
window.grid_columnconfigure(0, weight=1)

try:
    f = open("records.dat", "rb")     # apre il file "records.dat"
    percorso = load(f)                  # carica il record
    f.close()
except FileNotFoundError:
    record = 1000000000               # se il file non esiste inizializza come prima
    nome = ""

def scarica():
    print(percorso)
    os.chdir(percorso)
    alfa = subprocess.Popen("youtube-dl " + text_input.get(), shell=True, stdout=subprocess.PIPE ).stdout.read()
    print("fatto")
    text_response = 'file salvato nella posizione indicata!'
    textwidget = tk.Text()
    textwidget.insert(tk.END, text_response)
    textwidget.grid(row=3, column=0, sticky="WE", padx=10, pady=10)

    credits_label = tk.Label(window, text="ascii art by artii.herokuapp.com")
    credits_label.grid(row=4, column=0, sticky="S", pady=10)
welcome_label = tk.Label(window,
                         text="Welcome! Aggiungi una parola o una frase da scaricare:",
                         font=("Helvetica", 15))
welcome_label.grid(row=0, column=0, sticky="N", padx=20, pady=10)

text_input = tk.Entry()
text_input.grid(row=1, column=0, sticky="WE", padx=10)

download_button = tk.Button(text="DOWNLOAD", command=scarica)
download_button.grid(row=2, column=0, sticky="WE", pady=10, padx=10)


if __name__ == "__main__":
    window.mainloop()