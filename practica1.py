'''
#primer ejercicio en Python

numero =raw_input('Ingresa un numero:')

numero = int(numero)
suma = numero * 2

print suma'''

'''nombre = raw_input("Escribe tu nombre completo")

longitud = len(nombre)

if (longitud>12):
    print "Muy Largo"'''

# Piedra Papel o Tijeras

'''import random

aleatorio = random.randrange(1, 3)
computadora = ""
print("(1)Piedra")
print("(2)Papel")
print("(3)Tijeras")
opcion= int(input("Selecciona :"))

if opcion == 1:
   elusuarioelije ="Piedra"
elif opcion == 2:
    elusuarioelije ="Papel"
elif opcion == 3:
   elusuarioelije ="Tijeras"
print("Seleccionaste", elusuarioelije)

if aleatorio ==1:
    computadora ="Piedra"
elif aleatorio ==2:
    computadora ="Papel"
elif aleatorio ==3:
    computadora = "Tijeras"
print("Mr Roboto",computadora)

if computadora =="Piedra" and elusuarioelije == "Papel":
    print("YOU WIN")
elif computadora =="Papel" and elusuarioelije =="Tijeras":
    print ("YOU WIN")
elif computadora == "Tijeras" and elusuarioelije =="Piedra":
   print ("YOU WIN")

if computadora == "Piedra" and elusuarioelije =="Tijeras":
   print("YOU LOSE")
elif computadora == "Tijeras" and elusuarioelije =="Papel":
    print("YOU LOSE")
elif computadora == "Papel" and elusuarioelije =="Piedra":
    print ("YOU LOSE")

if computadora =="Piedra" and elusuarioelije == "Piedra":
    print ("EMPATE")
if computadora =="Papel" and elusuarioelije == "Papel":
    print ("EMPATE")
if computadora == "Tijeras" and elusuarioelije == "Tijeras":
    print ("EMPATE")'''

    #impresion del 1 al 100

'''for x in range(1,101):
    print x'''

#el uso del ELSE

'''x=50
if x>50:
    print ("Estas muy viejo")
else:
    print ("Estas joven") '''

#impresion del 1 al 100 forma2

'''for num in range (101):
    print num'''

    #Listas

'''lista=["A","E","I","4","false","27","5","33","end","hola","666","coco","gus"]

print lista[len(lista)-1]'''

#Slicing

'''saludo="Hola, amigo Bienvenido"
print saludo[len(saludo)-3]'''

#string formathing

'''nombre=raw_input("Como te llamas")

print "Hola, {}. Como te va?".format(nombre)
nombre = raw_input("Que edad tienes?")
print "Tienes{}".format(nombre)'''

#UPPER

'''hola ="ola k ase"
print hola .upper()'''

#Kata1
'''frase="How can mirrors be real if our eyes aren't real"
frase=frase.split(" ")
frase_lista=[]
for palabra in frase:
    buf=palabra[0].upper()+palabra[1:]
    frase_lista.append(buf)
frase=" ".join(frase_lista)
print frase'''

#Kata2
'''usuario=raw_input("Dime tu nombre :")
edad=int(raw_input("Escribte tu edad :"))
anio_actual=2017
nacimiento=anio_actual-edad
print int("Hola, {}.Cumpliras 100 anios en  {}".format(usuario) + str(nacimiento+100))'''

#kata3
'''num=int(raw_input("Dame un numero :"))
if num%2==0:
    print "Es par"
else:
    print "Es impar"'''

#Kata4
'''lista= [5,10,15,20,25]
lista_extremos =[lista[0], lista[len(lista)-1]]
lista_intermedios=lista[1:len(lista)-1]
print lista_intermedios, lista_extremos'''

#kata5 lineal search
'''lista= [5,10,15,20,25]
num = 33
is_true= False #flag
for x in lista:
    if num==x:
        print True
        is_true=True
if is_true==False:
    print False'''
#Kata5 Binary search

'''lista = range(1000)
def binarySearch (lista,x)
numero = raw_input("Selecciona un numero :")'''

#Diccionario
