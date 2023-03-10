import pandas as pd
import os
import random
import string


#asignar codigo unico alfanumerico de de tamaño 7
def insert_code_unique(df):
    while True:
        # Generar código aleatorio
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        
        # Verificar si el código ya existe en la tabla
        if not (df.iloc[:, 0] == code).any():
            break
    
    # Asignar el código a la primera columna de todas las filas del dataframe
    df.iloc[:, 0] = code

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

#Cargar el excel con todo. prioritario


def update_excel(filename, sheet_name="Inventario General"):
    df = pd.read_excel(filename, sheet_name)
    return df

#Cargar los codigos de categorias (category_cod) y codigo unico (col cod) ademas de asignar el tipo.
def update_col():
    pass

def set_type():
    pass

## NOTA: asignar por filas y obtener por columnas 

if __name__=="__main__":
	# Funciones validadas
    #convert_pdf_to_audio('lectura.pdf')
    #convert_pdf_to_audio_id('lectura.pdf', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')
    df = update_excel('inventario.xlsx')
    insert_code_unique(df)
    print(df)
    #Falta sin validar
    #convert_pdf_to_audio_name('lectura.pdf','Microsoft David Desktop')
else:
	print("Modulo Importado: [", os.path.basename(__file__), "]")
