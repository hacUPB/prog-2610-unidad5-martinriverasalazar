fp = open(".\\archivos_texto\\archivo.txt", "r")
#datos1 = fp.read()
#print ("El texto es", datos1)

datos2 = fp.readlines()
fp.close()
print (datos2)

for linea in datos2:
    print (linea[0])