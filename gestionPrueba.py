#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Escribir un programa para gestionar un listado telefónico con los nombres y los teléfonos de los clientes de una empresa. El programa incorpora funciones para crear el fichero con el listado si no existe, para consultar el teléfono de un cliente, añadir el teléfono de un nuevo cliente y eliminar el teléfono de un cliente. El listado debe estar guardado en el fichero de texto listado.txt donde el nombre del cliente y su teléfono deben aparecer separados por comas y cada cliente en una línea distinta
#el r+ es un rew 



ficherito={
    "Andres":"112312311",
    "Antonio": "15321204",
    "Juan": "123112313",
    "Pedro": "123123123",
    "Kevin":""

} 
comandos=[1,2,3,4,5]
listado="listado.txt"

def crearFicheroEcho():
    with open(listado,"w") as Fichero:
        for i in ficherito:
            Fichero.write(i+","+ficherito[i]+"\n")#antes era un "\n" #+","
        Fichero.close()  

""" def crearFichero():
    with open("fichero.txt","r+") as Fichero:
        contenido=Fichero.read()
        print(contenido)
        Fichero.close() """

def consultarCliente(cliente):      #Metodo para saber si el cliente existe en el fichero
    with open(listado, "r") as file: 
        for i in file:
            renglon= i.split(',')
            if cliente in renglon:
                return True
def consultarTelefono(cliente): #METODO PARA CONSULTAR EL TELEFONO DE UN CLIENTE
    with open(listado, "r") as file: 
        for i in file:
            renglon= i.split(',') # separo el renglon en un arreglo divido por la ','
            if cliente in renglon: #pregunto si el cliente se encuetra en el renglon
                #print(renglon)
                resutlado=renglon[1].rsplit('\n')
                return resutlado[0] #retorno el valor
            #
                #print("No se encontro el nuemro")
              

def añadirClienteYTelefono(cliente,telefono): #METODO PARA CREAR UN CLIENTE CON TELEFONO
    with open(listado,"a") as Fichero:    #escribe al final del archivo
        Fichero.write(cliente+","+telefono+"\n")       #inserta el nombre y el telefono del cliente
        Fichero.close()
    

def eliminarTelefono(cliente):  #METODO PARA ELIMINAR EL TELEFONO DE UN CLIENTE
   with open(listado, "r") as file: 
    clienteYNum= file.readlines()   #lee el archivo asi ej: ['Andres,112312311\n' , []...]
    for i,value in enumerate(clienteYNum):
        if cliente in value:
            clienteYNum[i]=cliente+","+'\n'       #Reemplaza el array con solo el nombre del cliente
            
    file.close()

   with open(listado, "w") as file: #escribe de nuevo todo el archivo ya modificado
    file.writelines(clienteYNum)
    file.close() 

def añadirTelefono(cliente,telefono):#METODO PARA AÑADIR UN TELEFONO A UN CLIENTE EXISTENTE
    with open(listado,"r") as file:
     clienteYNum= file.readlines()
     for i,values in enumerate(clienteYNum):
         if cliente in values:
             clienteYNum[i]= cliente+","+str(telefono)+'\n'
             
     file.close()
    with open(listado, "w") as file: #escribe de nuevo todo el archivo ya modificado
        file.writelines(clienteYNum)
        file.close() 


def pedirClientePorConsola():   #Metodo para consultar por consola al cliente, utiliza el metodo consultaCliente()
    while True:
        try:
            cliente=str(input("Ingrese el nombre del cliente para hacer la accion: ")).capitalize()
        except ValueError:
            print("Debe de ingresar un nombre valido")
        else:
            resultado=consultarCliente(cliente)
            if resultado is None:
                print("Error, el cliente:",cliente,"no se encuetra en el fichero, intentelo nuevamente")
            else:
                break
    return cliente

def pedirNumeroPorConsola(): #Metodo para Añadir número de telefono
    while True:
        try:
            numero=int(input("Ingrese un nuevo telefono para el cliente: "))
        except ValueError:
            print("Debe de ser un numero")
        else:
            break
    return numero

##El programa empieza desde aqui.
print("Bievenido a nuestro programa de gestion de listado telefonico, eliga entre las siguientes opciones:\n",
    "1.Crear un fichero(Recomendado)        2.Consultar el telefono de un cliente\n",
    "3.Añadir un cliente con su telefono    4.Eliminar telefono de un cliente\n",
    "5.Añadir el telefono de un cliente")
while True:
    try:
        eleccion=int(input("Ingrese opciones entre el  1 al 5: "))
        
    except ValueError:
        print("Error, la elecion debe de ser un numero")
    else:
        if eleccion not in comandos:
            print("Se tiene que elegir la opcion entre el 1 al 5 por favor intentelo de nuevo")
        else:
            break


if eleccion == 1:  #1.Crear un fichero(Recomendado)
    crearFicheroEcho()
    print("Se ha creado el fichero con algunos datos predeterminados, puede verlos en \"listado.txt\" \n")

elif eleccion == 2:     #2.Consultar el telefono de un cliente
    nombreCliente=pedirClientePorConsola()
    resultado=consultarTelefono(nombreCliente)
    if resultado == "":
        print("El cliente no tiene telefono")
    else:
        print(f"El teléfono del cliente \"{nombreCliente}\" es: {resultado}") #para Python 3.6 o superiores
    #print("El teléfono del cliente ",nombreCliente,"es:",resultado)

elif eleccion == 3: #3.Añadir un cliente con su telefono
    while True:
        try:
            nombreCliente=str(input("Ingrese el nombre del nuevo cliente:\n")).capitalize()
        except ValueError:
            print("Error, intentelo nuevamente")
        else:
            break
    numeroCliente=pedirNumeroPorConsola()
    añadirClienteYTelefono(nombreCliente,str(numeroCliente))
    print("El cliente",nombreCliente, "con su número",numeroCliente,"fue añadido al archivo \"fichero.txt\"")

elif eleccion == 4: #4.Eliminar telefono de un cliente
    nombreCliente=pedirClientePorConsola()
    eliminarTelefono(nombreCliente)
    print("El número del cliente",nombreCliente, "a sido eliminado" )

else:   #Eleccion 5.  #5.Añadir el telefono de un cliente
    nombreCliente=pedirClientePorConsola()
    numeroCliente=pedirNumeroPorConsola()
    añadirTelefono(nombreCliente,numeroCliente)
    print("El telefono",numeroCliente, "a sido añadido al cliente",nombreCliente)

        
#Si la eleccion es 1 se crea el fichero, no pide datos adicionales:
#Si la eleccion es 2 se consulta el telefono del cliente, se pide el nombre del cliente.
#Si la eleccion es 3 se añade un cliente con su telefono, se pide nombreCliente, numCliente
#Si la eleccion es 4 se elimina un telefono, se pide el nombre del cliente.
#Si la eleccion es 5 se ingresa un nuevo telefono, se pide el nombre del cliente

#Valoracion personal: odio el manejo de String