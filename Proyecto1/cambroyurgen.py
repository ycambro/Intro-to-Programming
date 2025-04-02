# Proyecto de Taller de Programación
import sys
sys.setrecursionlimit(1000000000)

def inicio(): #Se crea la funcion inicial, la que le da el inicio de all
    n, modo, M = map(int,input().split()) #Esta seria nuestra primer entrada donde n representa la cantidad de números, modo respresenta el modo a usar y M representa el número máximo
#Cabe aclarar que los datos los recibe todos en una sola linea separados por un espacio, ejemplo: 4 1 1000
#En las funciones de los modos n representa el número y fac representa los factores
#Otro dato, al retornarse o imprimirse n, es porque n es primo lo que lo vuelve su factor propio
#Adicionalmente, los print tienen ese formato para que no se impriman los factores en lineas separadas sino más bien en una misma lista separados por un espacio.

    def modo_1(n, fac=2): #Funcion del modo 1, fac empieza siendo 2
        if n == 1: #En caso de que n (aqui n respresenta el número dado, ejemplo 700) sea igual a 1 se retorna 1
            return 1
        if fac > n // 2: #Si el factor es mayor que la mitad de n, entonces se retorna n
            print(n)
            return n
        if n % fac == 0: #Pero, si n prod de fac es equivalente a 0, entonces se imprime el factor y se realiza la operación n//fac retornandola para continuar la recursión
            print(fac, end=" ")
            return modo_1(n // fac, fac)
        else: #En cualquier otro caso, se retorna la funcion pero se le suma 1 a fac
            return modo_1(n, fac + 1)

    def modo_2(n, fac=2): #Funcion del modo 2, fac empieza siendo 2
        if n == 1: #Si n == 1, entonces se imprime 1 y listo
            print(1)
        while n != 1: #Mientras n no sea 1, lo que se hace es:
            if fac > n//2: #Si fac es mayor que la mitad de n, entonces se imprime n y se rompe el ciclo (como se puede ver, es la misma funcion que modo_1 solo que iterativa)
                print(n)
                break
            if n % fac==0: #Si n prod de fac es = 0, entonces significa que fac es un factor de ese n, por lo tanto se imprime fac y se realiza la operacion n//fac lo que se guarda en n, tal y como funcionan los return
                print(fac, end=" ")
                n = n // fac
            else:
                fac+=1 #En cualquier otro caso, se suma 1 a fac y se guarda en si mismo
#modo_2 es casi igual a modo_1, la programe basandome completamente en los datos que nos brindaba el modo_1

    def modo_3(n, fac=3): #Función modo 3, fac empieza en 3
        if n == 1: #Si n es 1, entonces se retorna 1
            return 1
        if n % 2 == 0: #Si n prod de 2 es == 0, entonces se imprime el factor menos 1, porque menos 1? pues para que se imprima un 2 y no un 3, y se retorna n // 2 y el factor actual (cabe aclarar que esta parte de la funcion no esta en la funcion que nos dan, pero se necesita para cuando los factores son 2, puesto que si empezamos con el factor 3 pues... estariamos dejando el 2 por fuera algo que no se deberia de hacer)
            print(fac-1, end=" ")
            return modo_3(n // 2, fac)
        if fac**2 > n: #En caso de que fac * fac sea mayor que n, entonces se imprime y retorna n (cabe aclarar que ese retorno no afecta la respuesta en lo más mínimo, en sí lo uso porque esta en la funcion que nos dieron en el enunciado del proyecto y porque asi se da cierre a la recursividad)
            print(n)
            return n
        if n % fac == 0: #En caso de que n prod del factor sea igual a 0, entonces significaria que fac es factor de n y se imprimiria el factor, retornandose la funcion pero modificando n a n//fac
            print(fac, end=" ")
            return modo_3(n//fac, fac)
        else:
            return modo_3(n, fac+2) #En cualquier otro caso, se retorna la funcion sumandole 2 a fac, puesto que esta funcion va buscando los factores cada 2 números, este siendo el motivo por el cual nuestros factores inician en 3

    def modo_4(n, fac=3): #Funcion modo 4, fac empieza en 3
        if n == 1: #Si n == 1, entonces se imprime 1
            print(1)
        while n != 1: #En caso contrario, es decir, mientras n no sea 1, se hara lo siguiente:
            if n % 2 == 0: #Si n prod 2 es 0, entonces, se imprime fac-1 y n se convierte en n//2, para entender mejor esto, vease comentario de la linea 40.
                print(fac-1, end= " ")
                n = n // 2
            elif (fac ** 2) > n: #En otro caso, es decir si fac * fac es mayor que n, se imprime n y se rompe el while
                print(n)
                break
            elif n % fac == 0: #En otro caso, es decir si n prod fac es 0, entonces fac es factor de n, por lo que se imprime el factor y n se convierte en el resultado de n//fac
                print(fac, end= " ")
                n = n//fac
            else:
                fac += 2 #En cualquier otra situación, se le suman 2 a el factor, siguiendo el enunciado.
#Mismo asunto que el modo_2, se basa en el modo anterior, en este caso se basa del modo_3 pero usando iteracion.

#Para el modo 5, se necesitó más para poder hacerlo, lo primero que se necesita es crear la criba, por lo que la cree en una funcion separada con su debido nombre
    def cribaErastotenes(n): #Funcion criba de Erastótenes, donde n representa el número máximo que se nos da al inicio, es decir M
        lista_num = [] #Se crea una lista vacía la cual terminará teniendo todos los números en valores de True or False
        contador = 0 #Creamos esta variable contador, la cual será la encargada de darle a todos los números, un valor booleano, en este caso,
        while contador <= n: #Mientras contador sea menor o igual que n, a la lista_num se le añade un true y se aumenta el contador en 1, en si se añaden todos los números desde 0 hasta n
            lista_num.append(True)
            contador += 1
        lista_num[0] = False #El valor en la posicion 0 que se encuentre en la lista se le da valor de Falso, en este caso significa que 0 no es primo, lo cual es cierto
        lista_num[1] = False #El valor en la posicion 1 que se encuentre en la lista, tendrá valor Falso, significando que 1 no es primo
        n2 = 2 #Se crea una nueva variable llamada n2, con valor 2,
        while n2 <= n: #Mientras que n2 sea menor que n:
            if (lista_num[n2]): #Si hay valor en la posicion n2 de lista_num, entonces se crea una variable llamada j, donde j = n2 * n2
                j = n2 * n2
                while (j - 1 < n): #Mientras que j -1 sea menor a n, entonces el valor que este en la posicion j en la lista_num, se convertirá en Falso y a j se le sumarán 2:
                    lista_num[j] = False
                    j += n2
            n2 += 1 #En caso contrario del if que esta arriba, se le suma 1 a la variable n2
        return lista_num #Al final se retorna la lista de valores booleanos que representan a los primos, es decir, se retorna lista_num como respuesta

    def criba_aux(lista_num): #Se crea la funcion auxiliar que recibirá la lista de números en valores booleanos,  la idea de esta funcion es convertir la lista de valores booleanos en números normales pero eliminando los no primos
        primos = [] #Esta lista será donde guardaremos los primos
        for a in range(len(lista_num)): #Con esto hacemos el ciclo que irá recorriendo la lista en busca de los primos
            if lista_num[a] == True: #Si el valor que se encuentra en la posicion a de la lista es verdadero, quiere decir que es primo, por lo tanto:
                primos.append(a) #Esto se añadirá a la lista primos
        return primos #Al final se retorna la lista primo

    def modo_5(n, A): #Funcion modo 5, recibe el número y la criba de erastotenes
        if n == 1: #En caso de que n sea uno, se imprime uno y se retorna lo mismo (el return no afecta en nada a la impresión que se hace al final)
            print(1)
            return 1
        pos = 0 #Se crea una variable que se encargará de ser la posicion que se usará para revisar los factores
        cociente = None #Se crea una variable, en este caso cociente, la cual estará vacia y se usará para darle fin al while
        while cociente != 1: #Mientras el cociente no sea uno, pues esto significaría que ya se encontraron todos los factores
            fac = A[pos] #Este seria el factor primo, es decir el número primo de la criba, que se encuentra en la posicion "pos"
            if n % fac == 0: #Si n prod de fac es 0, entonces significaria que habriamos encontrado el primer factor por lo que se imprimiria y a n se le aplicaria una division entre fac, y el resultado tambien se le añade al cociente, es decir el cociente ahora sería n/fac
                print(fac, end=" ")
                n = cociente = n / fac
            if n % fac != 0: #En caso de que n prod fac no sea 0, entonces se le suma uno a posicion y se continua de esta forma
                pos += 1
                continue
        print()

#Los siguientes if, funcionan de la misma forma, a exepcion del 5 y el 6, lo que hacen es, dependiendo de el valor que se le da al modo
#Se crea un ciclo creado por un for, de i hasta el rango de n (n vendría siendo la cantidad de números a la que se le desea encontrar los factores primos)
#Dentro de ese for tendriamos la recepcion de el número, si el número es mayor que el límite establecido, es decir que M, entonces el programa imprimira la situación y se cerrara.
#Si no hay problema con el numero que se pone, entonces se llamará la función de el modo seleccionado con el número dado, esto se repite hasta que n, es decir la cantidad de números que se deseaba poner sea cumplido
    if modo == 1:
        for i in range(n):
            num = int(input())
            if num > M:
                print("El numero ingresado es mayor que el límite! Intentalo de nuevo!")
                exit()
            modo_1(num)

    if modo == 2:
        for i in range(n):
            num = int(input())
            if num > M:
                print("El numero ingresado es mayor que el límite! Intentado de nuevo!")
                exit()
            modo_2(num)

    if modo == 3:
        for i in range(n):
            num = int(input())
            if num > M:
                print("El numero ingresado es mayor que el límite! Intentalo de nuevo!")
                exit()
            modo_3(num)

    if modo == 4:
        for i in range(n):
            num = int(input())
            if num > M:
                print("El numero ingresado es mayor que el límite! Intentalo de nuevo!")
                exit()
            modo_4(num)

    if modo == 5: #Este if tiene un funcionamiento, un poco distinto a los 4 anteriores, si el modo seleccionado es 5:
        criba = criba_aux(cribaErastotenes(M)) #Se crea una variable llamada criba y esta sería la lista de números primos, es decir se haria la funcion criba_aux y cribaErastótenes
        for i in range(n): #Esta parte si sería lo mismo que los 4 anteriores, véase el comentario de la linea 113, 114 y 115
            num = int(input())
            if num > M:
                print("El numero ingresado es mayor que el límite! Intentalo de nuevo!")
                exit()
            modo_5(num, criba) #Otra diferencia sería que a la funcion de el modo, en este caso no solo se le da el numero, sinó que también se le da la criba, para que la funcion pueda trabajar de la forma programada y requerida
    if modo > 5: #Si el modo es mayor que 5, se imprime el problema y se cierra el programa.
        print("Por favor seleccione un modo entre 1 y 5!")
        exit()
inicio() #Aqui se hace el llamado de la funcion principal, es decir aqui se inicia, curiosamente, se inicia en el final jeje