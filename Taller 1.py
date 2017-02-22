#!/usr/bin/python
# -*- coding: utf-8 -*-

#Punto 1
def max(n1, n2):
    if n1 < n2:
        print n2
    elif n2 < n1:
        print n1
    else:
        print "Son iguales"

#Punto 2

def max_de_tres (n1, n2, n3):
    if n1 > n2 and n1 > n3:
        print n1
    elif n2 > n1 and n2 > n3:
        print n2
    elif n3 > n1 and n3 > n2:
        print n3
    else:
        print "Son iguales"

#punto 3

def largo_cadena (lista):
    cont = 0
    for i in lista:
        cont += 1
    return cont

#punto 4

def es_vocal (x):
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        return True
    elif x == "A" or x == "E" or x == "I" or x == "O" or x == "U":
        return True
    else:
        return False

#punto 5

def sum(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma


def multip(lista):
    multiplicacion = 1
    for i in lista:
        multiplicacion *= i
    return multiplicacion

#punto 6

def inversa (cadena):
    invertida = ""
    cont = len(cadena)
    indice = -1
    while cont >= 1:
        invertida += cadena[indice]
        indice = indice + (-1)
        cont -= 1
    return invertida

#punto 7

def inversa (cadena):
    invertida = ""
    cont = len(cadena)
    indice = -1
    while cont >= 1:
        invertida += cadena[indice]
        indice = indice + (-1)
        cont -= 1
    return invertida

def es_palindromo (cadena):
    palabra_invertida = inversa(cadena)
    indice = 0
    cont = 0
    for i in range (len(cadena)):
        if palabra_invertida[indice] == cadena[indice]:
            indice += 1
            cont += 1

    if cont == len(cadena):

        print "Es palindromo"
    else:
        print "No es palindromo"


#Punto 8

def superposicion (lista1, lista2):
    for i in lista1:
        for x in lista2:
            if i == x:
                return True
    return False

#Punto 9

def generar_n_caracteres (n, caracter):
    print n * caracter

#Punto 10

def procedimiento (lista):
    for i in lista:
        print i * "x"


#Punto 11

def cuantos_digitos(n):
    ind = 1
    while n > 9:
        n = n / 10
        ind = ind + 1
    print ind

# punto 12

def cuadrado(a):
    c=0
    b=0

    while c<10:
        a= c**2
        c+=4
        b+=a


    print(b)

#Punto 13

def serie():
    s =1
    while s<=10:
        n=1
        while n<=10:
            print n
            n+=1
        s+=1
serie()

#Punto 14

def tabla(a):

    for j in range(1,11):
        n=a*j
        print (str(a)+" * "+str(j)+" = "+str(n))

# Punto 15

def par_impar(n):
    ind=0
    a=n
    while n>0:
        r=n%10
        ind= ind+r
        n=n/10
    print ("la suma de los digitos del # " + str(a) +" es " + str(ind))
    if (ind%2==0):
        print ("la suma del # "+ str(a)+ " es par ")
    else:
        print ("la suma del # "+ str(a)+ " es impar ")

# Punto 16

def digitos(n):
    ind = 1
    while n >=10:
        n = n / 10
        ind = ind + 1

        if ind%2==0:
            print ind

# Punto 17

def mas_larga(lista):
    mas_larga =raw_input("Ingrese Palabra ")
    for i in lista:
        if len(lista) > len(mas_larga):
            mas_larga = lista
        elif len(lista) < len(mas_larga):
            mas_larga = mas_larga
        elif len(lista) == len(mas_larga):
            mas_larga="Son iguales"
    return mas_larga

#punto 18

def c_mayusculas (cadena):
    cont = 0
    for i in cadena:
        if i != i.lower():
            cont += 1
    print "La cadena tiene "+str(cont)+ " mayusculas "

#Punto 19

def aDecimal(numeroBin):
    numeroBin = str(numeroBin)
    decimal = 0
    exp = len (numeroBin) -1
    for i in numeroBin:
        decimal += (int(i) * 2**(exp))
        exp = exp - 1
    return decimal

#Punto 20

def es_bisiesto(a):
    print "Comprobacion de si un ano bisiesto o no"

    if a % 4 == 0 and (not(a % 100 == 0)):
        print "El ano "+ str(a)+ " es un ano bisiesto porque es multiplo de 4"
    elif a % 400 == 0:
        print "El ano "+ str(a)+ " es un ano bisiesto porque es multiplo de 400"
    else:
        print "El ano "+ str(a)+ " no es bisiesto"

while True:
    print """
Ejercicios Taller # 1:
1 - Funcion max() 2 Numeros
2 - Funcion max() 3 Numeros
3 - Funcion Longitud Cadena
4 - Funcion Reconoce Vocal
5 - Funcion Suma - Multiplicacion Cadena
6 - Funcion Inversion Cadena
7 - Funcion Palindromo Cadena
8 - Funcion Superposicion (Cadena Miembro en comun)
9 - Funcion Multiplicacion Caracter
10 - Funcion Imprimir Histrograma
11 - Funcion Cantidad Digitos 1-100000
12 - Funcion Suma Cuadrados de # separados 4 Posiciones
13 - Funcion Imprime 10 veces la serie de numeros de 1 a 10
14 - Funcion Tabla Multiplicar de un #
15 - Funcion Identifica si la suma de los digitos de un # es par o impar
16 - Funcion Digitos Pares de un #
17 - Funcion Toma Lista Palabras y Devuelve la mas Larga
18 - Funcion Contar letras Mayusculas en una Cadena
19 - Funcion # binarios a # Enteros
20 - Funcion Determina si un ano es bisiesto
21 - salir

Selecione la opcion que desea ejecutar
"""
    opcion = input(">")

    if opcion ==1:
            print ("Has pulsado la opcion 1 ")
            a = input("digite el primer numero:")
            b = input("digite el sehgundo numero:")
            max(a,b)

    elif opcion ==2:
            print ("Has pulsado la opcion 2 ")
            a = input("digite el Primer numero:")
            b = input("digite el Segundo numero:")
            c = input("digite el Tercer numero:")
            max_de_tres(a, b, c)
    elif opcion ==3:
            print ("Has pulsado la opcion 3 ")
            a = raw_input("digite una palabra :")
            print largo_cadena(a)
    elif opcion ==4:
            print ("Has pulsado la opcion 4 ")
            a = raw_input("digite una letra :")
            print es_vocal(a)
    elif opcion == 5:
            print ("Has pulsado la opcion 5 ")
            print sum([1,2,3,4])
            print multip([1,2,3,4])
    elif opcion == 6:
            print ("Has pulsado la opcion 6 ")
            a = raw_input("digite una palabra :")
            print inversa(a)
    elif opcion == 7:
            print ("Has pulsado la opcion 7 ")
            a = raw_input("digite una palabra :")
            es_palindromo(a)
    elif opcion == 8:
            print ("Has pulsado la opcion 8 ")
            a = raw_input("digite una palabra :")
            b = raw_input("digite una palabra :")
            print superposicion(a,b)
    elif opcion == 9:
            print ("Has pulsado la opcion 9 ")
            a = raw_input("digite un caracter especial :")
            b = input("digite un numero :")
            generar_n_caracteres(a, b)
    elif opcion == 10:
            print ("Has pulsado la opcion 10 ")
            procedimiento([4,9,7])
    elif opcion == 11:
            print ("Has pulsado la opcion 11 ")
            cuantos_digitos(100000)
    elif opcion == 12:
            print ("Has pulsado la opcion 12 ")
            b = input("digite un numero :")
            cuadrado(b)
    elif opcion == 13:
            print ("Has pulsado la opcion 13 ")
            serie()
    elif opcion == 14:
            print ("Has pulsado la opcion 14 ")
            m = int(input("Cual tabla de multiplica deseas conocer "))
            tabla(m)
    elif opcion == 15:
            print ("Has pulsado la opcion 15 ")
            m = input("Ingrese un numero ")
            par_impar(m)
    elif opcion == 16:
            print ("Has pulsado la opcion 16 ")
            m = int(input("Ingrese un numero "))
            digitos(m)
    elif opcion == 17:
            print ("Has pulsado la opcion 17 ")
            m = raw_input("Ingrese una Palabra ")
            print mas_larga(m)
    elif opcion == 18:
            print ("Has pulsado la opcion 18 ")
            m = raw_input("Ingrese una Palabra ")
            c_mayusculas(m)
    elif opcion == 19:
            print ("Has pulsado la opcion 19 ")
            m = raw_input("Ingrese un numero ")
            print aDecimal(m)
    elif opcion == 20:
            print ("Has pulsado la opcion 20 ")
            m = int(input("Ingrese un ano "))
            es_bisiesto(m)
    elif opcion ==21:
            print (exit())






