#EJERCICIO 10 

nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''

notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]

notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

#a) 

Nombres = nombres.replace('\n',' ').replace('\'','').strip(' ').split(',')

diccionario= {i:[j, k] for i, j, k in zip(Nombres,notas_1, notas_2)}

#b) 

promedio_ind = list(map(lambda notas:sum(notas) / 2, diccionario.values()))
    
for i, (clave, lista) in enumerate(diccionario.items()):
    lista.append(promedio_ind[i])

for lista in diccionario.values():
    print("El/la alumno/a",lista[0],"tiene promedio de", lista[2])

#c) 

promedio_total = sum(promedio_ind)/len(promedio_ind)

print('El promedio total del curso es:', promedio_total)

#d) 

max_val = max(diccionario.items(), key=lambda x: x[1][2])
print("El mayor promedio es:", max_val[1][2], "y lo tiene", max_val[0])    


#e) 

min_val = min(diccionario.items(), key=lambda x: x[1][2])
print("El menor promedio es:", min_val[1][2], "y lo tiene", min_val[0])    
