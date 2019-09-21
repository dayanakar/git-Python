#Print 
print ("Hola Mundo en Python")
# -*- coding: utf-8 -*-


# Variables y string es mejor usarlas en minúsculas
mensaje ="Hola Mundo en Python"
print(mensaje)
#String
nombre="Dayana Pérez"
#Python es un lenguaje orientado a objetos
print(nombre.title())
#Python es lenguaje orientado a objeto se declara un objeto hay
# métodos preprogramadas nombre es de clase string y el método title se invoca
# a través del punto

#Imprimir mayuscula método upper
print(nombre.upper())
#imprimir minusculas método lower
print(nombre.lower())

nombre= "Dayana"
apellido="Pérez"
#concatenación entre string
nombre_apellido= nombre + " " + apellido
mensaje ="Hola" + " " + nombre_apellido.title() + "!"
print(mensaje)
# Python es sensible a mayusculas y minúsculas

# Cambio de linea \n 
print("Hola\n Dayana")
#Como eliminar espacios en blanco

lenguaje= "  python    "
lenguaje.rstrip()
lenguaje.lstrip()
lenguaje.strip()

#Números en python
"""Se usa signo = para asignar variables"""
# Números enteros
2+3
3-2
2*3
3/2
3**2
3**200
x=2

#No olvidar la precedencia
2+3*5
(2+3)*5

#Números reales
y=2.2
0.1+0.1
0.2+0.2
2*0.2
2*0.1

#Es más debil la tipificación de r que de python

#Este código da error porque es  un entero
edad=23
#mensaje="Feliz" +edad + "° aniversario!"
#print(mensaje)
# Se corrige con str(..) para convertir el entero en string
edad=23
mensaje="Feliz " +str(edad)+ " aniversario!"
print(mensaje)
# Usando la biblioteca math
import math as mt #Carga el paquete
# Para obtener PI=3.141592....
print(mt.pi)
x=3
y=9
print(mt.sqrt(x*x +y*y))
res= mt.pi*2**3-mt.sqrt(4)
print(res)
#Lista
#Las posiciones inician en 0 no en 1 lista [] vector ()
bicicletas=['trek','cannondale','redline','specialized']
mensaje="Mi bicicleta fue una "+ bicicletas[0].title() +"."
print(mensaje)
mensaje="Mi bicicleta fue una " +bicicletas[2].title() +"."
print(mensaje)
mensaje="Mi bicicleta fue una " +bicicletas[1].title() +"."
print(mensaje)
mensaje="Mi bicicleta fue una " +bicicletas[3].title() +"."
print(mensaje)

#Modificando la entrada de una lista
motocicleta=['honda','yamaha','suzuki']
print(motocicleta)
motocicleta[0]='ducati'
print(motocicleta)

#Agregando una entrada
motocicleta=['honda','yamaha','suzuki']
motocicleta.append('ducati')
print(motocicleta)

#La lista vacía
motocicleta=[]
motocicleta.append('honda')
motocicleta.append('yamaha')
motocicleta.append('suzuki')
print(motocicleta)
#insertando en una lista
motocicleta=['honda','yamaha','suzuki']
motocicleta.insert(0,'ducati')
print(motocicleta)

#Borrando elementos de la lista
motocicleta = ['honda','yamaha','suzuki']
print(motocicleta)
del motocicleta[0]
print(motocicleta)

motocicleta = ['honda','yamaha','suzuki']
print(motocicleta)
del motocicleta[1]
print(motocicleta)

 # Comando para eliminar el útimo elemento de
 # una lista
motocicleta = ['honda','yamaha','suzuki']
print(motocicleta)
popped_motocicleta=motocicleta.pop()
print(popped_motocicleta)
print(motocicleta)

motocicleta =['honda','ducati','yamaha','suzuki',]
muy_cara='ducati'
motocicleta.remove(muy_cara)
print(motocicleta)
print('\nUna '+ muy_cara.title()+ ' es una motocicleta muy cara')

#Ordenando una lista objeto.método(parámetros) crear data frame
carros=['bmw','audi','toyota','subaru']
carros.sort()
print(carros)

#carros.sort(reserve=True)
#print(carros)

#longitud de una lista
carro=['bmw','audi','toyota','subaru']
len(carro)

# Ciclos for

magos=['alice','david','carolina']
for m in magos:
    print(m)
    
magos=['alice','david','carolina']
for m in magos:  
    print(m.title() +', fue un gran mago!')
    # Python usa identación en lugar de llaves
    # el siguiente código da error
magos=['alice','david','carolina']
for m in magos: 
    print(m)
# un bloque de ejecución
magos=['alice','david','carolina']
i=0
for m in magos: 
    print(m)
    i=i+1
    print(i)
print('Esto está fuera del ciclo')
#Listas Numéricas
#Observe que termina en 4
for i in range (1,5):
    print(i)
#Observe que termina en 5
    #list hace lista dinámicas
for i in range (1,6):
    print(i)
    lista_numeros=list(range(1,6))
    print(lista_numeros)
    
# Lista de números pares suma 2 y va de 2 en 2
lista_pares=list(range(2,2000,2))
print(lista_pares)    
# Lista de números impares suma 2 y va de 2 en 2
lista_impares=list(range(1,11,2))
print(lista_impares)   
    
# Lista de números al cuadrado
lista_cuadrados=[]
for i in range(1,11):
    cuadrado=i**2
    lista_cuadrados.append(cuadrado)
print(lista_cuadrados)  

#estadísticas básicas en una lista 
digitos=[1,2,3,4,5,6,7,8,9,0]  
min(digitos)
max(digitos)
sum(digitos)
media=sum(digitos)/len(digitos)
print(media)
# Parte de una lista
jugadores=['charles','martina','michael','florence','eli']    
print(jugadores[0:3])  
print(jugadores[1:2]) 
print(jugadores[1:4])    
print(jugadores[:4])     
print(jugadores[3:])     
print(jugadores[-3:]) #Del útlimo de la lista 3 para atrás

jugadores=['charles','martina','michael','florence','eli']    
print('Los primeros tres jugadores son:')
for i in jugadores[:3]:
    print(i.title())
    
    #Copiando lista
    comidas=['pizza','falafel','carrot cake']
    comidas2=comidas[:]
    print('Mis comidas favoritas son:')
    print(comidas)
    print('\n Mis comidas favoritas son:')
    print(comidas2)
    
    
    
    
comidas=['pizza','falafel','carrot cake'] 
comidas2=comidas[:] #En este caso son la misma variable, mismo puntero
comidas.append('cannoli')
comidas2.append('ice cream')
print('Mis comidas favoritas son:')
print(comidas)
print('\n Mis comidas favorias son:')
print(comidas2)

comidas=['pizza','falafel','carrot cake'] 
comidas2=comidas#En este caso son la misma variable, mismo puntero
comidas.append('cannoli')
comidas2.append('ice cream')
print('Mis comidas favoritas son:')
print(comidas)
print('\n Mis comidas favorias son:')
print(comidas2)

# Listas que no cambian --> tuples, usa paréntesis () en lugar de []
datos=(200,50,4)
print(datos[0])
print(datos[1])
print(datos[2])
#Esta línea da error porque no se puede modificar una tupla
#datos[1]=90

#datos=(-3,5,9.7,8,-56.7)
#print(datos)
#Matrices como una lista de listas
#==========================================
matriz=[[4,1,-3],[2,4.4,0],[-5,9,198],[2,4,-5]]
print(matriz)

for j in range(3):
    for i in range(4):
        print(matriz[i][j])
        
len(matriz)
len(matriz[0])

for j in range(len(matriz[0])):
    for i in range(len(matriz)):
        print(matriz[i][j])

#Creando una matriz en forma interactiva n xn
n=5
M=[]
for i in range(n):
    F=[]
for j in range (n):
    F.append(0)
    M.append(F)
    print(M)                

#Creando una matriz en forma interactiva n x m
n=5
m=3
M=[]
for i in range(n):
    F=[]
for j in range (m):
    F.append(0)
    M.append(F)
    print(M)

# Otra forma de hacer lo mismo
n=5
M=[]
for i in range(n):
    M.append([0]*n) # Agrega el 0 n=5 veces
    print(M)
    
#Matriz identidad
n=5
M=[];
for i in range(n):
    F=[] 
for j in range(n):
    if i==j:
        F.append(1)
    else:
        F.append(0)
    M.append(F)
    print(M)
#import pandas as pd #Carga el paquete
import pandas as pd
import numpy as np # importando numpy
df=pd.read_csv('Advertising.csv',delimiter=';')

    
    
    
    
    
    
    