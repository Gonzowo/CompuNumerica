##################################################
# Obtencion de valor con 2 cifras significativas #
# calculo de Error Absoluto y                    #
# Error Relativo (%)                             #
# a partir de carga_datos.py                     #
##################################################

import math
from carga_datos import crear_diccionario_dolar, datos
diccionario_dolar = crear_diccionario_dolar(datos)

def valor_n_cifras_significativas(valor, n):
    # Redondear a n cifras significativas
    if valor == 0:
        return 0.0
    magnitud = math.floor(math.log10(abs(valor)))
    valor_aprox = round(valor, n - 1 - magnitud)
    return valor_aprox

def obtener_diccionario_errores():
    errores = {}
    max_error = 0
    año_error = "" 
    mes_error = ""
    
    for año, meses in diccionario_dolar.items():
        errores[año] = {}
        for mes, valor in meses.items():
            # valor con 2 cifras significativas
            valor_aprox = valor_n_cifras_significativas(valor, 2)

            # Error absoluto
            error_absoluto = abs(valor - valor_aprox)

            # Error relativo
            error_relativo = round(((error_absoluto / abs(valor))*100), 2)

            # Almacenar los resultados en el nuevo diccionario
            errores[año][mes] = {
                'valor_real': valor,
                'valor_aproximado': valor_aprox,
                'error_absoluto': error_absoluto,
                'error_relativo': error_relativo
            }
            if error_relativo > max_error:
                max_error = error_relativo
                año_error = año
                mes_error = mes
    return errores, max_error, año_error, mes_error

def mostrar_diccionario(errores, max_error, año_error, mes_error):
    # muestra de valores por consola
    for año, meses in errores.items():
        print(f"\n---- AÑO {año} ----")
        for mes, datos in meses.items():
            print(f"Mes: {mes}")
            print(f"  Valor Original: {datos['valor_real']}")
            print(f"  Valor a 2 cifras significativas: {datos['valor_aproximado']}")
            # Se formatea la salida para mostrar 4 decimales por legibilidad
            print(f"  Error Absoluto: {round((datos['error_absoluto']), 2)}") 
            print(f"  Error Relativo: {datos['error_relativo']}\n")
    print("Error maximo: ", max_error, "en el año: ", año_error, "y en el mes: ", mes_error)

def main():
    datos_errores = obtener_diccionario_errores()
    mostrar_diccionario(*datos_errores)

if __name__ == "__main__":
    main()