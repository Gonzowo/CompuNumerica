###################################
# Laboratorio Evaluado n°1        #
# Gonzalo Cerpa Salas 21/08/2026  #
###################################

import numpy as np

datos = np.genfromtxt(
    fname='../data/dolar_observado_sii_2022_2025.csv',
    delimiter=',',
    names=True,
    dtype=None,
    encoding='utf-8'
)

# Diccionario para leer los valores en otros archivos
def crear_diccionario_dolar(datos):
    diccionario_dolar = {}
    for fila in datos:
        año = str(fila['anio']) 
        mes = str(fila['mes'])
        valor = float(fila['dolar_observado_promedio_clp'])
        
        if año not in diccionario_dolar:
            diccionario_dolar[año] = {}
            
        diccionario_dolar[año][mes] = valor
    return diccionario_dolar

def main():
    diccionario_dolar = crear_diccionario_dolar(datos)

if __name__ == "__main__":
    main()