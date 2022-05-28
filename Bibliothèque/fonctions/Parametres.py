import pickle, webbrowser
from os import remove
from tkinter import Button, Tk, Label, Frame, Entry

background = open("config.vix", "r").read()

def parametre(reload):

    def SupprCookie():
        remove("compte.bin")
        frame_parametre.destroy()
        reload()

    def AjCookie():
        pickle.dump("none none none", open("compte.bin", "wb+"))
        reload()

    def Sauvegarder():
        open("config.vix", "w").write(EntreeBg.get())
        frame_parametre.destroy()
        reload()

    frame_parametre = Tk()
    frame_parametre.title("Paramètres")
    frame_parametre.config(background=background)

    frame = Frame(frame_parametre, bg=background)
    Label(frame, text="Couleur de fond", bg=background).pack()
    EntreeBg = Entry(frame)
    EntreeBg.pack()
    Button(frame, text="Couleurs disponibles", bg="orange", command=lambda: webbrowser.open("https://askcodez.com/images3/156285517957003.png")).pack(pady=5)
    frame.pack(pady=10)

    frame = Frame(frame_parametre, bg=background)

    try:
        user = pickle.load(open("compte.bin", "rb"))
        Button(frame, text="Supprimer le cookie", bg="lightcoral", command=SupprCookie).pack(pady=5)
    except FileNotFoundError:
        Button(frame, text="Créer un cookie", bg="deepskyblue", command=AjCookie).pack(pady=5)
    
    frame.pack(pady=10)
    Button(frame_parametre, text="Sauvegarder", bg="yellow", command=Sauvegarder).pack()
    frame_parametre.mainloop()