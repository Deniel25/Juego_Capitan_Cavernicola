x=10                                #Variables que determinan las medidas de los volcanes
y=18                                
def triangulo (x,y):
    t=[]                            #Funcion que crea los volcanes
    for i in range(0,x):            #Creación de  listas vacias (columnas)
        t.append([])                    
    for i in range(0,x):            #Se rellenan las listas nuevamente con espacios
        for j in range(0,y):        #Se forma el tablero de forma rectangular con
            t[i].append(" ")        #espacios " " en cada lista
                
    der=8                               #2 variables que crearan los "bordes" o "limites" del
    izq=8                               #triagulo, parten con el mismo número porque es la punta
    for i in range(0,x-1):              #del volcan, y se reemplazan los espacios por "*" siempre
        for z in range(0,y-1):          #y cuando cumplan con la condición de que quede dentro
            if ((z<=der)and(z>=izq)):   #de los "bordes" o "limites"
                t[i][z]="*"
        der=der+1
        izq=izq-1
    return t

def imprimir_triangulo (t,x,y):
    print()
    print("|  -x 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16")
    print("y")                          
    for i in range (0,x-1):               #Función para imprimir el volcan, este se debe mostrar en pantalla
        print(i,"   ",end=" ")            #Esta función imprimirá las x-1 columnas y las y-1 filas para mostar en pantalla el volcan correspondiente.
        for j in range (0,y):
            print(t[i][j], end="  ")
        print()
    print()
    
def random(t,x,y):
    import random                       #Funcion para implementar los osos de manera random en un volcan, en esta ocación se implementaran en el volcan osos.
    r=0
    while(r<24):
        q=random.randrange(y-1)
        w=random.randrange(x-1)
        if (t[w][q]=="*"):
            t[w][q]= "X"
            r=r+1
    return t

def explorar(f,d):
    c = 0
    if (osos[f][d]!=" "):                   #Funcion para explorar y reemplzar las cuevas con el numero de osos alrededor. 
        for i in range(-1,2):
            if (osos[f-1][d+i]=="X"):
                c=c+1
        for i in range(-1,2):
            if (osos[f][d+i]=="X"):
                c=c+1
        for i in range(-1,2):
            if (osos[f+1][d+i]=="X"):
                c=c+1
        osos[f][d]=c
        marcas[f][d]=c
        return c

#####################################################################################################
    
for i in range(0,4):
    print()
#print("                             Hola")                          #Presentación del Juego y
print("              Bienvenido a Super Osito Searcher DX")         #Pantalla de titulo.
print()
#print("             Desarrollado por el equipo Daniel^2+Ana")
print()
print()
print()
print("                            v2.5.1")
print()
input("                 Presione enter para comenzar")

for i in range(0,3):
    print()
game_over="s"                                           
while(game_over!="n"):                                              #While para validar si desea jugar otra vez.
    marcas=triangulo(x,y)
    imprimir_triangulo(marcas,x,y)                                  #Creacion de volcanes (marcas y osos)
    osos=triangulo(x,y)                                             #Se imprime marcas.
    osos=random(osos,x,y)
    #JUEGO
    game_over="si"
    while (game_over=="si"):
        f=int(input("Ingrese coordenada y: "))                          #Preguntas del desarrollo del juego con su validación correspondiente.
        while (f<0 or f>x-2):
            f=int(input("Ingrese coordenada y valida entre 0 y 8: "))
        d=int(input("Ingrese coordenada x: "))
        while (d<0 or d>y-2):
            d=int(input("Ingrese coordenada x valida entre 0 y 16: "))
        while (marcas[f][d]==" "):
            d=int(input("Ingrese coordenada x valida: "))
        o=input("Qué quiere hacer Marcar/Desmarcar(m) Explorar(e): ")
        while (o!="m" and o!="e"):
            o=input("Qué quiere hacer Marcar/Desmarcar(m) Explorar(e): ")           
        print()    
        if (o=="e"):
            if (osos[f][d]=="X" and (osos[f][d]!="*")):                     #En caso de explorar y encontrarse con un oso, el juego se termina.
                imprimir_triangulo(osos,x,y)
                print ("                        PERDISTE JAJAJA")
                print()                    
                game_over=input("Deseas revivir?? si(s) no(n): ")     #Pregunta para volver a jugar con su validación.
                while(game_over!="s" and game_over!="n"):
                    game_over=input("Deseas revivir?? si(s) no(n): ")
            else:
                explorar(f,d)
                if explorar(f,d)==0:             
                    explorar(f-1,d-1)                       #en caso de que al explorar, la función eplorar marque un "0" en el tablero, las cuevas alrrededor
                    explorar(f-1,d)                         #del "0" se exploraran automaticamente.
                    explorar(f-1,d+1)
                    explorar(f,d-1)
                    explorar(f,d+1)
                    explorar(f+1,d-1)
                    explorar(f+1,d+1)
                    explorar(f+1,d)
                imprimir_triangulo(marcas,x,y)          #Se imprime el volcan para ver el progreso.
            cont=0
            for i in range (0,x-1):                     #Contador que va revisando si el numero de * que hay en el tablero.
                for j in range (0,y):
                    if(osos[i][j]=="*"):
                        cont=cont+1
            if (cont==0):                               #En el caso de explorar todas las cuevas y que el contador se mantenga en 0
                print()                                 #El juego termina con una victoria para el jugador.
                imprimir_triangulo(osos,x,y)
                print()
                print("                   Felicidades Ganaste!! :D")
                print()
                game_over=input("Deseas jugar otra vez?? si(s) no(n): ")                 #Pregunta para volver a jugar con su validación.
                while(game_over!="s" and game_over!="n"):
                    game_over=input("Deseas jugar otra vez?? si(s) no(n): ")           
        else:
            if (marcas[f][d]=="*"):                     #Remplazo de los * por + en caso de que se desee marcar una cueva.
                marcas[f][d]="+"
                imprimir_triangulo(marcas,x,y)
            else:
                if (marcas[f][d]=="+"):                 #Remplazo de los + por * en caso de que se desee desmarcar una cueva.
                    marcas[f][d]="*"
                    imprimir_triangulo(marcas,x,y)
                else:
                    print("No se puede marcar/desmarcar esta cueva, pruebe con otra.")      #En el caso de de haber un número en la cueva, no permitirá
                    print()                                                                 #remplazo de caracter * o +.
print()
input("                           Adios :)")                                 #Mensaje de despedida en caso de que el jugador no quiera seguir jugando.
