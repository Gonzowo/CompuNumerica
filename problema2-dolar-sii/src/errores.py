##################################################
# Obtencion de valor con 2 cifras significativas #
# calculo de Error Absoluto y                    #
# Error Relativo (%)                             #
# a partir de carga_datos.py                     #
##################################################

import numpy as np
from carga_datos import crear_diccionario_dolar, datos
diccionario_dolar = crear_diccionario_dolar(datos)

def valor_n_cifras_significativas(valor, n):
    if valor == 0:
        return 0.0
    magnitud = np.floor(np.log10(np.abs(valor)))
    valor_aprox = np.round(valor, int(n - 1 - magnitud))
    return float(valor_aprox)

def obtener_diccionario_errores():
    errores = {}
    lista_años = []
    lista_meses = []
    lista_valores = []
    
    for año, meses in diccionario_dolar.items():
        errores[año] = {}
        for mes, valor in meses.items():
            lista_años.append(año)
            lista_meses.append(mes)
            lista_valores.append(valor)

    arr_valores = np.array(lista_valores, dtype=np.float64)
    arr_magnitudes = np.floor(np.log10(np.abs(arr_valores)))
    decimales = 2 - 1 - arr_magnitudes
    factores = 10.0 ** decimales
    arr_aprox = np.round(arr_valores * factores) / factores
    
    arr_err_abs = np.abs(arr_valores - arr_aprox)
    arr_err_rel = np.round((arr_err_abs / np.abs(arr_valores)) * 100, 2)
    
    idx_max = np.argmax(arr_err_rel)
    max_error = arr_err_rel[idx_max]
    año_error = lista_años[idx_max]
    mes_error = lista_meses[idx_max]
    
    for i in range(len(lista_valores)):
        año = lista_años[i]
        mes = lista_meses[i]
        errores[año][mes] = {
            'valor_real': float(arr_valores[i]),
            'valor_aproximado': float(arr_aprox[i]),
            'error_absoluto': float(arr_err_abs[i]),
            'error_relativo': float(arr_err_rel[i])
        }
    return errores, float(max_error), año_error, mes_error

def mostrar_diccionario(errores, max_error, año_error, mes_error):
    # muestra de valores
    for año, meses in errores.items():
        print(f"\n---- AÑO {año} ----")
        for mes, datos in meses.items():
            print(f"Mes: {mes}")
            print(f"  Valor Original: {datos['valor_real']}")
            print(f"  Valor a 2 cifras significativas: {datos['valor_aproximado']}")
            # salida para mostrar 2 decimales 
            print(f"  Error Absoluto: {round((datos['error_absoluto']), 2)}") 
            print(f"  Error Relativo: {datos['error_relativo']}\n")
    print("Error maximo: ", max_error, "en el año: ", año_error, "y en el mes: ", mes_error)

def main():
    datos_errores = obtener_diccionario_errores()
    mostrar_diccionario(*datos_errores)

if __name__ == "__main__":
    main()