# Elaborado por: Leandro Camacho Aguilar & Celina Madrigal Murillo
# Fecha de Creación: 13/10/2020 10:00pm
# Fecha de última Modificación: 14/10/2020 09:39am
# Versión: 3.8

#Importación de librerias
import re
from Funciones import *

#Definición de funciones
def solicitarYValidarDatos():
    nombreCompleto=str(input("Digite su nombre completo: "))

    fechaDeNacimiento=str(input("Digite su fecha de nacimiento(Sea cuidadoso de usar el formado AAAA/MM/DD): "))
    if bool(re.match("\d{4}(?P<sep>[-/])\d{2}(?P=sep)\d{2}",fechaDeNacimiento)) == False:     
        input("Compruebe que esté siguiendo correctamente el formato solicitado al ingresar la fecha.\nPresione enter para continuar...")
        return ""

    altura=input("Digite su altura (ej: 1.80):")
    try:
        altura=float(altura)
    except:
        input("Compruebe que esté siguiendo correctamente el formato solicitado al ingresar la altura.\nPresione enter para continuar...")
        return ""
    sexo=str(input("Indique su sexo(M o F): "))
    if sexo.upper() =="M":
        sexo=True
    elif sexo.upper()=="F":
        sexo=False
    else:
        input("Ingrese un valor correcto en el apartado del sexo.\nPresione enter para continuar...")
        return ""
    return [nombreCompleto,fechaDeNacimiento,altura,sexo]

#Programa Principal
def mainMenu():
    paciente=solicitarYValidarDatos()
    if paciente=="":
        return ""
    print(paciente[0],", usted nació un día",diaParImpar(paciente[1]),"del mes de",nombreMes(paciente[1]),", usted tiene",getYears(paciente[1]),"años, que visto en binario es",yearToBin(paciente[1]), ",su signo sodiacal es:",getHoroscope(paciente[1]),"por ende su personalidad es",personalidad(paciente[1]),", su sexo es",["femenino","masculino"][paciente[3]],"y mide",paciente[2],"cm.")
    return
mainMenu()
