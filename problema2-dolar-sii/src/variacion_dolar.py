from errores import valor_n_cifras_significativas
from carga_datos import crear_diccionario_dolar, datos
diccionario_dolar = crear_diccionario_dolar(datos)

def variacion(diccionario, año_inicio, año_fin, mes, n_cifras):
    precio_inicio_real = diccionario[año_inicio][mes]
    precio_final_real = diccionario[año_fin][mes]

    precio_ini_aprox = valor_n_cifras_significativas(precio_inicio_real, n_cifras)
    precio_final_aprox = valor_n_cifras_significativas(precio_final_real, n_cifras)

    # Errores absolutos
    ea_inicio = abs(precio_inicio_real - precio_ini_aprox)
    ea_fin = abs(precio_final_real - precio_final_aprox)

    # Variacion y propagacion
    variacion_aprox = precio_final_aprox - precio_ini_aprox
    ea_propagado = ea_inicio + ea_fin

    # Error porcentual
    delta_p_real = precio_final_real - precio_inicio_real
    error_porcentual = (ea_propagado / abs(delta_p_real)) * 100 if delta_p_real != 0 else 0.0

    return {
        'precio_ini_aprox': precio_ini_aprox,
        'ea_inicio': ea_inicio,
        'precio_final_aprox': precio_final_aprox,
        'ea_fin': ea_fin,
        'variacion_aprox': variacion_aprox,
        'ea_propagado': ea_propagado,
        'error_porcentual': error_porcentual
    }

def mostrar_resultados(año_inicio, año_fin, mes, n_cifras, res):
    print("--- VARIACION DEL DOLAR (Diciembre 2022 hasta Diciembre 2023) ---")
    print(f"Valor 2022: {res['precio_ini_aprox']} (Error absoluto = {res['ea_inicio']:.2f})")
    print(f"Valor 2023: {res['precio_final_aprox']} (Error absoluto = {res['ea_fin']:.2f})")
    print(f"ΔP +/- error    : {res['variacion_aprox']:.2f} +/- {res['ea_propagado']:.2f}")
    print(f"Error porcentual: {res['error_porcentual']:.2f}%")

def main():
    año_inicio = "2022"
    año_fin = "2023"
    mes = "Diciembre"
    n_cifras = 3
    resultados = variacion(diccionario_dolar, año_inicio, año_fin, mes, n_cifras)
    mostrar_resultados(año_inicio, año_fin, mes, n_cifras, resultados)

if __name__ == "__main__":
    main()