import numpy as np

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
               ['Masculino', 65, 3, "Estadio", "de 10,000 a 15,000", True], ]
rango_de_edades = { "joven": [10, 19],
                    "millenial": [20, 35],
                    "super adulto": [36, 300],
                    }

#Podemos ver que tenemos 2 bases de datos. La primera es una lista de liistas y la segunda un diccionario.
#Reto facil (Mayor a 20=no joven, menor o igual a 20, joven)


#Creamos un ciclo. Para la vuelta n, encuesta regresara el primer elemento de encuestados.
for encuesta in encuestados:
    if encuesta[1]>20: #En este caso, encuesta[1] es el segundo elemento de la encuesta n, en este caso esa es la edad.
        encuesta.append("No joven")
    else:
        encuesta.append("Joven")
    print(encuesta)
print('\n')
#Reto dificil, usar diccionario.
#En este caso lo que hago es extraer las llaves del diccionario y guardarlas en una variable.
rango=list(rango_de_edades.keys())
print(rango)
print('\n')
#Ahora se repite el mismo caso excepto que se ponen mas condiciones en el if.
for encuesta in encuestados:

    #encuesta 1 es el segundo elemento del renglon n, la edad.
    #rango[0] es la primera llave, por lo que rango_de_edades[rango[0]]=rango_de_edades['joven']=[10, 19]
    #Entonces rango_de_edades[rango[0]][0]=10 y rango_de_edades[rango[0]][1]=19

    if encuesta[1] >= rango_de_edades[rango[0]][0] and encuesta[1] <= rango_de_edades[rango[0]][1]:
        encuesta.append(rango[0])
    elif encuesta[1] >= rango_de_edades[rango[1]][0] and encuesta[1] <= rango_de_edades[rango[1]][1]:
        encuesta.append(rango[1])
    elif encuesta[1] >= rango_de_edades[rango[2]][0] and encuesta[1] <= rango_de_edades[rango[2]][1]:
        encuesta.append(rango[2])
    else:
        encuesta.append('bebe')
    print(encuesta)
