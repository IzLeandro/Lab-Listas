from datetime import date
def getStringToList(fecha):#!Formato de fecha esperado YYYY/MM/DD
    year=int(fecha[:4])
    month=int(fecha[5:7])
    day=int(fecha[8:])
    return [year,month,day]

def getYears(fecha): #!Formato de fecha esperado YYYY/MM/DD
    fecha=getStringToList(fecha)
    fecha=date(fecha[0],fecha[1],fecha[2])
    today=date.today()
    return today.year - fecha.year - ((today.month, today.day) < (fecha.month, fecha.day))

