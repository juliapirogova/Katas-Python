#1. Funcion que recibe una cadena y devuelve un diccionario con las frecuencias de letras sin tener en cuenta espacio
frase = "Hola, caracola, cocacola"

def contar_letras (cadena):
    """_Es una función para contar letras en una cadena. Ignora los espacios.

    Args:
        cadena (str): la cadena de texto en la que vamos a contar las letras

    Returns:
       dict: diccionario letra-frecuencia

    """
    
    diccionario = {}
    for letra in cadena: 
      if letra != ' ':
       letra = letra.lower () #para eleminar las mayusculas
       diccionario [letra]= diccionario.get (letra, 0) + 1

    return diccionario

contar_letras (frase)


#2. Dada una lista, hay que obtener el doble usando map()
numeros = [1,4,5,3,8,9,15, 38, 11, 1356]
def doble (numero):
    """Es una funcion que coge un n''umero y devulve el doble

    Args:
        numero (int, float): un numero a doblar

    Returns:
        int, float: el doble del numero inicial
    """
    return numero * 2
resultado_map = map (doble, numeros)
nueva_lista = list (resultado_map) #lo convertimos en una lista
print (f' el resultado es' , nueva_lista)

#3. Funcion que toma una lista de palabras y una palabra objetivo y devuelve una nueva lista con palabras que contengan palabra objetivo
def buscar_palabra (lista_palabras, palabra):
    """Es una funcion que busca coincidencias de palabra base con las palabras de una lista

    Args:
        lista_palabras (list): una lista de palabras
        palabra (str): _palabra base

    Returns:
        _list: _devuelve una lista nueva con palabras que contengan la palabra base
    """
    lista_nueva = []
    for palabra in lista_palabras:
        if palabra_base in palabra:
            lista_nueva.append (palabra)
    return lista_nueva

lista_ejecutar = ["loca", "manzana", "roca", "palabra", "fresa", "provoca"]
palabra_base = "oca"

buscar_palabra(lista_ejecutar, palabra_base)
#4. funcion que calcula la diferencia entre valores de dos listas. usar map()

def diferencia (numero1, numero2):
    """_Funcion que calcula la diferencia entre dos numeros

    Args:
        numero1 (_int, float_): numero 1
        numero2 (_int, float): numero 2

    Returns:
        _int, float: la diferencia entre numero 1 y numero 2
    """

    resultado = numero1 - numero2
    return resultado

lista1 = [78, 34, 67, 59, 45, 20]
lista2 = [61, 25, 97, 59, 34, 19]

diferencia_listas = map (diferencia, lista1, lista2)
resultado = list(diferencia_listas)
print (resultado)

#5. Funcion que toma una lista de numeros y un valor opcional nota_aprobado (5). calcula la media, determina si  es mayor o igual que nota aprobado. Devuelve una tupla con nota media y estado.

def evaluar_aprobado (lista, nota_aprobado = 5):
    """Es una funcion que evalua una lista de notas y devuelve una tupla con la media de las notas y el estado (aprobado/no aprobado)

    Args:
        lista (_list): _lista de notas
        nota_aprobado (int, optional): _la nota de aprobado. Defaults to 5.

    Returns:
        _tupla: _tupla con nota media y el estado
    """
    media =  sum (lista)/ len (lista)
    estado = "aprobado" if media >= nota_aprobado else "no aprobado"
    return (media, estado)

lista_notas = [3,5,7,8,8,9,2,1,9,3]

evaluar_aprobado (lista_notas)

#6. Funcion que calcula factorial de un numero de manera recursiva
def factorial(x):
    """_Es una funcion que calcula el factorial de un numero de manera recursiva

    Args:
        x (_int): un numero

    Returns:
        _int: _el factorial del numero inicial
    """
    if x == 0 or x == 1:
        return 1 #el factorial de 1 y de 0 es 1 por convencion
    else: 
     return x * factorial(x - 1)

#7. Funcion que convierta una lista de tuplas a una lista de str usando funcion map ()

def tupla_a_str (tupla):
    """_Es una funcion que convierta una tupla a un str

    Args:
        tupla (_tuple_): _una tupla con la que vamos a trabajar

    Returns:
        _str_: devuelve un str
    """
    resultado = str(tupla)
    return resultado

tupla = ("mama", "yo", "te", "quiero", "mucho")
prueba = list (map (tupla_a_str, tupla)) #la funciion map() nos devuelve una lista de str a partir de una tupla
prueba
#8. Programa que pide 2 numeros y los divide. manejar el error de valor no numerico o 0.Division exitosa o no

try:
 numero1 = int(input("Ingrese un número: "))
 numero2 = int(input("Ingrese otro número: "))
 print("Los números ingresados por el usuario son:", numero1, ',', numero2)    
 resultado = numero1 / numero2
  
 print(f"El resultado de la división es: {round(resultado, 2)}. La division ha sido exitosa.")  

except ValueError:
    print("Por favor, ingrese un número válido. No se ha podido dividir exitosamente")   
   
except ZeroDivisionError:
    print("No se puede dividir entre cero.")

# 9. funcion que de la lista de nombres de mascotas devuelve una lista exluyendo las prohibidas en España. usar filter()

def mascotas (mascota):
    """Una funcion que comrara un elemento de la lista con otra lista con mascotas prohibidas en Espa;a.
      Devuelve una nueva lista excluyendo las prohibidas.

    Args:
        mascota (_str): nombre de una mascota_

    Returns:
        str_: _mascotas que no esten en la lista de prohibidos
    """
    lista_prohibidos = ["Mapache", "Tigre", "Serpiente Piton", "Cocodrilo", "Oso"]
    return mascota not in lista_prohibidos

lista_mascotas = ["Conejo", "Gato", "Mapache", "Oso", "Perro", "Serpiente"]

resultado = filter(mascotas, lista_mascotas)
print(list(resultado))
#10. funcion que calcula promedio de una lista. manejo de ZeroDivisionError
def calcular_promedio (lista_numeros): 
    """_Es una funcion que calcula el promedio de todos los numeros de una lista. 
    Si la lista esta vacia, devulve el mensaje que no se puede hacer la operacion.

    Args:
        lista_numeros (_list): _lista a calcular

    Returns:
        _float_: _el promedio de todos los numeros de la lista
    """

    try:
        return sum(lista_numeros)/len(lista_numeros)
    except ZeroDivisionError:
       print (f'La lista está vacia y no se puede calcular el promedio')

numeros = [2,4,6,8,4,9,10,15]
calcular_promedio(numeros) # devuelve 7.25
lista_vacia = []
calcular_promedio(lista_vacia) #devuelve el mensaje que no se puede calcular

# 11.Programa que pida la edad. manejo de errores de rango

try:
    edad = int(input("Por favor, escriba su edad:"))
    if 0 <= edad <= 120:
     print ("Su edad es ", edad)
    else:
     print ("La edad no es valida")

except ValueError: 
 print (f'Debes introducir una edad valida')

#12. funcion que recibe una frase y devuelve una lista con longitud de cada palabra. map()

import string
def longitud_palabra (frase):
    """_Es una funcion que recibe una frase, la divide en palabras, elimina los signos de puntuacion y calcula la longitud de palabras.

    Args:
        frase (cadena de str): _una frase para calcular la longitud de palabras

    Returns:
        _list: _una lista con la longitud de cada palabra de la frase dada
    """
 # He buscado c'omo mejoras la funcion y eleminar los signos de puntuacion de la frase. 
 #Para ello tenia que importar un modulo adicional string.
    frase_sin_puntuacion = ''.join(c for c in frase if c not in string.punctuation)
    palabra = frase_sin_puntuacion.split()
    longitud = list(map(len, palabra))
    return longitud

frase_evaluar = "Hola. Hoy es un dia perfecto para ver Stranger Things."
resultado = longitud_palabra(frase_evaluar)
print(resultado) # [4, 3, 2, 2, 3, 8, 4, 3, 8, 6]

#13. Funcion que para un conjunto de caracteres devuelve una lista de tuplas con mayuscula y minuscula. usa map()
def letra_ma_y_mi (letra):
    """Es una funcion que coge una letra y la devuelve en mayuscula y minuscula

    Args:
        letra (_str): _deuna letra

    Returns:
        _str_: letra en mayuscula y minuscula
    """
    return (letra.upper(), letra.lower())

set_prueba = {"a", "c", "T", "M", "J", "s"} #ya que es un set, no acepta repeticiones
resultado = list(map(letra_ma_y_mi, set_prueba))
print(resultado)

#14. Funcion que retorna palabras en una lista de palabras que empiezan con la misma letra . usa filter()
# esta funcion me ha parecido bastante dificil, tuve que buscar metodo startwith() y hacerlo con lambda

def palabras_con_letra(lista_palabras, letra):
    """_Es una funcion que de una lista de palabras devuelve otra lista en la que todas las palabras empiezan con la misma letra.

    Args:
        lista_palabras (_list): _lista con palabras
        letra (_str_): letra con la que empiezan las palabras

    Returns:
        _list_: lista con palabras que empiecen con la misma letra
    """
    resultado = list(filter(lambda palabra: palabra.lower().startswith(letra), lista_palabras)) #añadí un metodo para no depender de mayusculas
    return resultado

lista_palabras = ["mar", "gaviota", "libro", "leer", "moda", "letra", "ladrar", "Limon", "tele"]
palabras_con_letra(lista_palabras, "l")

#15. Funcion lambda que sume 3 a cada numero de la lista dada

def sumar_tres(lista):
    """_Es una funcion que suma 3 a cada numero de una lista

    Args:
        lista (_list): _lista de numeros

    Returns:
        _list: _nueva lista de numeros duspues de sumar 3
    """
    resultado = list(map(lambda numero: numero + 3 , lista))
    return resultado

lista_numeros = [7, 9, 4, 56, 903, 10045]
sumar_tres(lista_numeros)

#16. Funcion que toma una cadena de texto y numero n y devuelve una lista de palabras mas largas que n. usar filter()
def palabras_mas_largas (cadena, n):
    """Es una funcion que coge una cadena de texto, lo convierte en una una lista y luego filtra las palabras por su longitud.
Devuelve una lista con las palabras que coinciden con el criterio.
ARGS:
cadena (str): una frase
n (int): numero de letras
    Returns:
        _list: _lista palabras 
    """
    lista_cadena = list(cadena.split())
    resultado = list(filter(lambda palabra: len(palabra) > n, lista_cadena))
    return resultado

frase = "Mi personaje favorito de Stranger Things es Steve"
palabras_mas_largas(frase, 5)

#17. Funcion que toma una lista de digitos y devuelve el numero correspondiente. usar reduce()
from functools import reduce #tuve que importar reduce() antes de usarlo para mis katas

def digitos_a_numero (lista):
    """_Es una funcion que convierte digitos en un numero.

    Args:
        lista (_list): _lista de digitos

    Returns:
        _int_: _un numero 
    """
    resultado = reduce(lambda x,y: x * 10 + y, lista)
    return resultado

lista = [3,7,8]
digitos_a_numero(lista)

#18. crear una lista de diccionarios datos de estudiantes y filtrar por calificacion >=90.
lista_estudiantes = [
    {"nombre": "Pedro", "edad": 23, "calificacion": 15},
    {"nombre": "Ana" , "edad": 25, "calificacion": 95 },
    {"nombre": "Antonio" , "edad": 20, "calificacion": 56 },
    {"nombre": "Paco" , "edad": 19 , "calificacion": 89 },
    {"nombre": "Irene" , "edad": 21, "calificacion": 90},
    {"nombre": "Magdalena" , "edad": 23, "calificacion": 100 } 
    ]

estudiantes_alta_calificacion = list(filter(lambda estudiantes: estudiantes["calificacion"]>=90, lista_estudiantes))
print (estudiantes_alta_calificacion)

#19. una función lambda que filtre los números impares de una lista dada
lista_numeros =[1,7,9,8,67,546,3,90]
numeros_impares = list(filter(lambda x: x % 2 !=0, lista_numeros))
print (numeros_impares)

#20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa filter()

lista_int_str = ["a", 4, 5, "f", 45, "e", 6]
solo_int = list(filter (lambda x: type(x)== int, lista_int_str))
print(solo_int)

#21. Crea una función que calcule el cubo de un número dado mediante una función lambda

cubo_numero = lambda x: x**3
print(cubo_numero(5))

#22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa reduce().
lista_numeros = [3,5,7,8,2,34,5]
producto_total = reduce (lambda x,y: x*y, lista_numeros)
print(producto_total)

#23. Concatena una lista de palabras.Usa reduce().

lista_palabras = ["Locky", "es", "un", "villano", "y", "tambien", "un", "heroe"]
cadena_texto = reduce (lambda x,  y : x + " " + y, lista_palabras)
print (cadena_texto)

#24.Calcula la diferencia total en los valores de una lista. Usa reduce().
lista_numeros = [999, 876,4,35, 21,9,]
diferencia_total = reduce(lambda x, y : x - y, lista_numeros)
print (diferencia_total)

#25.  Crea una función que cuente el número de caracteres en una cadena de texto dada.
cadena_texto = "Eres de Marvel o de DC?"
def contar_caracteres(cadena):
 return len(cadena)

contar_caracteres(cadena_texto)

#26. Crea una función lambda que calcule el resto de la división entre dos números dados.

resto_division = lambda x, y: x % y 
resto_division ( 37, 7 )

#27. Crea una función que calcule el promedio de una lista de números.

def promedio_lista(lista):
    """_Es una funcion que calcula promedio de una lista de numeros

    Args:
        lista (_list): _una lista de numeros

    Returns:
        _float_: _promedio
    """
    promedio = round (sum(lista)/len(lista), 2)
    return promedio

lista_numeros = [4,4,8,8]
promedio_lista(lista_numeros)

#28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
def elemento_duplicado(lista):
    """_Es una funcion que busca el primer duplicado en una lista_

    Args:
        lista (list_): _duna lista

    Returns:
        _int, float, str_: _del primer duplicado
    """
    vistos = [] #creamos una lista vacia para agregar elementos que encontramos por primera vez alla
    for elemento in lista:
        if elemento in vistos:
            return elemento #nos devuelve el primer elemento repetido 
        else:
            vistos.append(elemento) #agregamos el elemento a una lista 

lista_duplicados = [3,6,8, "a" ,4,3,8,9, "f","r"]
elemento_duplicado(lista_duplicados)

#29. función que convierta una variable en cadena de texto y enmascare los caracteres con '#', excepto los últimos cuatro.

def ocultar(variable):
    """_Es una funcion que coge una variable y enmascara todos los caracteres con "#" menos los ultimos 4

    Args:
        variable (_str, int, float): _lo que vamos a enmascarar

    Returns:
        _str_: _el mensaje enmascarado
    """
    cadena = str(variable)
    return "#" * (len(cadena) - 4) + cadena[-4:] # va a reemplazar todo por # menos los ultimos 4. 

x = "Mi nobre es Ron Weasley"
ocultar(x)

#30. Crea una función que determine si dos palabras son anagramas

def anagramas(palabra1, palabra2):
    """Una funcion que devuelve True or False si las palabras son anagramas

    Args:
        palabra1 (_str): palabra1
        palabra2 (_str_): palabra2

    Returns:
        _bool_: _True o False
    """
    p1 = palabra1.lower() #que todas las letras sean minuscula
    p2 = palabra2.lower()

    return sorted(p1) == sorted (p2)

palabra1 = "amor"
palabra2 = "Roma"

anagramas(palabra1, palabra2)

#31. función que solicita ingresar una lista de nombres y luego solicite un nombre para buscar. Si está, se imprime fue encontrado, si no, excepción.
try:
    nombres = input("Dame nombres separados por comas")
    lista_nombres= [nombre.strip().lower for nombre in nombres.split(",") if nombre.strip()]  # limpiamos espacios y lo hacemos todo en minuscula
    nombre_a_buscar = input("Escribe un nombre para buscar en la lista").strip().lower()
    if nombre_a_buscar in lista_nombres:
       print (f'el nombre "{nombre_a_buscar}" fue encontrado en la lista')
    else:
       lista_nombres.index(nombre_a_buscar) #para que lance una excepcion

except ValueError:
 print(f"El nombre no esta en la lista")
#32 función que toma un nombre completo y una lista de empleados, lo busque y devuelve el puesto, de lo contrario, devuelve un mensaje que la persona no trabaja aquí

def empleado_puesto(nombre, lista):
    for empleado in lista: #porque tenemos una lista de diccionarios
        if empleado ["nombre"] == nombre:
            return f"El empleado '{empleado ["nombre"]}' trabaja como '{empleado ["posicion"]}' "
            
    return f"La persona {nombre} no trabaja en esta empresa"
lista_empleados = [
    {"nombre": "Francisco Delgado", "posicion": "limpiador"},
    {"nombre": "Pedro Pascal", "posicion": "gerente"},
    {"nombre": "Antonio Banderas", "posicion": "pintor"}
]

empleado_puesto("Antonio Banderas", lista_empleados )
#33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.
lista1 = [1,5,7,5,34,98]
lista2 = [90, 98,54,2,4,100]

suma_listas =  list(map(lambda x, y: x + y, lista1, lista2))
suma_listas
#34 clase arbol

class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []
    

    def crecer_tronco(self):
        self.tronco +=1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        for elemento in range(len(self.ramas)):
           self.ramas[elemento] += 1

    def quitar_ramas(self, posicion):
        self.ramas.pop(posicion - 1)

    def info_arbol (self):
        return {
            "Longitud tronco": self.tronco,
            "Numero ramas" : len(self.ramas),
            "Longitud ramas": self.ramas
        }
    



abedul = Arbol()
abedul.crecer_tronco()
abedul.nueva_rama()
abedul.crecer_ramas()
abedul.nueva_rama()
abedul.nueva_rama()
abedul.quitar_ramas(2)
info_abedul = abedul.info_arbol()
print (info_abedul)
#36. clase Usuario_banco
class Usuario_banco:

    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente 

    def retirar_dinero(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
        else: 
            raise ValueError(f' No se puede retirar {cantidad}. Saldo insuficiente.')

    def transferir_dinero(self, otro_usuario, cantidad):
        if not otro_usuario.cuenta_corriente or not self.cuenta_corriente:
            raise ValueError(" No se puede realizar la operación. Los usuarios no tienen cuentas corrientes.")
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} no tiene suficiente saldo para transferir {cantidad}.")
        
        self.saldo -= cantidad
        otro_usuario.saldo += cantidad

    def agregar_dinero(self, cantidad):
        self.saldo += cantidad

    def info (self):
        return f"👤 {self.nombre} | 💰 Saldo: {self.saldo} | 🏦 Cuenta corriente: {self.cuenta_corriente}"

Alicia = Usuario_banco("Alicia", 100, True)
Bob = Usuario_banco("Bob", 50, True)

Bob.agregar_dinero(20)
Bob.transferir_dinero(Alicia, 80) #no se puede hacer la operacion porque falta saldo
Alicia.retirar_dinero(50)

Alicia.info()

#37. Funcion procesar_texto

def contar_palabras(texto):
    frecuencia = {}
    palabras = texto.lower().strip().split() #que cada palabra empiece con minuscula, eleminar caracteres especiales y dividir texto en palabras
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra,0) + 1 #lo mismo que hicimos en el ejercicio 1
    return frecuencia

texto = "Contenía una flauta de madera toscamente trabajada. Era evidente que Hagrid la había hecho para Harry. Sopló y la flauta emitió un sonido parecido al canto de la lechuza. El segundo, muy pequeño, contenía una nota: “Recibimos tu mensaje y te mandamos tu regalo de Navidad. De tío Vernon y tía Petunia”. Pegada a la nota estaba una moneda de 50 peniques. - Qué detalle. - comentó Harry. Ron estaba fascinado con los 50 peniques." 

contar_palabras(texto)

import re
def reemplazar_palabra(texto, palabra_original, palabra_nueva):
    palabra_a_cambiar = r'\b' + re.escape(palabra_original) + r'\b'
    
    resultado = re.sub (texto, palabra_a_cambiar, palabra_nueva) #he buscado este metodo porque antes lo habia hecho con replace(), pero no respetaba los limites de la palabra y me cambiaba partes de otras parabras
    return resultado

reemplazar_palabra("de", "lechuza", texto)

def eliminar_palabra(texto, palabra_eliminar): #es muy parecido al anterior, solo que en vez de otra palabra vamos a utilizar ""
    palabra_eliminada = r'\b' + re.escape(palabra_eliminar) + r'\b'
    resultado = re.sub (palabra_eliminada, "", texto) 
    return resultado

eliminar_palabra(texto, "flauta")  
def procesar_texto(opcion, texto, *args):
    """
    opcion: tipo de funcion ('contar', 'reemplazar', 'eliminar')
    texto: texto a procesar
    *args: argumentos segun la opcion
    """
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        return reemplazar_palabra( texto, *args)
    elif opcion == "eliminar":
        return eliminar_palabra( texto, *args)
    else:
        return "Esta opcion no existe. Usa: 'contar', 'reemplazar' o 'eliminar'."
procesar_texto("contar", texto)
procesar_texto("reemplazar", texto, "de", "lechuza")
procesar_texto ("eliminar", texto, "flauta")

#38. Programa que pide la hora al usuario y dice que momento del dia es

def parte_del_dia():
    """Es una funcion que pide al usuario la hora y devuelve que parte del dia es
    """
    hora = int(input("Ingresa la hora actual (de 0 a 23): "))
    if hora < 0 or hora > 23:
        print(" Por favor, ingresa una hora válida")
    elif 6 <= hora < 12:
        print(" Es mañana")
    elif 12 <= hora < 20:
         print(" Es tarde")
    else:
        print(" Es noche")

parte_del_dia()

#39. Calificacion estudiante

def calificacion_estudiante(nota):
    """Es una funcion que evalua las notas de los estudiantes

    Args:
        nota (_float): la nota a evaluar
    """
    if 0 <nota <= 69:
        print(f'La calificacion es insuficiente')
    elif 70<=nota <=79:
        print (f'La nota es BIEN')
    elif 80<= nota <= 89:
        print(f'La nota es MUY BIEN')
    elif 90<= nota <= 100:
        print(f'La nota es EXCELENTE')
    else:
        print(f"Por varor, ingresa una nota valida")

calificacion_estudiante(90.5)

#40. funcion figuras

def area_figuras(opcion, tupla_datos):
    """_Es una funcion que calcula el area de una de las figuras dadas: rectangulo, circulo o triangulo

    Args:
        opcion (_str): _la figura: rectangulo, circulo o triangulo
        tupla_datos (_tuple): _tupla con los parametros necesarios para calcular el area

    Returns:
        _float_: _area de la figura
    """
    if opcion == "rectangulo":
       base, altura= tupla_datos #aqui definimos que datos tendra nuestra tupla
       area = base * altura
       return area 
    elif opcion == "circulo":
        radio = tupla_datos
        area = 3.14 * radio**2
        return area
    elif opcion == "triangulo":
        base, altura = tupla_datos
        area = (base * altura)/2
        return area
    
area_figuras("circulo", (5))

#41. Tienda online

def tienda_online():
  """Es una funcion que pide al usuario introducir un precio de articulo y un valor de cupon, si lo tiene. calcula el precio final.
  """
  precio_articulo = float(input("Por favor, ingrese el precio original del articulo"))
  if precio_articulo <= 0:
    print(f'Error de precio. Prueba otra vez')
    return

  descuento = input("¿Tiene Usd un cupon de descuento?(si o no)").strip().lower()
  if descuento == "si":
    valor_cupon = float(input("Ingrese el valor del cupon"))
    if valor_cupon <= 0:
      print (f'El cupon no es valido. Prueba otra vez')
    else:
      precio_final = precio_articulo - valor_cupon
      print( f'El precio final a pagar es {precio_final} euros')
  elif descuento == "no":
    print(f'El precio final del producto es {precio_articulo} euros')
  else:
    print("La respuesta no es valida. Prueba otra vez")

