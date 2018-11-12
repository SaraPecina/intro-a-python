import numpy as np

nombres = ['María del Rosario Estupiñan Hernández',
    'Ana Gabriela Martinez Martinez',
    'Gabriela Muñoz Pérez',
    'Claudia González Aguirre',
    'Denise Martínez Garcia',
    'Ana Karenina Macías Flores',
    'Roberta Pulido Díaz',
    'Yolanda Eréndira Ibarra Márquez',
    'Carmen Ochoa Escandón',
    'Josefina Salinas Martínez',
    'Hilda María Bañuelos Cortés',
    'Eunice Romero Garza',
    'María Margadalena Sanchez Sanchez',
    'Ana Carolina Junco Treviño',
    'Paula Ivette Durán Rosas',
    'Sandra Maldonado Barrón',
    'Amparo Armendáriz Ruiz',
    'Nadia Leticia Carranza Téllez',
    'Cinthia Ontiveros Garza']

#Creación de listas vacias
primer_nombre = []
apellidos = []
nombres3 = []


#Separación por columnas dependiendo de la longitud
for nombre in nombres:
    nombre2 = nombre.split(" ")  #Aquí se separan con comas los nombres
    if (len(nombre2)) == 3:   #Revisé la base de datos para ver la composición de nombres, esto no funcionaría para apellidos compuestos o con un solo apellido.
        primer_nombre.append(nombre2[0])
        apellidos.append(nombre2[1]+ " " + nombre2[2])
        nombre3 = [[nombre2[0]], [nombre2[1] + " " + nombre2[2]]]
        nombres3.append(nombre3)


    elif (len(nombre2)) ==4:
        primer_nombre.append(nombre2[0]+ " " + nombre2[1])
        apellidos.append(nombre2[2]+ " " + nombre2[3])
        nombre3 = [[nombre2[0] + " " + nombre2[1]], [nombre2[2] + " " + nombre2[3]]]
        nombres3.append(nombre3)

    elif (len(nombre2)) == 5:
        primer_nombre.append(nombre2[0]+ " " + nombre2[1]+ " " + nombre2[2])
        apellidos.append(nombre2[3]+ " " + nombre2[4])
        nombre3 = [[nombre2[0] + " " + nombre2[1] + " " + nombre2[2]], [nombre2[3] + " " + nombre2[4]]]
        nombres3.append(nombre3)


#Impresiones de listas
print("\n Lista de Nombres\n")
for prim_nom in primer_nombre:
    print(prim_nom)

print("\n Lista de apellidos\n")
for apellido in apellidos:
    print(apellido)

print("\n Lista de nombres completos\n")
for nomb3 in nombres3:
    print(nomb3)
