###################################
# Calculo de Error Absoluto y     #
# Error Relativo (%)              #
# a partir de CifrasSignificativas#
###################################

"""
Este script IMPORTA el archivo CifrasSignificativas.py (debe estar en la
misma carpeta que este script) y reutiliza su funcion
dos_cifras_significativas(valor), que ya entrega:

    valor_aproximado, error_absoluto = dos_cifras_significativas(valor)

A partir de eso, este script calcula ademas el ERROR RELATIVO PORCENTUAL:

    Ea = valor_verdadero - valor_aproximado      (error absoluto, con signo)
    Er = (Ea / valor_verdadero) * 100            (error relativo porcentual)
"""

import csv
import os

# Importamos el modulo con la logica de cifras significativas
import CifrasSignificativas as cs


def calcular_errores(valor_verdadero: float):
    """
    Usa dos_cifras_significativas() de CifrasSignificativas.py para obtener
    el valor aproximado, y calcula:
        - Ea: error absoluto (valor_verdadero - valor_aproximado)
        - Er: error relativo porcentual (Ea / valor_verdadero) * 100

    Retorna: (valor_aproximado, Ea, Er)
    """
    valor_aproximado = cs.dos_cifras_significativas(valor_verdadero)

    Ea = valor_verdadero - valor_aproximado

    if valor_verdadero != 0:
        Er = (Ea / valor_verdadero) * 100
    else:
        Er = float("nan")  # division por cero no definida

    return valor_aproximado, Ea, Er


def main():
    # Reutilizamos el nombre de archivo y la columna definidos en
    # CifrasSignificativas.py, para no repetir configuracion
    carpeta_script = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(carpeta_script, cs.NOMBRE_ARCHIVO)

    if not os.path.isfile(ruta_archivo):
        print(f"ERROR: no se encontro el archivo en: {ruta_archivo}")
        return

    with open(ruta_archivo, newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        filas = list(lector)

    print(f"{'Periodo':<15}{'Valor':>10}{'Aprox.':>10}{'Ea':>10}{'Er (%)':>10}")
    print("-" * 55)

    for fila in filas:
        valor = float(fila[cs.COLUMNA])
        aprox, Ea, Er = calcular_errores(valor)
        periodo = f"{fila['anio']}-{fila['mes']}"
        print(f"{periodo:<15}{valor:>10.2f}{aprox:>10.2f}{Ea:>10.2f}{Er:>9.2f}%")


if __name__ == "__main__":
    main()