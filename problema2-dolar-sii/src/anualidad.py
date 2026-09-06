from errores import valor_n_cifras_significativas
from carga_datos import crear_diccionario_dolar, datos
diccionario_dolar = crear_diccionario_dolar(datos)


def calcular_variaciones_anuales(diccionario, n_cifras=3):
    resultados = []
    años_evaluar = ["2022", "2023", "2024", "2025"]
    
    for año in años_evaluar:
        # Verificar que existen los datos
        if año in diccionario:
            precio_enero_real = diccionario[año]["Enero"]
            precio_diciembre_real = diccionario[año]["Diciembre"]
            
            # Valores con 3 cifras significativas
            precio_enero_aprox = valor_n_cifras_significativas(precio_enero_real, n_cifras)
            precio_diciembre_aprox = valor_n_cifras_significativas(precio_diciembre_real, n_cifras)
            
            # Errores absolutos base
            ea_enero = abs(precio_enero_real - precio_enero_aprox)
            ea_diciembre = abs(precio_diciembre_real - precio_diciembre_aprox)
            
            # Variacion Diciembre - Enero
            variacion_precio_aprox = precio_diciembre_aprox - precio_enero_aprox
            variacion_precio_real = precio_diciembre_real - precio_enero_real
            
            # Propagacion del error absoluto
            ea_total = ea_enero + ea_diciembre
            
            # Error relativo incluyendo variacion exacta
            error_relativo = (ea_total / abs(variacion_precio_real)) * 100
                
            resultados.append({
                'año': año,
                'variacion_precio_aprox': variacion_precio_aprox,
                'ea_total': ea_total,
                'error_relativo': error_relativo
            })
    
    # Ordenar la lista de diccionarios de menor a mayor error relativo
    resultados_ordenados = sorted(resultados, key=lambda x: x['error_relativo'])
    return resultados_ordenados

def main():
    resultados = calcular_variaciones_anuales(diccionario_dolar, n_cifras=3)
    
    print("--- CONFIABILIDAD DE LA VARIACIÓN ANUAL ---")
    print("Más confiable al menos confiable (2022-2025)\n")
    
    for rank, res in enumerate(resultados, start=1):
        año = res['año']
        delta_p = res['variacion_precio_aprox']
        ea = res['ea_total']
        err_porc = res['error_relativo']
        
        print(f"[{rank}] Año {año}")
        print(f"    Variación (Precio Dic - Enero) : {delta_p:.2f} +/- {ea:.2f}")
        print(f"    Error relativo                 : {err_porc:.2f}%\n")

if __name__ == "__main__":
    main()