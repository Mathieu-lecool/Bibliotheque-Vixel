from json import load, dump
from tkinter import *
from PIL import Image, ImageTk

background = open("config.vix", "r").read()
applis = load(open("appli.json", "r"))

def info(nom, reload):

    def SupprFavoris():
        try:
            applis[nom]["favoris"] = False
            dump(applis, open("appli.json", "w"))
            screen.destroy()
            reload()
        except:
             pass

    def Favoris():
        try:
            applis[nom]["favoris"] = True
            dump(applis, open("appli.json", "w"))
            screen.destroy()
            reload()
        except:
             pass
    
    def Sauvegarder():
        try:
            applis[nom]["description"] = desc.get()
            dump(applis, open("appli.json", "w"))
        except:
            pass

    try:
        screen = Tk()
        screen.title(f"Infos {nom}")
        screen.config(background=background)

        Label(screen, text="Description :", bg=background).grid()
        desc = Entry(screen)
        desc.grid()
        desc.insert(0, applis[nom]["description"])
        Button(screen, text="Sauvegarder", bg="orange", command=Sauvegarder).grid(pady=10, row=2)

        if applis[nom]["favoris"] == False:
            Button(screen, text="Ajouter aux favoris", bg="gold", command=Favoris).grid()
        else:
            Button(screen, text="Supprimer des favoris", bg="lightcoral", command=SupprFavoris).grid()
        screen.mainloop()
    except:
        pass