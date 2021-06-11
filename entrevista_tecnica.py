from os import system

#python 3.9.5


def suma_adyacentes(data,ejem):

    #if para condicionar el mensaje si es de los ejemplos(1,2) o solo la lista ingresada 
    if(ejem==0):
        print("***datos de la lista "+ repr(data)+"\n")
    else:
        print("***Ejemplo "+repr(ejem)+", lista "+ repr(data)+"\n")
        
    sum=0

    # for para recorrer el array y verificar los numeros adyacentes 
    for i in range(0,len(data)-1,1) :
        
        if((data[i+1]-data[i])==1):
            print("los numeros ["+repr(data[i])+"] ["+repr(data[i+1])+"] son adyacente\n")
            if(sum<(data[i+1]+data[i])):
                sum=data[i+1]+data[i]
    print("\n\t[ La suma de los numeros adycentes mas alta es = "+repr(sum)+" ]\n")
    print("presiona una tecla...")
    input()


def menu():

    system("cls")
    print( '* ENTREVISTA TECNICA \n \tencontrar los elementos de la lista que son adyacentes(juntos en la lista) y tienen la mayor suma.\n \tRetornar el resultado de sumarlos')
    print("[1] Ejemplos dados")
    print("[2] Ingresar datos ")    
    print("[0] Salir")


#funcion principal
def main() :  
  
    op=1
    while( op != 0 ):
        
        menu()

        #try para validar que  sea un numero
        try:
            op = int(input())
            
            
            if(op==1):

                system("cls")
                data=[1,2,3]
                suma_adyacentes(data,1)
                data=[4,5,1,2,3,4]
                suma_adyacentes(data,2)

            elif(op==2):

                data=[]
                print("ingresa 6 numeros ala lista ")
                for x in range(6):
                        num=int(input())
                        data.append(num)        
                suma_adyacentes(data,0)
            else:

                print("ingresa una opcion correcta")
                print("presiona una tecla...")
                input()

        except ValueError:
            print ("Debe ingresar un número correcto.")
            print("presiona una tecla...")
            input()
       
       


main()
