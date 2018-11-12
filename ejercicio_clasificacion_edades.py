encuestados = [['Femenino', 38, 2, "Nuevo Repueblo", "de 0 a 5,000", False],
               ['Femenino', 19, 0, "Contry La silla", "de 10,000 a 15,000", False],
               ['Masculino', 22, 1, "Fomerrey 22", "de 0 a 5,000", False],
               ['Masculino', 70, 3, "Valle Verde", "de 5,000 a 7,000", True],
               ['Femenino', 57, 4, "Centro", "de 7,000 a 10,000", False],
               ['Femenino', 44, 0, "Valle Alto", "de 30,000 a 50,000", False],
               ['Femenino', 20, 2, "Burócratas Municipales", "de 5,000 a 7,000", True],
               ['Masculino', 19, 0, "Buenos Aires", "de 10,000 a 13,000", True],
               ['Femenino', 12, 0, "Obrera", "de 5,000 a 7,000", True],
               ['Masculino', 32, 3, "Contry Sol", "de 10,000 a 15,000", False],
               ['Femenino', 87, 9, "Del Paseo", "de 15,000 a 20,000", True],
               ['Femenino', 25, 1, "Roma", "de 20,000 a 25,000", False],
               ['Masculino', 65, 3, "Estadio", "de 10,000 a 15,000", True]]



rangos_edades = {"kid": (range(1,10)), "joven": (range(11,21)), "millenial": (range(21,35)), "super_adulto": (range(35,300))}


for encuesta in encuestados:
    edad=encuesta[1]
    
    if edad in rangos_edades["kid"]:
        encuesta.append("Niño")
    elif edad in rangos_edades["joven"]:
        encuesta.append("Joven")
    elif edad in rangos_edades["millenial"]:
        encuesta.append("Millenial")
    elif edad in rangos_edades["super_adulto"]:
        encuesta.append("Super_adulto")
    else:
        encuesta.append("Sin_edad")

for encuesta in encuestados:
    print(encuesta)
