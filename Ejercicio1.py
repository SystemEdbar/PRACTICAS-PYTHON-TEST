def factorial(num):

    factorial = 1

    for i in range(1, num + 1):
        factorial = factorial * i
    return factorial

def ejer1():
    valor=float(input("INSERTE UN VALOR: "))
    if (valor%2)==0:
        print(valor, " es un numero PAR")
    else:
        print(valor, " es un numero IMPAR")

def ejer2():
    valor = float(input("INSERTE UN VALOR: "))
    valor2 = float(input("INSERTE OTRO VALOR: "))
    producto = valor*valor2
    print("El producto de los dos numeros es: ",producto)

def ejer3():
    valor = float(input("INSERTE UN VALOR: "))
    valor2 = float(input("INSERTE OTRO VALOR: "))
    if valor > valor2:
        print("El valor mayor es: ",valor)
        print("El valor menor es: ",valor2)
    elif valor < valor2:
        print("El valor mayor es: ",valor2)
        print("El valor menor es: ",valor)
    else:
        print("Ambos numeros son iguales: ", valor)

def ejer4():
    valor = float(input("INSERTE UN VALOR: "))
    valor2 = float(input("INSERTE OTRO VALOR: "))
    valor3 = float(input("INSERTE OTRO VALOR: "))
    if valor > valor2:
        if valor > valor3:
            if valor2 > valor3:
                print("El valor mayor es: ", valor)
                print("El valor medio es: ", valor2)
                print("El valor menor es: ", valor3)
            else:
                print("El valor mayor es: ", valor)
                print("El valor medio es: ", valor3)
                print("El valor menor es: ", valor2)
    if valor2 > valor:
        if valor2 > valor3:
            if valor > valor3:
                print("El valor mayor es: ", valor2)
                print("El valor medio es: ", valor)
                print("El valor menor es: ", valor3)
            else:
                print("El valor mayor es: ", valor2)
                print("El valor medio es: ", valor3)
                print("El valor menor es: ", valor)
    if valor3 > valor:
        if valor3 > valor2:
            if valor > valor2:
                print("El valor mayor es: ", valor3)
                print("El valor medio es: ", valor)
                print("El valor menor es: ", valor2)
            else:
                print("El valor mayor es: ", valor3)
                print("El valor medio es: ", valor2)
                print("El valor menor es: ", valor)
    if valor == valor2:
        if valor > valor3:
                print("El valor mayor es: ", valor)
                print("El valor menor es: ", valor3)
        else:
                print("El valor mayor es: ", valor3)
                print("El valor menor es: ", valor)
    if valor == valor3:
        if valor > valor3:
                print("El valor mayor es: ", valor)
                print("El valor menor es: ", valor2)
        else:
                print("El valor mayor es: ", valor2)
                print("El valor menor es: ", valor)
    if valor2 == valor3:
        if valor2 > valor:
                print("El valor mayor es: ", valor2)
                print("El valor menor es: ", valor)
        else:
                print("El valor mayor es: ", valor)
                print("El valor menor es: ", valor2)
    if valor == valor3 and valor3==valor2:
        print("Todos los valores son iguales: ", valor)

def ejer5():
    valor = int(input("INSERTE UN VALOR: "))
    for x in range(1,11):
        print(valor,"*",x,"=",x*valor)
        x+=1

def ejer6():
    print("Usted debe ingresar 30 valores")
    producto=1; suma=1
    for i in range(30):
        valor = float(input(" Ingrese un numero: "))
        producto *=valor
        suma +=valor
    print("El valor de su producto es:", producto)
    print("El valor de la suma es:", suma)

def ejer7():
    valor= str(input("INGRESE UN NUMERO"))
    suma=0
    while int(valor) >= 0:
        suma= float(suma) + float(valor)
        valor=str(input("INGRESE UN NUMERO O UN VALOR NEGATIVO PARA TERMINAR"))
    print("El resultado de las sumas es: ", suma)

def ejer8():
    primer = (input("INTRODUCE EL PRIMER NUMERO: "))
    segundo = (input("INTRODUCE EL SEGUNDO NUMERO: "))
    resultado = 0
    for i in range(0, int(segundo)):
        resultado = resultado + primer
    print(resultado)

def ejer9():
    primero = float(input("INTRODUCE EL DIVIDENDO NUMERO: "))
    segundo = float(input("INTRODUCE EL DIVISOR NUMERO: "))
    cociente=0
    resto=float(primero)

    while resto >= segundo:
        resto -= segundo
        cociente +=1
    print("El valor del cociente es:", cociente)
    print("El valor del resto es", resto)

def ejer10():
    valor= str(input("INGRESE UN NUMERO"))
    producto= str(input("INGRESE OTRO NUMERO"))
    while valor != "F" or valor != "f":
        producto= float(producto) * float(valor)
        valor=str(input("INGRESE UN NUMERO O F PARA SALIR"))
    print("El resultado del Producto es: ", producto)

def ejer11():
    lista= []
    mayor=0
    cont=int(input("Cuantos numeros desea digitar?"))
    for x in range(cont):
        valor=int(input("Digite un numero"))
        lista.append(valor)
    lista.append(0)
    for x in range(len(lista)-1):
        if lista[x] >= mayor:
            mayor=lista[x]
    print("El valor mayor ingresado es: ", mayor)

def ejer12():
    primero = int(input("INTRODUCE EL NUMERO QUE DESEA CONVERTIR: "))
    print(format(primero,"0b"))

def ejer13():
    suma=0
    x=2
    while x < 50:
        if (x%5)==0:
            suma += x
        x += 3
    print(suma)

def ejer14():
    valor = str(input("INGRESE UN NUMERO"))
    suma = str(input("INGRESE OTRO NUMERO"))
    x=1
    while valor != "F" and valor != "f":
        suma = float(suma) + float(valor)
        x += 1
        valor = str(input("INGRESE UN NUMERO O F PARA SALIR"))

    valor = float(suma)/x
    print("El resultado del Producto es: ", valor)

def ejer15():
    contador = 0
    a = 0
    b = 1
    c = 0
    N = int(input("INGRESE LA CANTIDAD QUE DESEA VER"))

    while contador < N:
        a = b
        b = c
        c = a + b
        print(c)
        contador = contador + 1

def ejer16():
    lista = []
    mayor = 0
    menor = 999999
    cont = 0
    while  cont==0 :
        valor = int(input("Digite un numero"))
        if (valor%2) == 0:
            lista.append(valor)
            cont = 0
        else:
            cont=1

    lista.append(0)
    lista2= lista
    if len(lista)>0 and len(lista2)>0:
        for x in range(len(lista) - 1):
            if lista[x] >= mayor:
                mayor = lista[x]
        for x in range(len(lista) - 1):
            if lista[x] <= menor:
                menor = lista2[x]
        print("El valor mayor ingresado es: ", mayor)
        print("El valor menor ingresado es: ", menor)

def ejer17():
    cant = int(input("Cuantas cantidades desea ingresar?"))
    cont=0
    total = 0
    while cont < cant:
        num1 = float(input("Ingrese un numero: "))
        cont = cont + 1
        if num1 % 2 == 0:
            total = total + num1
        else:
            total = total
    print("La suma de los pares es: ", total)

def ejer18():
    cant = int(input("Cuantas cantidades desea ingresar?"))
    lista=[]
    cont=0
    total = 0
    while cont < cant:
        num1 = int(input("Ingrese un numero: "))
        cont = cont + 1
        if num1 % 2 == 0:
            lista.append(num1)
    if cont <=10:
        print("La lista de los pares es: ", lista[0:cont])
    else:
        print("La lista de los pares es: ", lista[0:10])

def ejer19():
    cant = int(input("Cuantas cantidades desea ingresar?"))
    lista = []
    cont = 0
    cont2=0
    total = 0
    while cont < cant:
        num1 = int(input("Ingrese un numero: "))
        cont = cont + 1
        if num1 % 2 == 0:
            if cont <= 30:
                cont2 +=1
                lista.append(num1)
    lista.append(0)
    if cont2 <= 30:
        for x in range(cont2):
            total += lista[x]
        print("La suma de los pares es: ", total)
    else:
        for x in range(30):
            total += lista[x]
        print("La suma de los pares es: ", total)

def ejer20():
    num = int(input("Ingrese un numero: "))
    x=1
    factorial=1
    while x <= num:
        print(x)
        factorial = factorial*(x)
        x +=1
    print("El factorial de", num, "es:",factorial)

def ejer21():
    num = float(input("Ingrese un numero: "))
    x=1
    cont=0
    for x in range (1,int(num)+1):
        if (num % x ) == 0:
            cont += 1
    if cont == 2:
        print("El valor", num, "es primo")
    else:
        print("El valor", num, "no es primo")

def ejer22():
    lista= []
    total=0
    x=1
    for x in range(1,31):
        valor=float(input("Digite un numero"))
        lista.append(valor)
    lista.append(0)
    for x in range(1,31):
        cont=0
        for y in range(1, int(lista[x]) + 1):
            if (lista[x] % y) == 0:
                cont += 1
        if cont == 2:
            total= total+lista[x]
    print("La suma de los numeros primos es: ", total)

def ejer23():
    lista= []
    factlista=[]
    factorial=1
    total=0
    x=0
    y=1
    for x in range(1,6):
        valor=float(input("Digite un numero"))
        lista.append(valor)
    lista.append(0)
    for x in range(5):
        while y <= lista[x]:
            factorial = factorial*(y)
            y +=1
        factlista.append(factorial)
    for x in range(len(factlista)):
        total += factlista[x]
    print(total)

def ejer24():
    num1 = int(input("Entre mas grande el numero mas preciso es el valor de euler"))
    euler=1
    for i in range(1, num1):
            euler = euler+ 1/factorial(i)

    print("Numero de euler es: ", (euler))

def ejer25():
    numero = int(input("Ingrese el numero"))
    i= int(input("Ingrese I"))
    resultado = factorial(numero)/(factorial(i)*factorial(numero-i))
    print("EL resultado es: ", (resultado))

