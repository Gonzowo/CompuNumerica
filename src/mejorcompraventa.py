from errores import valor_cifras_significativas
from carga_datos import crear_diccionario_dolar, datos
diccionario_dolar = crear_diccionario_dolar(datos)

def encontrar_extremos(diccionario):
    min_precio = 999999999
    max_precio = 0
    min_info = {}
    max_info = {}

    for año, meses in diccionario.items():
        for mes, valor in meses.items():
            if valor < min_precio:
                min_precio = valor
                min_info = {'año': año, 'mes': mes, 'valor_real': valor}
            if valor > max_precio:
                max_precio = valor
                max_info = {'año': año, 'mes': mes, 'valor_real': valor}
                
    return min_info, max_info

def main():
    min_info, max_info = encontrar_extremos(diccionario_dolar)
    
    # Aproximaciones a 3 cifras significativas
    cifras = 3
    precio_compra = valor_cifras_significativas(min_info['valor_real'], cifras)
    precio_venta = valor_cifras_significativas(max_info['valor_real'], cifras)
    
    # Errores absolutos base
    ea_compra = abs(min_info['valor_real'] - precio_compra)
    ea_venta = abs(max_info['valor_real'] - precio_venta)
    
    # Ganancia (aproximados)
    ganancia_aprox = precio_venta - precio_compra
    
    # Propagación de error
    ea_ganancia = ea_compra + ea_venta
    
    # Rentabilidad porcentual
    rentabilidad = (ganancia_aprox / precio_compra) * 100
    
    # Propagación de error en la división
    if ganancia_aprox != 0:
        er_ganancia = ea_ganancia / abs(ganancia_aprox)
    else:
        er_ganancia = 0.0
    er_compra = ea_compra / abs(precio_compra)
    er_rentabilidad = er_ganancia + er_compra
    
    # Error relativo acumulado al error absoluto
    ea_rentabilidad = abs(rentabilidad) * er_rentabilidad

    # Salida de resultados
    print("--- MEJOR COMPRA/VENTA ---")
    print(f"[COMPRA MÍNIMA] : {min_info['mes']} {min_info['año']}")
    print(f"  Valor Original : ${min_info['valor_real']}")
    print(f"  Tasa Aprox     : ${precio_compra} +/- {ea_compra:.2f}\n")
    
    print(f"[VENTA MÁXIMA]  : {max_info['mes']} {max_info['año']}")
    print(f"  Valor Original : ${max_info['valor_real']}")
    print(f"  Tasa Aprox     : ${precio_venta} +/- {ea_venta:.2f}\n")
    
    print("--- PROPAGACIÓN DE ERROR ---")
    print(f"Ganancia Bruta    : ${ganancia_aprox:.2f} +/- {ea_ganancia:.2f} CLP")
    print(f"Rentabilidad Total: {rentabilidad:.2f}% +/- {ea_rentabilidad:.2f}%")

if __name__ == "__main__":
    main()