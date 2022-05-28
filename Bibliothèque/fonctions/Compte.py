from tkinter import Button, Tk, Label, Frame, Entry
from pickle import dump

background = open("config.vix", "r").read()

def compte(reload):

    def créerCompte(pseudo, mdp):
        fenetre_compte.destroy()
        fic = open("compte.bin", "wb+")
        dump(f"{pseudo} {mdp} oui", fic)
        fic.close()
        reload()

    fenetre_compte = Tk()
    fenetre_compte.title("Créer un compte")
    fenetre_compte.config(background=background)

    frame_compte = Frame(fenetre_compte, bg=background)
    frame = Frame(frame_compte, bg=background)
    Label(frame, text="Nom d'utilisateur", bg=background).grid()
    NomDu = Entry(frame)
    NomDu.grid()
    frame.grid(pady=10)

    frame = Frame(frame_compte, bg=background)
    Label(frame, text="Mot de passe", bg=background).grid()
    mdp = Entry(frame, show="*")
    mdp.grid()
    Button(frame, text="Envoyer !", bg="orange", command=lambda: créerCompte(NomDu.get(), mdp.get())).grid(pady=10)
    frame.grid(pady=10)

    frame_compte.grid()
    fenetre_compte.mainloop()