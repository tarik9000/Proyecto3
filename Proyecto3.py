"""
# Proyecto del tema
Vas a crear un programa que, primero le pida al usuario que ingrese un texto. Puede ser un texto cualquier, como un artículo entero, un párrafo, una frase, lo que quiera. Luego, el programa le va a pedir al usuario que también ingrese tres letras a su elección, y a partir de ese momento nuestro código va a procesar esa información para hacer cinco tipos de análisis y devolverle al usuario la siguiente información:
1.	¿Cuántas veces aparece cada una de las letras que eligió? Para lograr esto, puedes almacenar esas letras en una lista y luego usar algún método propio de string que permita contar cuántas veces aparece un substring dentro del string. Ten en cuenta que al buscar las letras puede haber mayúsculas y minúsculas, y esto afecta al resultado. Hay métodos que pasan letras a minúsculas o mayúsculas.
2.	Le va a decir al usuario cuántas palabras hay a lo largo de todo el texto. Recuerda que hay un método de string que permite transformarlo en una lista, y que hay funciones que cuentan el largo de una lista.
3.	Va a informar de cuál es la primera letra del texto y cuál es la última.
4.	El sistema nos va a mostrar cómo quedaría el texto si invirtiéramos el orden de las palabras.
5.	El sistema nos va a decir si la palabra “python” se encuentra dentro del texto.

"""
frase=input("Escriba una frase o cualquier tipo de texto a su eleccion: ")
lista=[input("Escriba una letra: "),input("Escriba una letra: "),input("Escriba una letra: ")]
mayusculas=frase.upper()
print("La letra "+lista[0]+" aparece "+str(mayusculas.count(lista[0].upper()))+" y la letra "+lista[1]+" aparece "+str(mayusculas.count(lista[1].upper()))+" y la letra "+lista[2]+" aparece "+str(mayusculas.count(lista[2].upper())))
palabras=frase.split(" ")
print("En el texto que has pasado tiene "+str(len(palabras))+" palabras")
print("La primera letra del texto es: "+frase[0]+" y la ultima letra es: "+frase[-1])
print("El texto invertido se veria asi: "+frase[::-1])

print("¿Se encuentra la palabra 'python' en el texto? "+str(mayusculas.find("python".upper())!=-1))