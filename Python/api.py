import urllib.request
import os

for i in range(10):
    imprimir=i+1
    opcion = input ("Texto a buscar: ")
    print(opcion)
    if(i<5):
        site = urllib.request.urlopen('https://es.wikipedia.org/w/api.php?action=query&list=search&srprop=snippet&format=json&origin=*&utf8=&srsearch='+opcion)
        data = site.read()
        print(data)

        isFile = os.path.isfile("./1_5/search"+str(imprimir)+".txt")
        if (isFile):
            os.remove("./1_5/search"+str(imprimir)+".txt")

        crear = open("./1_5/search"+str(imprimir)+".txt","wb") #open file in binary mode
        crear.write(data)
        crear.close()
    else:
        site = urllib.request.urlopen('https://es.wikipedia.org/w/api.php?action=query&list=search&srprop=snippet&format=json&origin=*&utf8=&srsearch='+opcion)
        data = site.read()
        print(data)

        isFile = os.path.isfile("./6_10/search"+str(imprimir)+".txt")
        if (isFile):
            os.remove("./6_10/search"+str(imprimir)+".txt")

        crear = open("./6_10/search"+str(imprimir)+".txt","wb") #open file in binary mode
        crear.write(data)
        crear.close()