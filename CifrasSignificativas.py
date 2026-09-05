###################################
# Laboratorio Evaluado n°1        #
# Gonzalo Cerpa Salas 21/08/2026  #
###################################

import csv
import math

# --- Configuracion ---
NOMBRE_ARCHIVO = 'dolar_observado_sii_2022_2025.csv'
COLUMNA = "dolar_observado_promedio_clp"


def dos_cifras_significativas(valor: float):
    """
    Transforma `valor` a su version de 2 cifras significativas (base 10).
    Unicamente realiza la transformacion; el calculo de errores se hace
    en Errores.py.
    """
    signo = -1 if valor < 0 else 1
    x = abs(valor)

    # Exponente n tal que 1 <= x / 10**n < 10
    n = math.floor(math.log10(x))

    # Mantisa completa (entre 1 y 10), redondeada a 1 decimal
    mantisa = round(x / (10 ** n), 1)

    # Caso borde: 9.96 -> 10.0, hay que subir el exponente
    if mantisa >= 10:
        mantisa = 1.0
        n += 1

    valor_aproximado = signo * mantisa * (10 ** n)
    valor_aproximado = round(valor_aproximado, max(0, -n + 6))  # limpia floats

    return valor_aproximado


def main():
    with open(NOMBRE_ARCHIVO, newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            valor = float(fila[COLUMNA])
            aprox = dos_cifras_significativas(valor)
            print(f"{fila['anio']}-{fila['mes']}: {aprox}")


if __name__ == "__main__":
    main()