print ("\nEjercicio 2: Mi mascota en años humanos")
print ("\nMI MASCOTA")

nombre_mascota = "Mio"
tipo = "gato"
edad_mascota = 8

#Regla popular: 1 año de gato equivale a 15 años humanos
edad_humana = edad_mascota * 15

# f-string: la f permite usar {variables} dentro del texto
print (f"Mi {tipo} se llama {nombre_mascota}")
print (f"Tiene {edad_mascota} años de {tipo}")
print (f"En años humanos tendría {edad_humana} años!\n")