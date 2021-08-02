class mult_matriz:
    def __init__(self,a,b):
        self.a = a
        self.b = b


    def revise_data(self,m,n,i,j):
        if n != i :
            pass
        else:
            print('se puede multiplicar las matrices')


m=int(input('ingrese m: '))
n=int(input('ingrese n: '))
p=int(input('ingrese p: '))
q=int(input('ingrese q: '))

#Crear matriz 1
matriz1=[]
for i in range (1,m+1):
    matriz1.append([0]*n)
    print (matriz1)
print()

#Crear matriz 2
matriz2=[]
for i in range (1,p+1):
    matriz2.append([0]*q)
print (matriz2, end='print()')
print()

mult_matriz.revise_data(0,3,4,4,3)

