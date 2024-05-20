
import pickle
import os
import time

with open("My_copy.pkl","rb") as lf:
    recovery_data=pickle.load(lf)
    os.system("cls")


    for nombre,numero in sorted(recovery_data.items()):
     
     print(nombre,numero)
     print("leyendo contactos........")
     time.sleep(3)
    
print(f"                Total de contactos en copia de seguridad {len (recovery_data.items())}")

if len (recovery_data.items()) == 0: 
      print("                            Copy empty ")