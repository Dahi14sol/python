calificaciones = [1,2,3,4,5]
nombre = ["Moises","Camila","Fernanda", "Pablo","Tania"]
lista_variada = [True,  10.5, "abc", [0,1,1]]

print("estudiante", nombre[2])
print("calificacion", calificaciones[2])
print("lita dentro de otra", lista_variada[3][0] )
print("imprimir un rango o slices", nombre[1:2])
print(lista_variada)

#agregar elementos a una lista 
nombre.append("Anibal")
print(nombre) 
#remover elementos de una lista
nombre.remove("Camila")
print(nombre)