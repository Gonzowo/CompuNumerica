from errores import valor_n_cifras_significativas
from carga_datos import crear_diccionario_dolar, datos
diccionario_dolar = crear_diccionario_dolar(datos)

def evaluacion_entre_puntos():
    # Capital inicial (Pesos chilenos)
    M = 1000000  # Capital inicial (Pesos chilenos)
    # Definicion de las fechas de compra y venta
    año_compra = "2025"
    mes_compra = "Enero"

    año_venta = "2025"
    mes_venta = "Marzo"


    # Comprobacion que las fechas existen en los datos
    if (año_compra in diccionario_dolar and año_venta in diccionario_dolar ):
        valor_real_compra = diccionario_dolar[año_compra][mes_compra]
        valor_real_venta = diccionario_dolar[año_venta][mes_venta]

        precio_compra = valor_n_cifras_significativas(valor_real_compra, 2)
        precio_venta = valor_n_cifras_significativas(valor_real_venta, 2)

        # dolares_comprados = M / precio_compra
        dolares_comprados = M / precio_compra

        # pesos_venta = dolares_comprados * precio_venta
        pesos_venta = dolares_comprados * precio_venta
        
        # ganancia = pesos_venta - M
        ganancia = pesos_venta - M

        # errores relativos de compra y venta
        e_relativo_compra = abs(valor_real_compra - precio_compra) / abs(valor_real_compra)
        e_relativo_venta = abs(valor_real_venta - precio_venta) / abs(valor_real_venta)

        # propagacion de error para las multiplicaciones/divisiones
        e_relativo_acumulado = e_relativo_compra + e_relativo_venta
            
        # error absoluto para los pesos finales
        e_absoluto_pesos = abs(pesos_venta) * e_relativo_acumulado
            
        # error absoluto a la suma/resta (M no suma error)
        e_absoluto_ganancia = e_absoluto_pesos
            
        # error porcentual final de la ganancia
        if ganancia != 0:
            e_porcentual_ganancia = (e_absoluto_ganancia / abs(ganancia)) * 100
        else:
            e_porcentual_ganancia = 0.0

        print(f"--- EVALUACIÓN ENTRE DOS PUNTOS ---")
        print(f"Capital Inicial (M)  : ${M} CLP\n")
    
        print(f"COMPRA en {mes_compra} {año_compra}")
        print(f"    Precio_compra (aproximado): ${precio_compra}")
        print(f"    Dolares obtenidos: {dolares_comprados:.2f} comprados\n")
    
        print(f"VENTA en {mes_venta} {año_venta}")
        print(f"    Tasa aproximada (precio_venta): ${precio_venta}")
        print(f"    Venta por: {dolares_comprados:.2f} * {precio_venta} = ${dolares_comprados * precio_venta:.2f} CLP\n")
    
        print(f"--- RESULTADO ---")
        texto_resultado = f"${abs(ganancia):.2f} +/- {e_absoluto_ganancia:.2f} CLP"
        if ganancia > 0:
            print(f"    Ganancia de         : +{texto_resultado}")
            print(f"    Error porcentual    : {e_porcentual_ganancia:.2f}%")
        elif ganancia < 0:
            print(f"    Pérdida de          : -{texto_resultado}")
            print(f"    Error porcentual    : {e_porcentual_ganancia:.2f}%")
        else:
            print(f"    Punto de equilibrio : $0.00 +/- {e_absoluto_ganancia:.2f} CLP")

def main():
    evaluacion_entre_puntos()

if __name__ == "__main__":
    main()