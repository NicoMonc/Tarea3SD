import subprocess
import psycopg2

connection = psycopg2.connect(  user = "root",
                                password = "facil123",
                                host = "database",
                                port = "5432",
                                database = "reduce")

try:
    cursor = connection.cursor()
    #print ( connection.get_dsn_parameters(),"\n")
    #cursor.execute("SELECT version();")
    #record = cursor.fetchone()
    #print("You are connected to - ", record,"\n")

    for i in range(10):
        imprimir=i+1
        if (i<5):
            output = subprocess.check_output("cat 1_5/search"+str(imprimir)+".txt | python3 mapreduce.py | sort -k1,1 | python3 reducer.py", shell=True)
        else:
            output = subprocess.check_output("cat 6_10/search"+str(imprimir)+".txt | python3 mapreduce.py | sort -k1,1 | python3 reducer.py", shell=True)

        lineas = output.split()
        contador=0
        for each in lineas:
            lineas[contador] = each.decode("utf-8")
            contador+=1

        print(str(imprimir)+" - "+str(len(lineas)))
        valor=0
        while (valor<len(lineas)):
            cursor.execute("INSERT INTO registros (palabra,numero,archivo) VALUES (%s,%s,%s)",(lineas[valor],lineas[valor+1],imprimir))
            valor+=2
        
    cursor.execute("select * from registros order by palabra desc")
    registros.cursor.fetchall()
    for linea in registros:
        print(row)

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

"""
for each in lineas:
    if (lineas[contador][len(lineas[contador])-1]=='"'):
        primer=str(lineas[contador]).replace('b"','')
        fin=str(primer).replace('"','',1)
        print("Hola")
    else:
        primer=str(lineas[contador]).replace("b'","")
        fin=str(primer).replace("'","",1)

    lineas[contador]=fin
    contador+=1
    """
