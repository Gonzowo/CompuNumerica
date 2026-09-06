import matplotlib.pyplot as plt
import numpy as np
from carga_datos import crear_diccionario_dolar, datos
diccionario_dolar = crear_diccionario_dolar(datos)


def evaluar_ciclo_compra_venta(diccionario, monto_inicial):
    meses_orden = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
                   "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    
    etiquetas_temporales = []
    precios_dolar = []
    errores_flotantes = []
    
    # Extraer datos
    for año in sorted(diccionario.keys()):
        for mes in meses_orden:
            if mes in diccionario[año]:
                precio_actual = diccionario[año][mes]
                
                dolares_comprados = monto_inicial / precio_actual
                pesos_recuperados = dolares_comprados * precio_actual
                
                # Error por la mantisa de 64 bits
                error_absoluto = monto_inicial - pesos_recuperados
                
                etiquetas_temporales.append(f"{mes[:3]} {año}")
                precios_dolar.append(precio_actual)
                errores_flotantes.append(error_absoluto)
                
    return etiquetas_temporales, precios_dolar, errores_flotantes

def graficar_patrones(etiquetas, precios, errores):
    # Crear una figura
    fig, ax1 = plt.subplots(figsize=(14, 6))

    # Graficar la curva del precio del dolar
    color_precio = 'tab:blue'
    ax1.set_xlabel('Tiempo en meses')
    ax1.set_ylabel('Precio Dolar a CLP', color=color_precio)
    ax1.plot(etiquetas, precios, color=color_precio, marker='o', label='Precio Dolar')
    ax1.tick_params(axis='y', labelcolor=color_precio)
    ax1.tick_params(axis='x', rotation=45)

    # Crear un segundo eje Y
    ax2 = ax1.twinx()  
    
    # Graficar el error de punto flotante
    color_error = 'tab:red'
    ax2.set_ylabel('Error de punto flotante', color=color_error)
    ax2.plot(etiquetas, errores, color=color_error, linestyle='--', marker='x', label='Error Float64')
    ax2.tick_params(axis='y', labelcolor=color_error)

    # Visuales
    plt.title('La ida y vuelta que no vuelve (2022-2025)')
    fig.tight_layout()
    plt.grid(True, alpha=0.3)

    # Guardar grafico en carpeta graficos
    plt.savefig('../graficos/error_punto_flotante_2022_2025.png', dpi=300, bbox_inches='tight')

    plt.show()

def comparar_precision_flotante():
    exacto = -0.99
    
    # Resta en float32
    float32_v1 = np.float32(874.67)
    float32_v2 = np.float32(875.66)
    res_float32 = float32_v1 - float32_v2
    error_float32 = abs(exacto - res_float32)
    
    # Resta en float64
    float64_v1 = np.float64(874.67)
    float64_v2 = np.float64(875.66)
    res_float64 = float64_v1 - float64_v2
    error_float64 = abs(exacto - res_float64)
    
    print("--- COMPARACION DE PRECISION float32 VS float64 ---")
    print(f"Valor matematico exacto : {exacto}")
    print(f"Resultado en Float32    : {res_float32:.10f} (Error absoluto: {error_float32:.2e})")
    print(f"Resultado en Float64    : {res_float64:.16f} (Error absoluto: {error_float64:.2e})\n")
    
if __name__ == "__main__":
    monto_inicial=1000000
    etiquetas, precios, errores = evaluar_ciclo_compra_venta(diccionario_dolar, monto_inicial)
    graficar_patrones(etiquetas, precios, errores)
    comparar_precision_flotante()