from clases import Automovil
import csv


def imprimir(objeto,datos):
    """
    funcion generica para imprimir informacion,
    recibe 2 parametros 
    <objeto> que sirve para visualizar el concepto a imprimir
    <datos>  que sirve para visualizar el detalle del concepto
    """
    print("\n********************************************************************************************************************************************************************")
    print(f"{objeto} {datos}")
    print("********************************************************************************************************************************************************************")
    
##### implementar modo "x" para que generre error y usar  try  except
    
def guardar(archivo,informacion):
    """
    funcion generica para guardar informacion en un archivo,
    recibe 2 parametros 
    <archivo>     que es el nombre del archivo
    <informacion> que son los datos a registrar en el archivo
    """    
    informacion2 = str(informacion)
    informacion2 += "\n"
    with open(archivo, 'a') as fichero:
        fichero.write(informacion2)
        fichero.close()
        
def guardar_encabezado(archivo,encabezados):
    """
    funcion generica para guardar en encabezado en un archivo,
    recibe 2 parametros 
    <archivo>     que es el nombre del archivo
    <encabezados> que son los encabezados a registrar en el archivo
    """ 
    existe_archivo=False
    try:
        if open(archivo):
            return
    except:
        existe_archivo=True
        with open(archivo, 'a') as fichero:
            fichero.write(str(encabezados))
            fichero.close()

def recuperar(nombre_archivo):
    """
    funcion generica para recuperar la informacion de un archivo,
    recibe 1 parametro
    <nombre_archivo>     que es el nombre del archivo
    """ 
    vehiculos = []
    archivo = open(nombre_archivo, "r")
    archivo_csv = csv.reader(archivo)
    for vehiculo in archivo_csv:
        vehiculos.append(vehiculo)
    archivo.close()
    return vehiculos

def obtenerEncabezados(encabezados):
    """
    funcion generica para obtener los encabezados desde un objeto,
    recibe 1 parametro
    <encabezados>     que es el nombre del objeto
    """ 
    titulos = ""
    for detalle in encabezados:
        detalle+=","
        titulos += detalle
    titulos += "\n"
    
    return titulos

def obtenerListaEncabezados(encabezados):
    """
    funcion generica para crear una lista con los encabezados de un objeto,
    recibe 1 parametro
    <encabezados>     que es el nombre del objeto
    """ 
    lista_encabezado = []
    for detalle_encabezado in encabezados:
        lista_encabezado.append(detalle_encabezado)
    
    return lista_encabezado

def datos_de_diccionario(diccionario,encabezados):
    """
    funcion generica para obtener los datos de un objeto,
    recibe 2 parametros
    <diccionario>     que es el nombre del diccionario
    <encabezados>     que es la lista con encabezados del diccionario
    """ 
    diccionario2 = dict=[diccionario]
    contador=0
    datos = []
    largo=encabezados.__len__()
    for row, _dict in enumerate(diccionario2):
        for col, key in enumerate(encabezados):
            contador+=1
            datos.append(_dict[key])
            if contador==largo:
                contador=0

    datos_str = str(datos)
    cadena1       = datos_str.replace("[", "")
    datos_finales = cadena1.replace("]", "")
    
    return datos_finales