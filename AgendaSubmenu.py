import os
import time
import json
import pickle

contactos = {}
contactos_copia={}


with open("My_copy.pkl","rb") as lf:
    recovery_dict=pickle.load(lf)
    os.system("cls")   

with open("My_contacts.pkl","rb") as tf:
    agenda_dict=pickle.load(tf)
    os.system("cls")

for nombre,numero in sorted(recovery_dict.items()):
     contactos_copia[(nombre)]=numero
     print(nombre,numero)
     print("incorporando copia de seguridad .............")
     os.system("cls")


print(f"Total de contactos en copia de seguridad {len (recovery_dict.items())}")

for nombre,numero in sorted(agenda_dict.items()):
     contactos[(nombre)]=numero
     print(nombre,numero)
     print("leyendo contactos en agenda ........")
     os.system("cls")
    
print(f"                 Total de contactos agendados {len (agenda_dict.items())}")
time.sleep(4)

if len (agenda_dict.items()) == 0:
      print("                      Agenda empty ")
      time.sleep(3)

  
def agenda(ing):
 
 if ing=="8":
  print("Esta a punto de salir del sistema")
 elif ing=="4":
  get_value(ing)
 elif ing=="2":
  contactosC(ing)
 elif ing=="1":
  ingresos(ing) 
 elif ing=="5":
  modificar(ing)
 elif ing=="3":
  consultar(ing)
 elif ing=="6":
  eliminar(ing)
 elif ing=="7":
  opc_advanced(ing)

#Inicio Submenu
def opc_advanced(dato):
    if dato=="7":
       while True:
          print("""                  1)Count Contact
                  2)List Contact
                  3)Reset Agenda 
                  4)Data recovery
                  5)Security copy
              """)
          opt=int(input("Ingrese una opcion para ingresar al menu avanzado: "))
          
          match opt:
             case 1:#Count Contactos
                for nombre,numero in  contactos.items():
                 print(f"La cantidad de contactos agendados es de: {len(contactos.items()) }")
                 time.sleep(4)
                 os.system("cls")
                 return
                
             case 2:#Lista Contactos
                print(sorted(contactos.items()))
                time.sleep(3)
                os.system("cls")
                return
             case 3: # Reset
                print("Esta a punto de resetear la agenda,todos los contactos se borraran¡¡¡")
                r=input("Digite 1 para continuar o 0 para salir: ")
                if r =="1":
                 for nombre,numero in contactos.copy().items():
                  contactos_copia[(nombre)]=numero
                 print("realizando copia de seguridad.......")
                 time.sleep(2)
                 contactos.clear()
                 print("                     Reset agenda completado")
                 time.sleep(4)
                 os.system("cls")
                 return
                else :
                 print("Reingresando al menu")
                 time.sleep(2)
                 os.system("cls")
                 return
             case 4:#Recovery
                 print(sorted(contactos_copia.items()))
                 for nombre,numero in sorted(contactos_copia.copy().items()):
                  contactos[(nombre)]=numero
                 print("Ingresando contactos......")
                 print(f"Copia de seguridad integrada con exito {len(contactos_copia.copy().items())} contactos")
                 contactos_copia.clear()
                 time.sleep(2)
                 os.system("cls")
                 return 
             case 5:#Copy
                print(sorted(contactos_copia.items()))
                time.sleep(3)
                os.system("cls")
                return
                
# Fin Submenu              

#Funciones           
def contactosC(dato):
    
     if dato == "2":
      print(json.dumps(contactos, sort_keys=True, indent=4))
      time.sleep(5)
      os.system("cls")
      return 
    
def modificar(dato):

     if dato == "5":
         nombre=input("Ingrese el nombre: ").title()
         if nombre not in contactos:
          print("contacto inexistente")
          time.sleep(4)
          os.system("cls")
          return
         if nombre in contactos:
          numero=int(input("Ingrese el nuevo numero: "))
          contactos[nombre]=numero
          print(f"contacto {nombre} modificado,su numero es ahora: {numero}")
          time.sleep(4)
          os.system("cls")
          return

def consultar(dato):

     if dato == "3": 
         nombre=input("Ingrese Nombre: ").title()
         if nombre in contactos:
          print(f"El numero del contacto {nombre} es: {contactos[nombre]} ")
          time.sleep(4)
          os.system("cls")
          return 
         if nombre not in contactos:
          print(" contacto inexistente")
          time.sleep(3)
          os.system("cls")
          return
         
def get_value(dato):
    
     if dato =="4":
         a=int(input("Ingresre el numero: "))
         for clave, valor in contactos.copy().items():
          if a == valor:
           print(f"El numero: {valor} esta asociado al contacto: {clave} ")
           time.sleep(3) 
           os.system("cls")
           return 
     if a not in list(contactos.values()):
           print("El numero no esta asociado a ningun contacto")
           time.sleep(3) 
           os.system("cls")
           return
         
def eliminar(dato):
                       
     if dato == "6": 
         nombre = input("Ingrese el nombre: ").title()   
         if nombre not in contactos:
          print("contacto inexistente")
          time.sleep(4)
          os.system("cls")
          return
         if nombre in contactos:
          print(contactos.pop(nombre))
          print(f"El contacto {nombre} fue eliminado ")
          time.sleep(4)
          os.system("cls")
          return
         
def ingresos(dato):
    
     if dato == "1":
        nombre=validate_filled_spaces()
        if nombre in contactos:
            print("Contacto existente")
            time.sleep(4)
            os.system("cls")
            return 
 
        try:
            numero=validate_int()
            if numero <= 999999999 or  numero >= 10000000000:
             raise ValueError ("Debe ingresar diez digitos")
              
              
        except  ValueError as e :
            print(e)
            time.sleep(5) 
            os.system("cls")
            numero=int(input('Ingrese el Numero: '))

       
        if  numero not in contactos.values(): 
            contactos[(nombre)]=numero
            print("Contacto agregado")
            print (nombre,numero)
            time.sleep(5)
            os.system("cls"),
            return

        else:
            a=numero
            for nombre, numero in contactos.copy().items():
              if a==numero:
               print("El numero existe en la agenda")
               print(f"El numero: {numero} esta asociado al contacto: {nombre}")
               time.sleep(4)
               os.system("cls")

def validate_filled_spaces():
    while True:
        nombre=input("Ingrese el nombre: ").strip().title()
        if nombre:
            return nombre
        else:
            print("Ingrese un nombre sin dejar espacios") 

def validate_int():
   while True:
        numero=input("Ingrese el numero del contacto: ")
        try:
           numero = int(numero)
           return numero
        except ValueError:
           print ("La entrada es incorrecta: escribe un numero entero")

# Fin Funciones
while True: 
 os.system("cls")
 
 from datetime import datetime
 dt=datetime.now()
 print("{}:{}:{}".format(dt.hour, dt.minute, dt.second))
 print("{}/{}/{}".format(dt.day, dt.month, dt.year))
 
 print("Bienvenido a tu agenda")
 print("""         
       
    ♣  Opere segun el siguiente menu  ♣  
     
      1) Ingresar nuevos contactos
      2) Ver contactos encolumnados alfabeticamente
      3) Consultar un contacto
      4) Averiguar si un numero esta asociado a un contacto
      5) Modificar un contacto
      6) Eliminar contacto
      7) Advanced menu
      8) Salir
      """)
 

 with open("My_contacts.pkl","wb") as tf:
    pickle.dump(contactos, tf)

 with open("My_copy.pkl","wb") as lf:
    pickle.dump(contactos_copia,lf)

 
 open_menu=input("Digite una opcion: ")
 agenda(open_menu)
 
 a=input("Si desea continuar digite 1, sino digite 0 para salir: ")
 if a =="0":
  time.sleep(1)
  os.system("cls")
  print(  "                                        Agenda out of line  ☀  system off  ☀                              "                            ) 
  break
 
