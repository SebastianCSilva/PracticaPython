
#https://es.stackoverflow.com/questions/388732/como-seria-el-c%c3%b3digo-para-este-programa-en-python

numteclado = 5+1
sumatotal = 0
for i in range(numteclado):
    aux = 0
    sumareset = 0
    textosum = ""
    if i<=0:
        pass
    else:
        while(aux<i):
            aux+=1
            sumareset = sumareset + aux
            textosum = textosum + str(aux) 
            if aux==i:
                pass
            else:
                textosum = textosum + "+"
        print(textosum + "=" + str(sumareset))
        
        sumatotal = sumatotal + sumareset
    print("\n")

print("La suma de la serie es =",sumatotal)