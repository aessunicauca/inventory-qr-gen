import pandas as pd
import os
import random
import string
from QR import *

#asignar codigo unico alfanumerico de de tamaño 7
def insert_code_unique(df, code_size=5):
    for i in range(df.shape[0]):
        while True:
            # Generar código aleatorio
            code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=code_size))
            
            # Verificar si el código ya existe en la tabla
            if not df["code"][i] == code:
                # Asignar el código a la fila
                df["code"][i] = code
                break

#sacar categorias de category_code y en la hoja categorias con el category_id y subcategory_id
def insert_code_category():
    pass

#insertar el mensaje "ANTES DE USAR ESTE ELEMENTO DEBES ESCANEAR ESTE CÓDIGO" si la columna 'type'=="large"
def insert_message():
    pass

#insertar tipo (large o small) como parametro de entrada para buscar es el codigo.
#large =25x15 mm
#
#asigna large si category == Cajas
def insert_type():
    pass

#Depende del tipo de QR asignado en la funcion insert_type
def set_type_qr():
    pass

#Cargar los codigos de categorias (category_cod) y codigo unico (col cod) ademas de asignar el tipo.
def update_col():
    pass

def set_type():
    pass

## NOTA: asignar por filas y obtener por columnas 

if __name__=="__main__":
	# Lee el Excel
    df = pd.read_excel('inventario.xlsx', sheet_name="Inventario General", header=0)
    # Inserta la columna 'code' con códigos únicos alfanumericos de tamaño 5
    insert_code_unique(df, 5)

    #Crear columna 'urls' con la combinación sitio web + code
    df["url"] = df["code"].apply(lambda x: 'astrosuite.firebaseapp.com/' + x)

    # Guarda el archivo en Excel
    df.to_excel('exported.xlsx')

    # Genera el PDF con el listado de URLs
    # TODO: debería recibir el Dataframe y usar las columnas title, type, owner y message 
    # para generar un PDF de los small (imagenes con qr y owner de tamaño 1x1.5cm) y los 
    # large (imagenes con qr, owner, title truncado, message y logo de tamaño 7.5x2.5cm)
    generar_pagina(df["url"].to_list())
else:
	print("Modulo Importado: [", os.path.basename(__file__), "]")
