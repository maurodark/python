equipo = {10 : "Pablo Divala", 7 : "Cristiano Ronaldo",  17 : "Cuadrado"}



print (equipo[10])
print (equipo.get(9, "NO exsite ese jugador"))
print (10 in equipo)
print (equipo.keys())
print (equipo.values())
print (len(equipo))

equipo.clear()
print (equipo)