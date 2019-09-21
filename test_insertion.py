from insertion import sort
file = input("Indique la ubicacion del archivo: ")
f=open(file, "r")

A = []
f1 = f.readlines()
for line in f1:
	A.append(int(line))

print("Antes -> "+str(A))
sort(A, len(A) )
print("Despues -> "+str(A))