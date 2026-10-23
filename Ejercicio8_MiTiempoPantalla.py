print ("\n★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★")
print ("Ejercicio 8: Mi tiempo de pntalla")
print ("★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ TIEMPO DE PANTALLA ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★")
#Damos de alta la variable app y las horas que paso al día
app = "TikTok"
horas_diarias = 2
print (f"\nPaso {horas_diarias} horas diarias en {app}")

#Calculamos las horas al año, esta formula dice: horas_anio = 2 * 365
horas_anio = horas_diarias * 365
print (f"Al año son {horas_anio} horas")

#Converimos las horas a días completos (1 día tieme 24 horas)
#Esta formula dice: dias_anio = 730 / 24, que da 30.4166667
dias_anio = horas_anio / 24
#El :.1f muestra solo 1 decimal, así que se ve 30.4
print (f"¡Eso equivale a {dias_anio:.1f} días completos sin parar!")

#Calculamos cuántos meses con (un mes tiene aprox. 30 días)
#Esta formula dice: meses = 30.4 / 30
meses = dias_anio / 30
print (f"\nO sea, caso {meses:.1f} meses de mi año se van en {app}\n")
print ("★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★")