import matplotlib.pyplot as plt
import numpy as np
from carga_datos import crear_diccionario_dolar, datos
diccionario_dolar = crear_diccionario_dolar(datos)

def evaluar_ciclo_compra_venta(diccionario, monto_inicial=1000000):
    meses_orden = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
                   "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    
    etiquetas_temporales = []
    precios_dolar = []
    errores_flotantes = []
    
    # Extraer datos cronológicamente
    for año in sorted(diccionario.keys()):
        for mes in meses_orden:
            if mes in diccionario[año]:
                precio_actual = diccionario[año][mes]
                
                # Ciclo de conversión
                dolares_comprados = monto_inicial / precio_actual
                pesos_recuperados = dolares_comprados * precio_actual
                
                # Calcular el error introducido por la limitación de la mantisa de 64 bits (Float)
                error_absoluto = monto_inicial - pesos_recuperados
                
                etiquetas_temporales.append(f"{mes[:3]} {año}")
                precios_dolar.append(precio_actual)
                errores_flotantes.append(error_absoluto)
                
    return etiquetas_temporales, precios_dolar, errores_flotantes

def graficar_patrones(etiquetas, precios, errores):
    # Crear una figura con dos subgráficos superpuestos que comparten el eje X
    fig, ax1 = plt.subplots(figsize=(14, 6))

    # Graficar la curva del precio del dólar (Eje Y izquierdo)
    color_precio = 'tab:blue'
    ax1.set_xlabel('Tiempo (Meses)')
    ax1.set_ylabel('Precio Dólar (CLP)', color=color_precio)
    ax1.plot(etiquetas, precios, color=color_precio, marker='o', label='Precio Dólar')
    ax1.tick_params(axis='y', labelcolor=color_precio)
    ax1.tick_params(axis='x', rotation=45)

    # Crear un segundo eje Y que comparte el mismo eje X
    ax2 = ax1.twinx()  
    
    # Graficar el error de punto flotante (Eje Y derecho)
    color_error = 'tab:red'
    ax2.set_ylabel('Error de Recuperación (CLP)', color=color_error)
    ax2.plot(etiquetas, errores, color=color_error, linestyle='--', marker='x', label='Error Float64')
    ax2.tick_params(axis='y', labelcolor=color_error)

    # Configuraciones visuales finales
    plt.title('Correlación entre el Precio del Dólar y el Error de Precisión (Punto Flotante)')
    fig.tight_layout()
    plt.grid(True, alpha=0.3)
    plt.show()

if __name__ == "__main__":
    etiquetas, precios, errores = evaluar_ciclo_compra_venta(diccionario_dolar, monto_inicial=1000000)
    graficar_patrones(etiquetas, precios, errores)