#Vamos a tomar como delimitadores que separan subcadenas a los "espacios,_,-,punto y coma,punto")
#Coincidencia 100% y subcadenas desordenadas --> Parecidas
#Coincidencia > 80% y < 100%, y subcadenas en orden --> Parecidas
#Coincidencia > 80% y < 100%, y subcadenas desordenadas --> Diferentes
#Coincidencia < 80% (sin importar el orden) --> Diferentes

import re
def eliminarDelimitadores(cadena):
    delim= r'[-,;._\s+]'
    partes=re.split(delim,cadena)
    return partes

def comparar(partes_c1, partes_c2):
    coincidencias=[]

    for s1 in partes_c1:
        for s2 in partes_c2:
            if(s1 not in coincidencias and s1==s2):
                coincidencias.append(s1)

    if(len(partes_c1) > 0 or len(partes_c2) > 0):
        return len(coincidencias)/max(len(partes_c1),len(partes_c2))
    else:
        print("No se puede comparar. Las cadenas estan vacías")
        return 1
def mismo_orden(partes_c1,partes_c2):
    contador=0
    if(len(partes_c1) <= len(partes_c2)):
        for i in range(len(partes_c1)):
            if(partes_c1[i]==partes_c2[i]):
                contador+=1

    else:
        for i in range(len(partes_c2)):
            if(partes_c1[i]==partes_c2[i]):
                contador+=1

    return contador==min(len(partes_c1),len(partes_c2)) #El minimo porque hemos contado teniendo en cuenta la cadena mas corta
def main():
    cadena1=input("Ingrese la cadena 1: ")
    cadena2=input("Ingrese la cadena 2: ")
    partes_c1=eliminarDelimitadores(cadena1)
    partes_c2=eliminarDelimitadores(cadena2)


    porcentaje_coincidencia = comparar(partes_c1, partes_c2)
    if(porcentaje_coincidencia == 1):
        if(mismo_orden(partes_c1,partes_c2)):
            print("Las cadenas son iguales")
        else:
            print("Las cadenas son parecidas")
    elif(porcentaje_coincidencia > 0.8):
        if(mismo_orden(partes_c1,partes_c2)):
            print("Las cadenas son parecidas")
        else:
            print("Las cadenas son diferentes")
    else:
        print("Las cadenas son diferentes")

main()