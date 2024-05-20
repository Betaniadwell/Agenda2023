import pickle
import os
import time

with open("My_contacts.pkl","rb") as tf:
    agenda_dict=pickle.load(tf)
    os.system("cls")
    
    for nombre,numero in sorted(agenda_dict.items()):
     
     print(nombre,numero)
     print("leyendo contactos........")
     time.sleep(3)
    
print(f"                Total de contactos agendados {len (agenda_dict.items())}")

if len (agenda_dict.items()) == 0:
      print("                      Agenda empty ")











