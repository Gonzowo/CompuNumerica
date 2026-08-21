#############################################
# Prueba punto flotante Computacion Numerica#
# Gonzalo Cerpa Salas 21/08/2026            #
#############################################


#######
# Numero entero a decimal en base 10
x = input("")
cifras_significativas = len(x) - 1
B = 10
aux_x = float(x) / (10**cifras_significativas)

#Salida
salida = {
    "A": aux_x,
    "B": B,
    "C": cifras_significativas,
    "X": x
}
print(salida)
#######