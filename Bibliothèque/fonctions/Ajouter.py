from json import dump, load
from datetime import date
from tkinter import Button, Tk, Label, Frame, Entry

background = open("config.vix", "r").read()
applis = load(open("appli.json", "r"))

def ajouter(reload):

    def AjouterCatalogue(nom, Chemain):
        Ajouter.destroy()
        if nom != "":
            applis[nom] = {}
            try:
                content = str(float(Chemain)) + " Go"
            except:
                content = "Non-valide"
            applis[nom]["utilisation"] = str(date.today())
            applis[nom]["poids"] = content
            applis[nom]["description"] = ""
            applis[nom]["favoris"] = False
            dump(applis, open("appli.json", "w"))
            reload()

    Ajouter = Tk()
    Ajouter.title("Ajouter une application")
    Ajouter.config(background=background)

    frame = Frame(Ajouter, bg=background)
    Label(frame, text="Nom :", bg=background).grid()
    Nom = Entry(frame)
    Nom.grid()
    frame.grid(pady=10)

    frame = Frame(Ajouter, bg=background)
    Label(frame, text="Poids (Go) :", bg=background).grid()
    Chemain = Entry(frame)
    Chemain.grid()
    frame.grid(pady=10)

    Button(Ajouter, text="Ajouter !", bg="orange", command=lambda: AjouterCatalogue(Nom.get(), Chemain.get())).grid()

    Ajouter.mainloop()