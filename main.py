#import:
import os
from io import BytesIO
import time
import subprocess
#print di versione:
print("easy youtube-dl versione 0.0.1")
while True:
    print("pronto")
    #scrittura URL
    print("")
    print("")
    URL = input("inserisci qui l'url del video di youtube:...")
    print("")
    name = input("ok, ora inserisci il nome del file in cui vuoi salvare il video:...")
    print("")
    estensione = input("inserisci ora il tipo di file in cui voui salvare il video (per l'elenco delle estensioni supportate digita 'types'):...")
    if estensione == 'types':
        print(".mp4")
        print(".avi")
    print("")
    print("inizializzazione procedura di conversione...")
    #comandi:
    os.chdir("C:/Users/matte/Desktop")
    alfa = subprocess.Popen("youtube-dl " + URL, shell=True, stdout=subprocess.PIPE ).stdout.read()
    print("fatto")