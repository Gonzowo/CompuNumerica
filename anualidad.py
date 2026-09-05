import math
from CompuNumerica.src.carga_datos import diccionario_dolar
from CompuNumerica.src.errores import valor_n_cifras_significativas

def calcular_variaciones_anuales(diccionario, n_cifras=3):
    resultados = []
    años_evaluar = ["2022", "2023", "2024", "2025"]
    
    for año in años_evaluar:
        # Verificar que existen los datos requeridos para el año en curso
        if año in diccionario and "Enero" in diccionario[año] and "Diciembre" in diccionario[año]:
            p_enero_real = diccionario[año]["Enero"]
            p_diciembre_real = diccionario[año]["Diciembre"]
            
            # 1. Aproximaciones
            p_enero_aprox = valor_n_cifras_significativas(p_enero_real, n_cifras)
            p_diciembre_aprox = valor_n_cifras_significativas(p_diciembre_real, n_cifras)
            
            # 2. Errores absolutos base
            ea_enero = abs(p_enero_real - p_enero_aprox)
            ea_diciembre = abs(p_diciembre_real - p_diciembre_aprox)
            
            # 3. Variación (Diciembre - Enero)
            delta_p_aprox = p_diciembre_aprox - p_enero_aprox
            delta_p_real = p_diciembre_real - p_enero_real
            
            # 4. Propagación del error absoluto en la resta
            ea_total = ea_enero + ea_diciembre
            
            # 5. Cálculo del error porcentual respecto a la variación exacta
            if delta_p_real != 0:
                error_porcentual = (ea_total / abs(delta_p_real)) * 100
            else:
                # Si la variación real es cero, el error porcentual tiende a infinito
                error_porcentual = float('inf') 
                
            resultados.append({
                'año': año,
                'delta_p_aprox': delta_p_aprox,
                'ea_total': ea_total,
                'error_porcentual': error_porcentual
            })
    
    # Ordenar la lista de diccionarios de menor a mayor error porcentual
    resultados_ordenados = sorted(resultados, key=lambda x: x['error_porcentual'])
    return resultados_ordenados

def main():
    # Se utilizan 3 cifras significativas para mantener la consistencia con el cálculo anterior
    resultados = calcular_variaciones_anuales(diccionario_dolar, n_cifras=3)
    
    print("--- CONFIABILIDAD DE LA VARIACIÓN ANUAL (ΔP = Diciembre - Enero) ---")
    print("Orden: Del más confiable (menor %) al menos confiable (mayor %)\n")
    
    for rank, res in enumerate(resultados, start=1):
        año = res['año']
        delta_p = res['delta_p_aprox']
        ea = res['ea_total']
        err_porc = res['error_porcentual']
        
        print(f"[{rank}] Año {año}")
        print(f"    Variación (ΔP ± Ea) : {delta_p:.2f} ± {ea:.2f}")
        print(f"    Error porcentual    : {err_porc:.2f}%\n")

if __name__ == "__main__":
    main()