import random
sentence=""
z=0
sentence = input("Escribe una oracion: ")

lists=list(sentence)

for z in range(len(lists)):
    r=random.randint(0,1)
    if r == 0:
        lists[z]=(lists[z].upper())
    elif r == 1:
        lists[z]=(lists[z].lower())
    z=z+1
print("".join(lists))