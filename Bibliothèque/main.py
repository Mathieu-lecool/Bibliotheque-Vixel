from email.mime import image
import pickle, webbrowser
from json import dump, load
from socket import socket
from time import sleep
from os import remove, getcwd
from subprocess import run
from datetime import date
from tkinter import Button, Tk, Label, Frame, Entry
from fonctions.Parametres import parametre
from fonctions.Ajouter import ajouter
from fonctions.Compte import compte
from fonctions.Informations import info

background = open("config.vix", "r").read()

applis = load(open("appli.json", "r"))
#pickle.dump("none none none", open("compte.bin", "wb"))
try:
    user = pickle.load(open("compte.bin", "rb"))
except FileNotFoundError:
    user = "none none none"

if user.split(" ")[2] == "oui":
    try:
        run(f"python {getcwd()}/updater/updater.py", shell=True)
        serveur = socket()
        serveur.connect(("192.168.1.101", 32001))
        serveur.listen()
        serveur.sendall(user)
        sleep(0.5)
        serveur.sendall(str(applis).encode())
        serveur.close()
    except:
        pass

def reload():
    app.destroy()
    run(f"python {__file__}", shell=True)

def supprimer():
    try:
        del applis[Bar.get()]
        dump(applis, open("appli.json", "w"))
        reload()
    except:
        pass

def jeJoue():
    try:
        applis[Bar.get()]["utilisation"] = str(date.today())
        dump(applis, open("appli.json", "w"))
        reload()
    except:
        pass

app = Tk()
app.title("Vixel")
app.config(background=background)
app.resizable(0, 1)
app.iconbitmap("Vixel.ico")

Bar = Entry(app)
Bar.grid(column=3, row=1)

frame = Frame(app, bg=background)
Button(frame, text="Je l'utilise", command=jeJoue, bg="orange").grid(column=3, row=2)
Button(frame, text="Inforamtions", command=lambda: info(Bar.get(), reload), bg="orange").grid(column=3, row=2)
Button(frame, text="Supprimer", command=supprimer, bg="lightcoral").grid(column=3, row=4, pady=5)
frame.grid(column=3, row=2)

Button(app, text="Ajouter une appli", bg="dodgerblue", command=lambda: ajouter(reload)).grid(column=0, row=1)

if user != "none none none":
    Label(app, text=f"Connecté avec :\n{user.split(' ')[0]}", bg="dodgerblue").grid(row=2)
else:
    Button(app, text="Se connecter", bg="dodgerblue", command=lambda: compte(reload)).grid(row=2)

Button(app, text="Paramètres", bg="dodgerblue", command=lambda: parametre(reload)).grid(column=0, row=3)

compteur_rangée = 0
compteur_collone = 1
row = 0
nb_frame = 0
nb_pixel = 0

for appli in applis:
    if (compteur_collone % 2) == 0:
        position = 2
    else:
        position = 1
    if (compteur_rangée % 2) == 0:
        row += 1
    couleur = "deepskyblue"
    if applis[appli]["favoris"] == True:
        couleur = "gold"
    frame = Frame(app, bg=couleur)
    Label(frame, bg=couleur, text=f"Nom: {appli}\nDernière utilistation: {applis[appli]['utilisation']}\nPoids: {str(applis[appli]['poids'])}").grid(row=2)
    frame.grid(row=row, column=position, padx=10, pady=10)
    compteur_collone += 1
    compteur_rangée += 1
    nb_frame += 1
    if not (nb_frame % 2) == 0:
        nb_pixel += 80

if nb_pixel < 190:
    nb_pixel = 190
    
app.geometry(f"785x{nb_pixel}")

app.mainloop()