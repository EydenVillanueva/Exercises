def dayOfYear(date):
    date = date.split('-')

    anio = int(date[0])
    meses = int(date[1])
    dias = int(date[2])

    suma = 0
    es_bisiesto = False
    if anio%4 == 0 and anio%100 != 0:
        es_bisiesto = True
    
    for i in range(1,meses+1):
        if i != meses:
            if i == 2 and es_bisiesto:
                suma+= 29
            elif i == 2 and not es_bisiesto:
                suma+= 28
            elif i <= 7:
                if i%2 == 0:
                    suma+= 30
                elif i%2 != 0:
                    suma+= 31
            elif i > 7:
                if i%2 == 0:
                    suma+= 31
                elif i%2 != 0:
                    suma+= 30              


    suma+= dias

    return suma
    
if __name__ == "__main__":
    print(dayOfYear("1900-03-25"))

