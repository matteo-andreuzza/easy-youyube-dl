import tkinter 
import requests
import os
from io import BytesIO
import time
import subprocess

finestra = tkinter.Tk()

menu = tkinter.Frame(finestra)
menu.grid(sticky=tkinter.N)
tkinter.Label(menu, 
              text="Enter").grid(row=0)
campo = tkinter.Entry(menu)
campo.grid(row=0, column=1)
tkinter.Button(menu, text="Enter").grid(row=1)