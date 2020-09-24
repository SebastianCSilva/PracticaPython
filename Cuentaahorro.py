# coding=utf-8
dineromensual=int(input("Dinero mensual a guardar\n"))
years = int(input("Años a guardar\n"))

#Inicializacion de los 12 meses 
meses = []
for mes in range(12):
    meses.append(mes)


interes = 1.035
dineromes = []
dinerosininterez = (dineromensual*12) * years
dineroconinterez = 0

for _ in range(len(meses)):
    dineromes.append(dineromensual)


for year in range(years-1):
    
    for mes in range(len(meses)):
        dinerototal = dineromes[mes]
        dineroconinterez = dinerototal * interes
        dineromes[mes] = dineroconinterez + dineromensual
        
dineroconinterez = 0 
for _ in range(len(meses)):
    dineroconinterez = dineroconinterez + dineromes[_] 
    

print('Dinero con interez ' + str(dineroconinterez))
print('Dinero sin interez '+ str(dinerosininterez))
print('Dinero de diferencia debido al interez ' + str(dineroconinterez - dinerosininterez))


