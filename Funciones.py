from datetime import date
def getStringToList(fecha):#!Formato de fecha esperado YYYY/MM/DD
    """
    Funcionamiento: Utiliza el string y lo acomoda en una lista ordenada para ingresarse al date()
    Entradas: fecha(str): 
    Salidas: retorna una lista ordenada por YYYY/MM/DD """
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
    Funcionamiento: Utiliza el string y lo acomoda en una lista ordenada para ingresarse al date()
    Entradas: fecha(str): 
    Salidas: retorna una lista ordenada por YYYY/MM/DD """
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
        else: return "virgo"
    elif fecha[1] == 9:
        if fecha[2] < 23: return "virgo"
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
    Entradas:
        x(int): Número decimal
    Salidas:
        respuesta(int): Número binario
    """
    respuesta = 0
    i=0
    while x != 0:
        respuesta = respuesta + (x%2)*10**i
        x = x//2
        i = i + 1
    return respuesta
def yearToBin(fecha):
    years=getYears(fecha)
    return (fromDecToBin(years))