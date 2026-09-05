import math

def valor_n_cifras_significativas(valor, n):
    if valor == 0:
        return 0.0
    magnitud = math.floor(math.log10(abs(valor)))
    return round(valor, n - 1 - magnitud)

# Valores crudos
p_2022_real = 875.66
p_2023_real = 874.67

# Aproximación a 3 cifras significativas
p_2022_aprox = valor_n_cifras_significativas(p_2022_real, 3)
p_2023_aprox = valor_n_cifras_significativas(p_2023_real, 3)

# Errores absolutos iniciales
ea_2022 = abs(p_2022_real - p_2022_aprox)
ea_2023 = abs(p_2023_real - p_2023_aprox)

# Calculo de la variación (Resta)
delta_p_aprox = p_2023_aprox - p_2022_aprox

# Propagacion del error
ea_total = ea_2022 + ea_2023

# Error porcentual respecto al valor de la variación exacta
delta_p_real = p_2023_real - p_2022_real
error_porcentual = (ea_total / abs(delta_p_real)) * 100

# Salida de resultados
print("--- VARIACIÓN DEL DÓLAR (3 Cifras Significativas) ---")
print(f"Precio 2022 -> Original: {p_2022_real} | Aprox: {p_2022_aprox} | Ea: {ea_2022:.2f}")
print(f"Precio 2023 -> Original: {p_2023_real} | Aprox: {p_2023_aprox} | Ea: {ea_2023:.2f}\n")

print(f"Resultado (ΔP ± error) : {delta_p_aprox:.2f} ± {ea_total:.2f}")
print(f"Error porcentual       : {error_porcentual:.2f}%")