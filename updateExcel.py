import pandas as pd
import os
import random
import string
from QR import *

# TODO: split in modular functions as some of this def will only be used once
# TODO: create easy functions on normal use cases like regenerating PDFs from Excel file (useful if the org receives new stuff)

#asignar codigo unico alfanumerico de de tamaño 7
def insert_code_unique(df, code_size=5):
    for i in range(df.shape[0]):
        if pd.isna(df["code"][i]):
            while True:
                # Generar código aleatorio
                code = ''.join(random.choices(string.ascii_uppercase + \
                                            string.ascii_lowercase + string.digits, k=code_size))
                
                # Verificar si el código ya existe en la tabla
                if not df["code"][i] == code:
                    # Asignar el código a la fila
                    df["code"][i] = code
                    break

def insert_code_category(df):
    # Cargar tabla de Categorías
    categorias_df = pd.read_excel('inventario.xlsx', sheet_name='Categorías', header=0)
    categorias_df['category_desc'] = categorias_df["Nombre"]
    
    # Concatenar category_id y subcategory_id en una nueva columna
    categorias_df['category_code'] = categorias_df['category_id'].apply(lambda x: str(x).zfill(2)).astype(str)\
        + categorias_df['subcategory_id'].apply(lambda x: str(x).zfill(2)).astype(str)
    # Guardar en hoja "Categorías" y "Inventario General"
    test_df = pd.merge(df, categorias_df, on="category_desc", how="left")

    df["category_id"] = test_df["category_id"]
    df["subcategory_id"] = test_df["subcategory_id"]
    df["category_code"] = test_df["category_code_y"]

    return df, categorias_df

if __name__=="__main__":
	# Lee el Excel
    df = pd.read_excel('inventario.xlsx', sheet_name="Inventario General", header=0)
    # Inserta la columna 'code' con códigos únicos alfanumericos de tamaño 5
    insert_code_unique(df, 3)

    #Crear columna 'urls' con la combinación sitio web + code
    df["url"] = df["code"].apply(lambda x: 'astrosuite.firebaseapp.com/i/' + x)

    [df, categorias_df] = insert_code_category(df)

    #TODO: Finish, identify large and none qr meritory categories
    df["type"] = df["category_code"].map({ "0900": "large", "0006": "none"}).fillna("small")

    df["message"] = df["type"].map({ "large": "ESCANEA ESTE QR ANTES DE USAR" })

    # Guarda el archivo en Excel
    df.to_excel('exported.xlsx')

    # Genera el PDF con el listado de URLs
    # TODO: debería recibir el Dataframe y usar las columnas title, type, owner y message 
    # para generar un PDF de los small (imagenes con qr y owner de tamaño 1x1.5cm) y los 
    # large (imagenes con qr, owner, title truncado, message y logo de tamaño 7.5x2.5cm)
    generar_pagina(df)
else:
	print("Modulo Importado: [", os.path.basename(__file__), "]")
