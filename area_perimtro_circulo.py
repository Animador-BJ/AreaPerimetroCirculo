# Programa para calcular el area y el perimetro de un circulo de radio R

import math  

# input
print("--------------------------------------")
R = input ("Ingrese el valor delradiodel cirrcuulo: ")
R = int(R)

# processing
A = math.pi*R*R
P = 2*math.pi*R

# output
print ("--------------------------------------")
print ("El área delcirculo es: " + str(A))
print ("El perimetro del circuloes: " + str(P))
print ("--------------------------------------")