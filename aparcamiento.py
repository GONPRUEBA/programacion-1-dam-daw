horas = float(input('Indtroduce las horas que has usado el parking: '))

if horas < 2:
    print('El costo total es: ',horas*2,'€')
elif horas > 2 and horas < 5:
    print('El costo total es: ',horas*1.5,'€')
else:
    print('El costo total es: ',horas,'€')
