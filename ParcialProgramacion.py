#Elementos repetidos 
lista=[1,2,3,4,5,6,6]

for i in lista:
    a= lista.count(i)

if a !=1:
    print("Existen caracteres repetidos")
else:
    print("No existen caracteres repetidos")


#Cadena de caracteres (vocales)
cadena= ["introduccion","programacion","taller"]
a=list(cadena)
print(a)

for i in a:
    if i == "a" or 'e' or 'i' or 'o' or 'u':
        print(i)
    else:
        print("La cadena no existe")


#Elementos que no se repiten
a=[1,3,5,7]
b=[1,2,3,4]

resultado=[]

for x in a:
    if x in b:
        print("Hay elementos de la segunda lista")
    else:
        resultado.append(x)

print("Los elementos que se encuentran solo en la primera lista son: ",resultado)

#promedio
lista=[2,3,4,5,6]
suma= sum(lista)
promedio= suma/len(lista)
print("El promedio es: ",promedio)

#mediana 
a= [5,2,7,4,8,5,6]
a.sort()
x=len(a)
if x % 2 != 0:
    mediana= a[x//2]
else:
    mediana= (a[x//2+1]+a[x//2])/2
    
print("La mediana de la lista:",a,"es: ",mediana)
