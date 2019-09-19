A = [5,4,3,2,8,9,13,56,1,4,7,-1]

file = input("Indique la ubicacion del archivo: ")
f=open(file, "r")

A = []
f1 = f.readlines()
for line in f1:
	A.append(int(line))

def sort(arr, n):
	for i in range(1,n):
		x = arr[i]
		j = i-1
		while j>=0 and x<arr[j]:
			arr[j+1] = arr[j]
			j-=1
		arr[j+1] = x

print(A)
sort(A, len(A) )
print(A)