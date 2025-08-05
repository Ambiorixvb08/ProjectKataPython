from functools import reduce
import math

# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias 
# de cada letra en la cadena. Los espacios no deben ser considerados.


def CreateDiccionary(cadena):

    frecuencia= {}

    for cad in cadena:

        if cad != " ":

            l = cad.lower()

            if l.isalpha():

                frecuencia[l] = frecuencia.get(l,0) + 1

    return frecuencia

saludo = "Hola mi nombre es ambiorix"

pruebaEjer1 = CreateDiccionary(saludo)

print("pruebaEjer1",pruebaEjer1)


# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

initList = [10,5,25,30]

dobles = list(map(lambda x: x * 2, initList))

print("dobles",dobles)


# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe
# devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.


def buscar_palabra(lista_palabras, palabra_objetivo):
    resultado = []
    palabra_objetivo = palabra_objetivo.lower()  # agrego el .lower() para que no me distinga entre mayusculas y minusculas de esta forma todas son minusculas

    for palabra in lista_palabras:
        if palabra_objetivo in palabra.lower():
            resultado.append(palabra)

    return resultado

palabras = ["Dedar", "Dedo", "Dado", "duda", "duración", "dudation"]
p_objetivo = "Duda"

pruebaEjer3 = buscar_palabra(palabras, p_objetivo)

print(pruebaEjer3)

# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

listOne = [2,5,8,7,4,3,6]
listTwo = [7,8,9,4,2,3,6,5,0]

def diferencia_listas(lista1, lista2):
    def resta(a, b):
        return a - b

    return list(map(resta, lista1, lista2))

pruebaEjer4 = diferencia_listas(listOne,listTwo)

print(pruebaEjer4)

# 5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por
# defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
# que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
# una tupla que contenga la media y el estado.

num_list = [4,5,6,7,8,9,1,3]
option_value = 5

def evaluar(numeros, default_value = 5):
    estado = "Suspenso"
    if not numeros:
        return (0, estado)

    media = sum(numeros) / len(numeros)

    if media >= default_value:
        estado = "Aprobado"

    return (media, estado)

# Ejecucion de la función

pruebaEjer5 = evaluar(num_list, option_value)

print("pruebaEjer5", pruebaEjer5)

# 6.Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial(num):
   if num < 0:
       return ValueError("El numero tiene que ser un numero positivo")
   if num == 0 or num == 1:
        return 1
   else:
    return num * factorial(num - 1)

pruebaEjer6 = factorial(10)

print("pruebaEjer6",pruebaEjer6)

# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

def converTuplaInList(tupla1):
    return list(map(lambda tupla: ", ".join(map(str, tupla)), tupla1))

datos = [(1, 2), (3, 4), ('a', 'b')]

pruebaEjer7 = converTuplaInList(datos)

print("pruebaEjer7", pruebaEjer7)

# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
# o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
# indicando si la división fue exitosa o no.

def dividir8():
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        resultado = num1 / num2
        print(f"División exitosa: {num1} / {num2} = {resultado}")
# Controlamos que los valores sean numericos
    except ValueError:
        print("Error: Debes ingresar valores numéricos.")
# Controlamos que los valores sean mayor que 0
    except ZeroDivisionError:
        print("Error: No se puede dividir entre 0.")
# Devolvemos un mensage success
    else:
        print("La operación se realizó correctamente.")
# Cerramos el programa
    finally:
        print("Fin del programa.")

pruebaEjer8 = dividir8()

print("pruebaEjer8", pruebaEjer8)


# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
# excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
# "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()


def filterAnimalList(lista_mascotas):
    lista_p = ["Mapache", "Tigre","Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda x: x not in lista_p, lista_mascotas))

animales= ["Perro", "Gato","Serpiente Pitón", "Cocodrilo", "Oso","Lagartija"]
pruebaEjer9 = filterAnimalList(animales)

print("pruebaEjer9",pruebaEjer9)

# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una
# excepción personalizada y maneja el error adecuadamente.

def promedio10(lista_num):
    try:
        if not lista_num:
            raise ValueError("La lista está vacía. No se puede calcular el promedio.")
        
        promedio = sum(lista_num) / len(lista_num)
        return promedio

    except ValueError as e:
        print(f"Error: {e}")
        return None
    

pruebaEjer10 = promedio10(num_list)

print("pruebaEjer10", pruebaEjer10)

# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
# valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones
# adecuadamente.

def PedirEdad():
    try:
        edad = float(input("Ingrese su edad: "))
        
        if edad < 0 or edad > 120:
            raise ValueError("La edad debe estar entre 0 y 120 años.")
        
        print(f"La edad introducida es {edad}")
        return edad

    except ValueError as e:
        print(f"Error: {e}")
        return None


pruebaEjer11 = PedirEdad()

print("pruebaEjer11", pruebaEjer11)

# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

def converlist(frase):
     return list(map(len, frase.split()))

frase = "Hi my name is luis and i work a hospital"

pruebaEjer12 = converlist(frase)

print('pruebaEjer12',pruebaEjer12)


# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
# mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()

def letras_mayus_minus(s):
    letras = filter(str.isalpha, s.lower())
    unicas = sorted(set(letras))
    return list(map(lambda c: (c.upper(), c.lower()), unicas))

pruebaEjer13 = letras_mayus_minus(frase)

print('pruebaEjer13',pruebaEjer13)

# 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la
# función filter()

def devolver_palabra_clave(list_word,key_word):
    return list(filter(lambda x:  key_word in x, list_word))

listaWork = ['juan','maria','pepe','luis','julio', 'luis']
keyWork= 'j'
pruebaEjer14 = devolver_palabra_clave(listaWork, keyWork)

print('pruebaEjer14',pruebaEjer14)

# 15. Crea una función lambda que sume 3 a cada número de una lista dada.

sumar_tres = lambda lista: list(map(lambda x: x + 3, lista))

pruebaEjer15 = sumar_tres(num_list)

print('pruebaEjer15',pruebaEjer15)

# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de
# todas las palabras que sean más largas que n. Usa la función filter()

def word_more_long(phrase, num):
    words = phrase.split()
    return list(filter(lambda word: len(word) > num, words))

pruebaEjer16 = word_more_long(frase,5)
print('pruebaEjer16',pruebaEjer16)

# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2]
# corresponde al número quinientos setenta y dos (572). Usa la función reduce()

def list_to_number(list_number):
    return reduce(lambda acc, d: acc * 10 + d, list_number)


pruebaEjer17= list_to_number(num_list)
print('pruebaEjer17',pruebaEjer17)

# 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
# (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a
# 90. Usa la función filter()

lista_estudiantes = [
    {'nombre': 'Juan', 'edad': 20, 'calificacion': 85},
    {'nombre': 'María', 'edad': 22, 'calificacion': 92},
    {'nombre': 'Luis', 'edad': 21, 'calificacion': 78},
    {'nombre': 'Ana', 'edad': 23, 'calificacion': 95}
]

def estudiantes_destacados(estudiantes):
    return list(filter(lambda est: est['calificacion'] >= 90, estudiantes))

pruebaEjer18 = estudiantes_destacados(lista_estudiantes)

print('pruebaEjer18',pruebaEjer18)

# 19.Crea una función lambda que filtre los números impares de una lista dada.

def filter_impar(list_number):
    return list(filter(lambda imp: imp % 2 != 0,list_number ))


pruebaEjer19 = filter_impar(num_list)
print('pruebaEjer19',pruebaEjer19)

# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función
# filter()

def search_num(list_value):
    return list(filter(lambda x: isinstance(x, int),list_value))

list_mixt = [1 , 'hola', 4, 'Gato']

pruebaEjer20 = search_num(list_mixt)
print('pruebaEjer20',pruebaEjer20)

# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda

def calcule_cub(number):
    return number ** 3

pruebaEjer21 = calcule_cub(2)
print('pruebaEjer21',pruebaEjer21)

# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() .

def producto_total(list_number):
    return reduce(lambda a, b: a * b, list_number)

pruebaEjer22 = producto_total(num_list)
print('pruebaEjer22',pruebaEjer22)

# 23. Concatena una lista de palabras.Usa la función reduce() .

def concatenar_palabras(lista_palabras):
    return reduce(lambda x, y: x + ' ' + y, lista_palabras)

pruebaEjer23 = concatenar_palabras(listaWork)
print('pruebaEjer23',pruebaEjer23)

# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() .
def diferencia_total(lista):
    return reduce(lambda a, b: a - b, lista)


pruebaEjer24 = diferencia_total(num_list)
print('pruebaEjer24',pruebaEjer24)

# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

def contar_caracteres(texto):
    return len(texto)

pruebaEjer25 = contar_caracteres(frase)
print('pruebaEjer25',pruebaEjer25)

# 26.Crea una función lambda que calcule el resto de la división entre dos números dados.

def calcular_resto(number1, number2):
    resto_division = lambda a, b: a % b
    return resto_division(number1,number2)


pruebaEjer26 = calcular_resto(10,2)
print('pruebaEjer26',pruebaEjer26)


# 27. Crea una función que calcule el promedio de una lista de números.

def promedioList(listNumber):
    promedio = sum(listNumber)/len(listNumber)
    return promedio

pruebaEjer27 = promedioList(num_list)
print('pruebaEjer27',pruebaEjer27)

# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def first_duplicate(lista):
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None

listaDuplicados= [1 ,2,1,5,4]

pruebaEjer28 = first_duplicate(listaDuplicados)
print('pruebaEjer28',pruebaEjer28)

# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el
# carácter '#', excepto los últimos cuatro.

def enmascarar_variable(variable):
    texto = str(variable) 
    longitud = len(texto)
    if longitud <= 4:
        return texto
    return '#' * (longitud - 4) + texto[-4:]

pruebaEjer29 = enmascarar_variable(frase)
print('pruebaEjer29',pruebaEjer29)

# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
# pero en diferente orden.

def anagramWord(w1, w2):
    return sorted(w1) == sorted(w2)

pruebaEjer30 = anagramWord("roma","amor")
print('pruebaEjer30',pruebaEjer30)

# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
# esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
# lanza una excepción.

def seach_name_list():
    try:
        mensaje_entrada = input("Introduzca una lista de nombres separados po comas: ")
        lista_nombre = [nombre.strip().lower() for nombre in mensaje_entrada.split(',')]
    
        nombre_buscar = input("Introduce el nombre a buscar: ").strip().lower()

        if nombre_buscar in lista_nombre:
            print(f"El nombre {nombre_buscar} fue encontrado en la lista")
            return True #he agregado este true para que la funcion no devuelva none
        else:
            raise ValueError(f'El nombre {nombre_buscar} no se ha encontrado')
    except ValueError as e:
        print("error: ", e)
        return False

pruebaEjer31 = seach_name_list()
print('pruebaEjer31',pruebaEjer31)

# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
# devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
# no trabaja aquí.

lista_empleados = [
    {'nombre': 'Juan', 'puesto': 'Responsable'},
    {'nombre': 'María', 'puesto': 'Backend'},
    {'nombre': 'Luis', 'puesto': 'Frontend' },
    {'nombre': 'Ana', 'puesto': 'FullStack'}
]
nombre= 'Luis'
def search_employee(list_employee, name_employee):
    for employee in list_employee:
        if employee['nombre'].lower() == name_employee.lower():
            return employee['puesto']
        
    return 'La persona buscada no trabaja aqui'


pruebaEjer32 = search_employee(lista_empleados, nombre)
print('pruebaEjer32',pruebaEjer32)


# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.
def sumar_elementos(lista1, lista2):
     return list(map(lambda a, b: a + b, lista1, lista2))

pruebaEjer33 = sumar_elementos(num_list, num_list)
print('pruebaEjer33',pruebaEjer33)

# 34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
# crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para
# manipular la estructura del árbol.


class Arbol:
    def __init__(self, tronco= 1 , ramas= None):
        self.tronco = tronco 
        self.ramas = ramas if ramas is not None else []   

    def crecer_tronco(self, cantidad = 1):
        self.tronco += cantidad
        print(f"El tronco ha crecido, su altura actual es {self.tronco}")
        
    def nueva_rama(self,rama):
        self.ramas.append(rama)
        print("Se agrego una nueva rama,")
        
    def crecer_ramas(self):
        self.ramas = [rama + " (crecida)" for rama in self.ramas]
        print("Todas las ramas han crecido.")
        
    def quitar_rama(self, rama):
        if rama in self.ramas:
            self.ramas.remove(rama)
            print(f"Se quitó la rama: {rama}")
        else:
            print(f"La rama '{rama}' no se encontró.")
    
    def info_arbol(self):
        print(f"Altura del tronco: {self.tronco}")
        print(f"Ramas: {self.ramas}")
        
        
        # Caso de uso:
# 1. Crear un árbol.
miArbol = Arbol()
# 2. Hacer crecer el tronco del árbol una unidad.
miArbol.crecer_tronco(5)
# 3. Añadir una nueva rama al árbol.
miArbol.nueva_rama("Primera rama")
# 4. Hacer crecer todas las ramas del árbol una unidad.
miArbol.crecer_ramas()
# 5. Añadir dos nuevas ramas al árbol.
miArbol.nueva_rama("Segunda rama")
miArbol.nueva_rama("Tercera rama")
# 6. Retirar la rama situada en la posición 2.
miArbol.quitar_rama("Segunda rama")
# 7. Obtener información sobre el árbol.
miArbol.info_arbol()


# 36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
# corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y
# agregar dinero al saldo.

class UsuarioBanco:
    def __init__(self,nombre = "",saldo = 0,tiene_cuenta_corriente= False):
        self.nombre = nombre
        self.saldo = saldo
        self.tiene_cuenta_corriente= tiene_cuenta_corriente
        
    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            print(f"No tiene suficiente saldo para retirar. Saldo actual: {self.saldo}")
        else:
            self.saldo -= cantidad
            print(f"{self.nombre} ha retirado {cantidad}. Saldo actual: {self.saldo}")
        
    def transferir_dinero(self, otro_usuario, cantidad):
        if cantidad > self.saldo:
            print(f"No tiene suficiente saldo para transferir. Saldo actual: {self.saldo}")
        else:
            self.saldo -= cantidad
            otro_usuario.saldo += cantidad
            print(f"{self.nombre} ha transferido {cantidad} a {otro_usuario.nombre}.")
            print(f"Su saldo ahora es: {self.saldo}")
            
    def agregar_dinero(self, cantidad):
        self.saldo += cantidad
        print(f"{self.nombre} ha agregado {cantidad}. Saldo actual: {self.saldo}")
        
#         Código a seguir:
# 1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False .
primer_cliente = UsuarioBanco(nombre="Antonio Vargas Garcia",saldo=3000,tiene_cuenta_corriente=True)
segundo_cliente = UsuarioBanco(nombre="Mario Vargas De la cruz",saldo=1100,tiene_cuenta_corriente=True)
# 2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de nopoder hacerse.
primer_cliente.retirar_dinero(25)
# 3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual.Lanzará un error en caso de no poder hacerse.
primer_cliente.transferir_dinero(otro_usuario=segundo_cliente,cantidad=1050)
# 4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
primer_cliente.agregar_dinero(50)


# Caso de uso:
# 1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
alicia = UsuarioBanco(nombre="Alicia",saldo=50,tiene_cuenta_corriente=True)
bob = UsuarioBanco(nombre="Bob",saldo=50,tiene_cuenta_corriente=True)
# 2. Agregar 20 unidades de saldo de "Bob".
bob.agregar_dinero(20)
# 3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
bob.transferir_dinero(otro_usuario=alicia,cantidad=80)
# 4. Retirar 50 unidades de saldo a "Alicia".
alicia.retirar_dinero(50)


# 37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras ,
# reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro
# de la función procesar_texto .
# Código a seguir:
# 1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario.
def contar_palabras(texto):
    palabras = texto.lower().split()
    conteo = {}
    for palabra in palabras:
        palabra = palabra.strip(".,;:?!")  
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo
# 2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tieneque devolver el texto con el remplazo de palabras.
def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)
# 3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.
def eliminar_palabra(texto, palabra_a_eliminar):
    palabras = texto.split()
    resultado = [palabra for palabra in palabras if palabra != palabra_a_eliminar]
    return " ".join(resultado)
# 4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un número de argumentos variable según la opción indicada.
def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        if len(args) < 2:
            raise ValueError("Se requieren dos argumentos: palabra_original y palabra_nueva.")
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        if len(args) < 1:
            raise ValueError("Se requiere al menos una palabra a eliminar.")
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError("Opción no válida. Usa 'contar', 'reemplazar' o 'eliminar'.")
# Caso de uso:
# Comprueba el funcionamiento completo de la función procesar_texto
texto_prueba = "Hi today is sunday and i am doing my homework."

# Contar palabras
resultado_contar = procesar_texto(texto_prueba, "contar")
print("Contar palabras:", resultado_contar)

# Reemplazar palabra
resultado_reemplazo = procesar_texto(texto_prueba, "reemplazar", "mundo", "planeta")
print("Reemplazo de palabras:", resultado_reemplazo)

# Eliminar palabra
resultado_eliminar = procesar_texto(texto_prueba, "eliminar", "mundo")
print("Texto con palabra eliminada:", resultado_eliminar)

# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

def reloj_dia_noche():
    try:
        hora = int(input("Introduzca una hora (0 a 23): "))
        if hora < 0 or hora > 23:
            raise ValueError("La hora debe estar entre 0 y 23.")

        if 6 <= hora < 12:
            print("Es de mañana")
        elif 12 <= hora < 20:
            print("Es de tarde")
        else:
            print("Es de noche")

    except ValueError as e:
        print(f"Error: {e}")
        
pruebaEjer38 = reloj_dia_noche()
print('pruebaEjer38', pruebaEjer38)

# 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
# Las reglas de calificación son:
# - 0 - 69 insuficiente
# - 70 - 79 bien
# - 80 - 89 muy bien
# - 90 - 100 excelente

def calificacion_texto():
    try:
        nota = float(input("Introduce la calificación numérica del alumno (0 a 100): "))

        if nota < 0 or nota > 100:
            raise ValueError("La calificación debe estar entre 0 y 100.")

        if nota < 70:
            print("Calificación: Insuficiente")
        elif nota < 80:
            print("Calificación: Bien")
        elif nota < 90:
            print("Calificación: Muy bien")
        else:
            print("Calificación: Excelente")

    except ValueError as e:
        print(f"Error: {e}")
        
pruebaEjer39 = calificacion_texto()
print('pruebaEjer39', pruebaEjer39)    

# 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o
# "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).

def calcular_area(figura, datos):
    figura = figura.lower()
    
    if figura == "rectangulo":
        if len(datos) != 2:
            return "Error: Para un rectángulo se necesitan dos datos (base, altura)."
        base, altura = datos
        return base * altura

    elif figura == "circulo":
        if len(datos) != 1:
            return "Error: Para un círculo se necesita un dato (radio)."
        radio = datos[0]
        return math.pi * radio**2

    elif figura == "triangulo":
        if len(datos) != 2:
            return "Error: Para un triángulo se necesitan dos datos (base, altura)."
        base, altura = datos
        return (base * altura) / 2

    else:
        return "Error: Figura no reconocida"
    
pruebaEjer40 = calcular_area("rectangulo", (5, 10))
print('pruebaEjer40', pruebaEjer40)

# 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
# monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo
# siguiente:
# 1. Solicita al usuario que ingrese el precio original de un artículo.
# 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
# 3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
# 4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor
# a cero). Por ejemplo, descuento de 15€.
# 5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
# 6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu
# programa de Python.

def calcular_precio_final():
    try:
        precio_original = float(input("Ingrese el precio original del artículo (€): "))

        if precio_original <= 0:
            print("El precio debe ser mayor que cero.")
            return

        tiene_cupon = input("¿Tiene un cupón de descuento? (sí o no): ").strip().lower()

        if tiene_cupon == "sí" or tiene_cupon == "si":
            valor_descuento = float(input("Ingrese el valor del cupón (€): "))
            if valor_descuento > 0:
                precio_final = precio_original - valor_descuento
                if precio_final < 0:
                    precio_final = 0  # Evitar precios negativos
                print(f"Descuento aplicado: -{valor_descuento:.2f}€")
                print(f"Precio final con descuento: {precio_final:.2f}€")
            else:
                print("El cupón no es válido. Se cobrará el precio completo.")
                print(f"Precio final: {precio_original:.2f}€")

        elif tiene_cupon == "no":
            print(f"No se aplicó descuento. Precio final: {precio_original:.2f}€")

        else:
            print("Respuesta no válida. Por favor, responda 'sí' o 'no'.")

    except ValueError:
        print("Error: Ingrese solo números válidos para el precio y el descuento.")

pruebaEjer41 = calcular_precio_final()
print('pruebaEjer41',pruebaEjer41)
