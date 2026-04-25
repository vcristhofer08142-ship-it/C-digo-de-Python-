""" # DIFERENTES MANERAS DE IMPRIMIR TEXTO

s = "hola" + "mundo"
print(s)
r = "hola" "mundo"
print(r)
t = "hola" * 3
print(t)

# sep= lo q va entre las palabras , end= lo q va al final de todo el texto
print("perro", "gato", "raton", sep="@", end="#\n") 
print("FIN")


# FORMAS DE RECIBIR UN DATO 
print("Ingrese nombre:")
nom=input()
print(f"Se llama {nom}")
print()

nom=input("Ingrese nombre:\n")
print(f"Se llama {nom}")


# CONDICIONAL Y BUCLE 

name = 'Antony'

if name == 'Debora':
   print('Hi Debora!')
elif name == 'George':
   print('Hi George!')
else:
   print('Who are you?')



spam = 0
while spam < 5:  # Continue while spam is less than 5
    print('Hello, world.')
    spam = spam + 1  # Increment counter to avoid infinite loop
    
    
for i in range(5):
    print(f'Will stop at 5! or 4? ({i})') # la "f" va para q se puede poner variables adentro del mensaje  """



""" # TIPOS DE DATOS

edad : int = 18
altura : float = 1.8
nombre : str = "Carlos"
esVerde : bool = False

print(f"{nombre} tiene {edad} años y su carro {"es" if esVerde else "no es" } verde")


# FUNCIONES  

def separa(n):
   return int(n), n-int(n)
   
def mas10(num : int):
   print(num+10)

def sum_two_numbers(number_1 : int, number_2 : int) -> int: # metodo pide las variables 
   return number_1 + number_2
result = sum_two_numbers(7, 8)
print(result)

def sum_two_numbersX(number_1 : int=3, number_2 : int=2) -> int: # no pide variables , ya estan asignadas en el metodo 
   return number_1 + number_2
result = sum_two_numbersX()
print(result)

mas10(10)
e, d = separa(10.5)
print(e,d)


# LISTA 

a = [1, 2, 3, 4]
#agregar 
a.append(5)
print(a)
a.insert(5, 7)  # primer valor indica la posición , el segundo reprenta el dato 
print(a)


#borrar
a.remove(7)
print(a)
del a[3]
print(a)

# posición 
print(a.index(5)) """





""" # DESTRUCTURACIÓN 

#  tradicional
muebles = ['mesa', 'silla', 'armario', 'estante']
m = muebles[0]
s = muebles[1]
a = muebles[2]
e = muebles[3]
print(m,s,a,e)

# moderna
m,s,a,e = ['mesa', 'silla', 'armario', 'estante']
print(m,s,a,e)



# intercambios de varialbles 
x = 10
y = 20

tmp = x
x = y
y = tmp

x,y = y,x
print(x,y)





# LISTA CON INDICE NEGATIVO Y SUBLISTA 

lista = ["Carlos", 20, 1.8, True] # se crea una lista de diferentes tipos de datos (si se puede)

print(lista[1])
lista[0] = "Beto"
print(lista)

# aceder a indice negativo : el -1 es el ultimo elemento , el -2 es el q esta a la izquierda del ultimo y asi 
print(lista[-1])
print(lista[-3])


a = [1, 2, 3, 4]
b = a[1:3] #incluir elemntos de otra lista , en sin cotar el ultimo , en este caso no cuenta el q esta en la posición 3
b[1] = 33
# a[] crea un copia de la lista a y lo asigna a la variable b 


print(b)
print(a)





# PERTENECIA in

a = [1, 2, 3, 4]
print(2 in a) # imprime true o false ; 2 pertenece a la lista a ?
print(7 in a)

# imprime la lista 
for x in a:  
    print(x)
 """



# INSERTAE ELEMENTOS EN UNA LIST CON FOR DE FORMA DIRECTA 


#lista = [ expresion FOR variables IN secuencia]
lista = [ 2*x for x in range(1,10+1)]
print(lista)

#cree una lista de los multiplos de 3 a partir de los valores del 1 al 100
lista = [x for x in range(1, 101) if x % 3 == 0] 
print(lista)

#otra mejorar
lista=[3*x for x in range(1,33+1)] 
print(lista)


# OBJETO 


"""
c#
class Perro{
    public string raza {get;set;}
    public string edad {get;set;}
    
    public Perro(){
        this.edad = 1;
    }
    public Perro(string raza){
        this.raza = raza;
        this.edad = 1;
    }
    public string ToString(){
        return $"{this.raza} de {this.edad} años"
    }
    public void Ladrar(){
        Console.WriteLine($"{this.raza} dice guau")
    }
}

Perro p = new Perro();
Perro q = new Perro("Chuguagua");
q.Ladrar()
"""
#python
class Perro:
    def __init__(self, raza = ""):
        self.raza = raza
        self.edad = 1
    def __str__(self):
        return f"{self.raza} de {self.edad} años"
    def ladrar(self):
        print(f"{self.raza} dice guau")

p = Perro()
print(p)
p.ladrar()

q = Perro("Chuguagua")
print(q)
q.ladrar()
    
