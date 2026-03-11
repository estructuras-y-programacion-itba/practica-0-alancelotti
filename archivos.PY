def creandorpartida():
    archivo= open("probando1.txt","w")
    archivo.write("J  J1  J2\n")
    archivo.write("G        \n""E        \n""P        \n""F        \n""1        \n""2        \n""3        \n""4        \n""5        \n""6        \n")
    archivo.close()

def escribiendo(jugada,letra,puntos,J):
    n=0
    frase=""
    archivo= open("probando1.txt","r")
    lineas=archivo.readlines()
    archivo.close()
    for L in lineas[jugada]:
        if n==J:
            L=str(puntos)
        frase+=L
        print(L)
        n+=1
    lineas[jugada]=frase
    archivo=open("probando1.txt","w")
    for l in lineas:
        archivo.write(str(l))     
    archivo.close()

creandorpartida()
escribiendo(9,"G  ",60,7)  




# Tu implementacion va aqui
from random import randint
def hola_mundo():
    return "hola_mundo"


def main():
    # Aqui ejecutas tus soluciones
    puntos1=0
    puntos2=0
    crearpartida()
    fin=False
    n=1
    numeros1=[]
    numeros2=[]
    result1= [0,False,False,False,False]
    result2= [0,False,False,False,False]
    while not fin and (not result2[1] or not result2[2] or not result2[3] or not result2[4] or len(numeros2)<6):
        if n%2!=0:
            print(" jugador 1")
            J=3
            vuelta= tiradado(puntos1,result1[1],result1[2],result1[3],result1[4],J)
            fin= vuelta[3]
            vuelta1=vuelta[0]
            result1=vuelta[1]
            if vuelta[2]:
                vuelta2= preguntar(vuelta1)   
                vuelta3= preguntar(vuelta2)
                vuelta3.sort()
                print(vuelta3)
                result1=puntaje(vuelta3,result1[0],result1[1],result1[2],result1[3],result1[4],numeros1,J)
                puntos1= result1[0]
                numeros1= result1[5]
            else:
                puntos1+=vuelta[1][0]
                print("hola")
        else:
            print(" Jugador 2")
            J=7
            vuelta= tiradado(puntos2,result2[1],result2[2],result2[3],result2[4],J)
            fin= vuelta[3]
            vuelta1=vuelta[0]
            result2=vuelta[1]
            if vuelta[2]:
                vuelta2= preguntar(vuelta1)   
                vuelta3= preguntar(vuelta2)
                vuelta3.sort()
                print(vuelta3)
                result2=puntaje(vuelta3,result2[0],result2[1],result2[2],result2[3],result2[4],numeros2,J)
                puntos2= result2[0]
                numeros2= result2[5]
            else:
                puntos2+=vuelta[1][0]
        n+=1
        print(puntos1)
        print(puntos2)
    if puntos1>puntos2:
        print(" Ganos el jugador 1")
    elif puntos2>puntos1:
        print(" Gano el jugador 2")
    else:
        print( " Estamos ante un empate")                
    

def crearpartida():
    archivo= open("partida1.txt","w")
    archivo.write("J  J1  J2\n")
    archivo.write("G         \n""E         \n""P         \n""F         \n""1         \n""2         \n""3         \n""4         \n""5         \n""6         \n")
    archivo.close()

def tiradado(puntos,E,F,G,P,J):
    situacion=True
    fin= False
    d1= randint(1,6)
    d2= randint(1,6)
    d3= randint(1,6)
    d4= randint(1,6)
    d5= randint(1,6)
    vuelta1= [d1,d2,d3,d4,d5]
    vuelta1.sort()
    print(vuelta1)
    if vuelta1[0]==vuelta1[1]==vuelta1[2]==vuelta1[3]==vuelta1[4] and not(G):
        puntos += 80
        G = True 
        situacion= False
        fin= True
        escribir(1,"G  ",80,J)
    elif vuelta1[0]+1==vuelta1[1] and vuelta1[1]+1==vuelta1[2] and vuelta1[2]+1==vuelta1[3] and vuelta1[3]+1==vuelta1[4]  and not(E):
        situacion=False
        puntos += 25
        E = True
        escribir(2,"E  ",25,J)
    elif ((vuelta1[0]==vuelta1[1]==vuelta1[2]==vuelta1[3] or vuelta1[1]==vuelta1[2]==vuelta1[3]==vuelta1[4])) and not(P):
        situacion=False
        puntos += 45
        P = True
        escribir(3,"P  ",45,J)
    elif ((vuelta1[0]==vuelta1[1]==vuelta1[2] and vuelta1[3]==vuelta1[4]) or (vuelta1[0]==vuelta1[1] and vuelta1[2]==vuelta1[3]==vuelta1[4])) and not(F):
        print(F)
        situacion=False
        puntos += 35
        F = True
        escribir(4,"F  ",35,J)
    return vuelta1, [puntos,E,F,G,P],situacion, fin


def preguntar (vuelta):
    posiciones=[1,2,3,4,5]
    print("                      posiciones:",posiciones,"\n")
    print ("queres volver a tirar algun dado?",vuelta)
    n=int(input("cuantos queres cambiar?"))
    for i in range(n):
        posicion= int(input("que dado volves a tirar? (Ponga la posicion en la que esta dicho dado)")) 
        vuelta[posicion-1]=randint(1,6)
    return vuelta      


def puntaje (vuelta3,puntos,E,F,G,P,numeros,J):
    n=0
    if vuelta3[0]==vuelta3[1]==vuelta3[2]==vuelta3[3]==vuelta3[4] and not(G):
        puntos += 50
        G = True
        escribir(1,"G  ",50,J)
    elif vuelta3[0]+1==vuelta3[1] and vuelta3[1]+1==vuelta3[2] and vuelta3[2]+1==vuelta3[3] and vuelta3[3]+1==vuelta3[4]  and not(E):
        puntos += 20
        E = True
        escribir(2,"E  ",20,J)
    elif (vuelta3[0]==vuelta3[1]==vuelta3[2]==vuelta3[3] or vuelta3[1]==vuelta3[2]==vuelta3[3]==vuelta3[4]) and not(P):
        puntos += 40
        P = True
        escribir(3,"P  ",40,J)
    elif ((vuelta3[0]==vuelta3[1]==vuelta3[2] and vuelta3[3]==vuelta3[4]) or (vuelta3[0]==vuelta3[1] and vuelta3[2]==vuelta3[3]==vuelta3[4])) and not(F):
        puntos += 30
        F = True
        escribir(4,"F  ",30,J)
    elif vuelta3[0] not in numeros or vuelta3[1] not in numeros or vuelta3[2] not in numeros or vuelta3[3] not in numeros or vuelta3[4] not in numeros : 
        cont=0
        n= int(input("que numero queres sumar? En caso de no querer sumar ninguno ponga 0  "))
        while (n in numeros) or ((n not in vuelta3) and n!=0):
            n= int(input("Ese numero ya fue usado o no esta dentro de las opciones, porfavor elija otro. En caso de no querer sumar ninguno ponga 0    "))
        for i in vuelta3:
            if n==i :   
                cont+=i
                print(cont,"este es el puntaje")
                puntos+= i
                if i not in numeros:
                    numeros.append(i)            
        if n!=0:
            escribir(n+4,str(n)+"  ",cont,J)
        if n==0 :      
            lista=tachar(E,F,G,P,numeros,J)
            E=lista[0]
            F=lista[1]
            G=lista[2]
            P=lista[3]
            numeros= lista[4]
    else:
        lista=tachar(E,F,G,P,numeros,J)
        E=lista[0]
        F=lista[1]
        G=lista[2]
        P=lista[3]
        numeros= lista[4]
    return puntos,E,F,G,P,numeros

def tachar(E,F,G,P,numeros,J):
    situacion= True
    while situacion:
        opcion= input(" Elija que opcion desea tachar ")
        if (opcion=="G" or opcion== "g") and not(G):
            G=True
            situacion= False
            escribir(1,"G  ",0,J)
        elif (opcion=="E" or opcion== "e") and not(E):
            E=True
            situacion= False
            escribir(2,"E  ",0,J)  
        elif (opcion=="F" or opcion== "f") and not(F):
            F=True
            situacion= False
            escribir(4,"F  ",0,J) 
        elif (opcion=="P" or opcion== "p") and not(P):
            P=True
            situacion= False 
            escribir(3,"P  ",0,J)  
        elif 49<=ord(opcion)<=54:
            if int(opcion) not in (numeros):
                situacion=False
                numeros.append(int(opcion)) 
                escribir(int(opcion)+4,opcion+"  ",0,J)                   
    return E,F,G,P,numeros   

def escribir(jugada,letra,puntos,J):
    n=0
    frase=""
    archivo= open("partida1.txt","r")
    lineas=archivo.readlines()
    archivo.close()
    for L in lineas[jugada]:
        if n==J:
            L=str(puntos)
        frase+=L
        n+=1
    lineas[jugada]=frase
    archivo=open("partida1.txt","w")
    for l in lineas:
        archivo.write(str(l))     
    archivo.close()

# No cambiar a partir de aqui
if __name__ == "__main__":
    main()
