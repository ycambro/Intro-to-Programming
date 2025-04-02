#----Matrices-----------------------------------------------------------------------|

#Imprime cada una de las posiciones, de la
#matriz que detecta como resultado.
def IMPRIMIR_MATRIZ(matriz):
    for fila in matriz:
        print(*fila, sep="")
        #El (sep="") hace que la piezas se
        #impriman sin espacios entre ellas.


#Crea una matriz llena de "." según el
#largo y el ancho ingresados en INICIO.
def CREAR_MATRIZ_VACIA(largo, ancho):
   return [["."] * ancho for i in range(largo)]


#----Recorte de Piezas-----------------------------------------------------------|

#Determina que posiciones de la
#matriz 4x4 (en la que viene la pieza),
#pertenecen a la propia pieza y
#las guarda en una lista.
def COORDENADAS(pieza):
    cord = []
    for i in range(len(pieza)):
        for j in range(len(pieza[0])):
            if pieza[i][j] != ".":
                cord.append([i, j])

    return cord


#Determina en cual columna inicia y
#en cual columna termina la pieza
#ocupa la pieza dentro su matriz 4x4.
def LARGO(entrada):
    cord = COORDENADAS(entrada)

    der = 0 #Máx. cant. de
    izq = 3 #desplazamientos
    for par in cord:
        if par[1] > der:
            der = par[1]
        if par[1] < izq:
            izq = par[1]

    ancho = der - izq+1
    return ancho, izq, der

#"der" es necesario ratonarlo?
#izq = espacios necesarios a mover a la izquierda.

#Crea una nueva matriz de la pieza donde se excluyen
#las filas y columnas "vacías" (llenas solo de ".").
def RECORTE(entrada):
    cord = COORDENADAS(entrada)
    ancho, izq, der = LARGO(entrada)

    #Crea una matriz del mín. tamaño posible para la pieza.
    pieza = CREAR_MATRIZ_VACIA(cord[-1][0] - cord[0][0]+1, ancho)
    for punto in cord:
        #Calcula el desplazamiento necesario de la pieza hacia la esquina sup. izq.
        #para que quepa perfectamente dentro de su nueva matriz; pieza[x][y].
        pieza[punto[0] - cord[0][0]][punto[1] - izq] = entrada[punto[0]][punto[1]]

    return pieza

#----Cálculo Soluciones y Rotaciones-------------------------------------------------|

#Genera una copia de la
#matriz que le entre.
def COPIAR(matriz):
    nueva = []
    for i in matriz:
        nueva.append(i.copy())

    return nueva


#Calcula las 4 rotaciones posibles
#de una matriz, no necesariamente
#cuadrada, al girarla 90 grados.
def ROTAR(mat, veces):
    nueva = mat
    for i in range(veces): #Veces -> veces que se va a rotar.
        nueva = CREAR_MATRIZ_VACIA(len(mat[0]), len(mat))
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                nueva[len(mat[0]) - 1 - j][i] = mat[i][j]
        mat = nueva

    return nueva


#Genera la inversa de una lista
#y con eso poder encontrar la
#inversa de la matriz.
def INVERSA(entrada):
    inversa = []
    for i in entrada:
        inversa.insert(0, i)

    return inversa


#Primero calcula todas las 8 rotaciones
#de cada pieza y después busca las posibles
#combinaciones de estas en un tablero vacío,
#del largo y ancho establecidos.
def POSIBILIDADES(pieza, L, A):
    rotaciones = []
    for i in range(4): #Hace la rotación 4 veces.
        rotaciones.append(ROTAR(COPIAR(pieza), i))
        ''''''''
        nueva = []
        for fila in rotaciones[-1]:
            nueva.append(INVERSA(fila))
        rotaciones.append(nueva)

    posibilidades = []
    for i in rotaciones:
        for fila in range(0, L - len(i) + 1):
            for columna in range(0, A - len(i[0]) + 1):
                tablero = CREAR_MATRIZ_VACIA(L, A)

                for f in range(len(i)):
                    for c in range(len(i[0])):
                        tablero[fila + f][columna + c] = i[f][c]
                posibilidades.append(tablero)

    return posibilidades


#Revisa la matriz que le entra en busca de ".",
#si no encuentra ninguno significa que todas las
#piezas están bien acómodadas, por lo que sí se
#encontró una posible solución.
def SOLUCION(entrada):
    noHayPuntos = True
    for i in entrada:
        for j in i:
            if (j == "."):
                noHayPuntos = False

    return noHayPuntos


#Determina si una pieza en un posición dentro
#del tablero se puede insertar una pieza, de
#ser así, procede a hacerlo.
def METER(padre, entrada):
    for i in range(len(padre)):
        for j in range(len(padre[0])):
            if entrada[i][j] == ".":
                continue
            if padre[i][j] != ".":
                return False, padre
            padre[i][j] = entrada[i][j]

    return True, padre


#Basados en los principios de la pila (LIFO),
#escoge los hijos de la matriz actual.
def HIJOS(pila, piezas, padre, utilizados):
    for i in range(len(piezas)):
        if i in utilizados:
            continue

        for posicion in piezas[i]:
            lograr, matriz = METER(COPIAR(padre), posicion)
            if lograr == True:
                pila.append([matriz, utilizados + [i]])

    return pila


#----STARTER------------------------------------------------------------------------|

def INICIO():
    #Recibe los inputs según se indica
    L, A, P = map(int, input().split())

    #Recorre el input en P(piezas) y llama a la función RECORTE, la cual
    #se encarga de eliminar el espacio sobrante en las matrices de las piezas.
    piezas = []
    for i in range(P): #Repite este ciclo segúna la cant. de piezas indicadas.
        pieza = RECORTE([list(input()), list(input()), list(input()), list(input())])
        piezas.append(POSIBILIDADES(pieza, L, A)) #Va agregar a una lista las posibles
        #posiciones que puede llegar a tener la pieza en el tablero.

    pila = [[CREAR_MATRIZ_VACIA(L, A),[]]]
    while pila != []:
        pilaPila = pila.pop()

        #Si encuentra una matriz que cumple con lo que establece
        #SOLUCION, la va a imprimir y terminar el ciclo.
        if SOLUCION(pilaPila[0]):
            IMPRIMIR_MATRIZ(pilaPila[0])
            break
        pila = HIJOS(pila, piezas, pilaPila[0], pilaPila[1])

INICIO()
#El código no retorna nada en el caso que no encuentre una solución,
#simplemente se termina la ejecución.