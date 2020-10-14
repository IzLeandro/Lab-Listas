# Elaborado por: Leandro Camacho Aguilar & Celina Madrigal Murillo
# Fecha de Creación: 13/10/2020 10:00pm
# Fecha de última Modificación: 14/10/2020 09:39am
# Versión: 3.8

#Importación de librerias
from datetime import date

#Definición de funciones 
def getStringToList(fecha):#!Formato de fecha esperado YYYY/MM/DD
    """
    Funcionamiento: Utiliza el string y lo acomoda en una lista ordenada para ingresarse al date()
    Entradas: fecha(str): 
    Salidas: retorna una lista ordenada por YYYY/MM/DD 

    """
    year=int(fecha[:4])
    month=int(fecha[5:7])
    day=int(fecha[8:])
    return [year,month,day]
def getYears(fecha): #!Formato de fecha esperado YYYY/MM/DD
    """
    Funcionamiento: Retorna los años según la fecha de nacimiento ingresada por el usuario
    Entradas: fecha(str): 
    Salidas: No Variable(int): luego de realizar una resta y una comparación donde se aprovecha una
    función de py, donde toma los True/False como 1/0, lo que nos permite realizar cosas como una resta:
    10-True= 9"""
    fecha=getStringToList(fecha)
    fecha=date(fecha[0],fecha[1],fecha[2])
    today=date.today()
    return today.year - fecha.year - ((today.month, today.day) < (fecha.month, fecha.day))
def getHoroscope(fecha):
    fecha=getStringToList(fecha)
    """
    Funcionamiento: Según la fecha de nacimiento dice a que signo pertenece 
    Entradas: fecha(str): 
    Salidas: String

    """
    if fecha[1] == 12:
        if fecha[2] < 22: return "Sagitario"
        else: return "Capricornio"
    elif fecha[1] == 1:
        if fecha[2] < 20: return "Capricornio"
        else: return "Acuario"
    elif fecha[1] == 2:
        if fecha[2] < 19: return "Acuario"
        else: return "Picis"
    elif fecha[1] == 3:
        if fecha[2] < 21: return "Picis"
        else: return "Aries"
    elif fecha[1] == 4:
        if fecha[2] < 20: return "Aries"
        else: return "Tauro"
    elif fecha[1] == 5:
        if fecha[2] < 21: return "Tauro"
        else: return "Geminis"
    elif fecha[1] == 6:
        if fecha[2] < 21: return "Geminis"
        else: return "Cancer"
    elif fecha[1] == 7:
        if fecha[2] < 23: return "Cancer"
        else: return "Leo"
    elif fecha[1] == 8:
        if fecha[2] < 23: return "Leo"
        else: return "Virgo"
    elif fecha[1] == 9:
        if fecha[2] < 23: return "Virgo"
        else: return "Libra"
    elif fecha[1] == 10:
        if fecha[2] < 23: return "Libra"
        else: return "Escorpio"
    elif fecha[1] == 11:
        if fecha[2] < 22: return "Escorpio"
        else: return "Sagitario"
def fromDecToBin(x):
    """
    Funcionamiento: Crea un número binario a partir del número decimal dado.
    Entradas: x(int): Número decimal
    Salidas:respuesta(int): Número binario

    """
    respuesta = 0
    i=0
    while x != 0:
        respuesta = respuesta + (x%2)*10**i
        x = x//2
        i = i + 1
    return respuesta
def yearToBin(fecha):
    """
    Funcionamiento: Convierte la edad en binario.
    Entradas: fecha(str):
    Salidas: Número binario

    """
    years=getYears(fecha)
    return (fromDecToBin(years))
def esPar(num):
    """
    Funcionamiento: Dice si un número es par o impar.
    Entradas: Número
    Salidas: Booleano 

    """
    if num%2==0:
        return True
    return False
def diaParImpar(dia):
    """
    Funcionamiento: Dice si un número es par o impar.
    Entradas: fecha(str)
    Salidas: String

    """
    if esPar(getStringToList(dia)[2]):
        return 'par'
    return 'impar'
def nombreMes(numMes):
    """
    Funcionamiento: Dado un número retorna a que mes representa ese número.
    Entradas: fecha(str)
    Salidas: String

    """
    if getStringToList(numMes)[1]==1:
        return 'Enero'
    elif getStringToList(numMes)[1]==2:
        return 'Febrero'
    elif getStringToList(numMes)[1]==3:
        return 'Marzo'
    elif getStringToList(numMes)[1]==4:
        return 'Abril'
    elif getStringToList(numMes)[1]==5:
        return 'Mayo'
    elif getStringToList(numMes)[1]==6:
        return 'Junio'
    elif getStringToList(numMes)[1]==7:
        return 'Julio'
    elif getStringToList(numMes)[1]==8:
        return 'Agosto'
    elif getStringToList(numMes)[1]==9:
        return 'Setiembre'
    elif getStringToList(numMes)[1]==10:
        return 'Octubre'
    elif getStringToList(numMes)[1]==11:
        return 'Noviembre'
    else:
        return 'Diciembre'
def personalidad(signo):
    """
    Funcionamiento: Dice como es su personalidad según su signo.
    Entradas: fecha(str)
    Salidas: String

    """
    if getHoroscope(signo)=='Acuario':
        return 'fuerte y simpática'
    elif getHoroscope(signo)=='Piscis':
        return 'tranquila, amable y amistosa'
    elif getHoroscope(signo)=='Aries':
        return 'enérgica y activa'
    elif getHoroscope(signo)=='Tauro':
        return 'práctica y tenaz'
    elif getHoroscope(signo)=='Geminis':
        return 'abierta y sociable'
    elif getHoroscope(signo)=='Cáncer':
        return 'leal y de carácter protector'
    elif getHoroscope(signo)=='Leo':
        return 'curiosa y enérgica'
    elif getHoroscope(signo)=='Virgo':
        return 'analítica y de perfil bajo'
    elif getHoroscope(signo)=='Libra':
        return 'justa e intelectual'
    elif getHoroscope(signo)=='Escorpio':
        return 'ambiciosa y pasional'
    elif getHoroscope(signo)=='Sagitario':
        return 'sociable y tolerante'
    elif getHoroscope(signo)=='Capricornio':
        return 'seria y realista'

