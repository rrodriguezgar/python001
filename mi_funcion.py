def preguntar_nombre():
    nombre:str=input("¿Cual es tu nombre?")
    print ("Hola", nombre)
    return


#print(preguntar_nombre())


def calcular_media(*args):
    total=0
    for i in args:
        total+=i
    resultado_media = total/len(args)
    return resultado_media

a,b,c,d=5,10,15,20
media=calcular_media(a,b,c,d)
print(media)

def test_kwargs(**kwargs):
    for clave, valor in kwargs.items():
        print('{0}={1}'.format(clave, valor))
        

kwargs={'diez':10, 'veinte':20}

test_kwargs(**kwargs)

def crear_lista(n):
    lista=[]
    for i in range(n):
        lista.append(i)
    return lista

print(crear_lista(10))

#lambda
def multiplicar(x,y):
    return x*y

print(multiplicar(2,4))

print(f"{(lambda x, y: x*y)(10,2)}")