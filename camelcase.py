
"""
Programa basico para trabajar con camel case y saber cuantas palabras tiene un metodo cualquiera dado al programa 
en este caso esta definido para que sea mucho mas facil de revisar pero facil de cambiar para cualquier otro caso
"""
def cuantasMayus(metodo):
    mayus=1
    for i in metodo:
        aux = i.isupper()
        if aux ==True:
            mayus = mayus + 1
    return mayus



print(cuantasMayus("updatePassword"))