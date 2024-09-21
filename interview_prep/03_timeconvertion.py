s = '07:05:45PM'

def timeConversion(s):
    # Extrae horas, minutos, segundos y periodo AM/PM
    hh = int(s[:2])
    mm = s[3:5]
    ss = s[6:8]
    TT = s[8:]
    
    if TT == 'AM':
        if hh == 12:
            hh = 0  # Cambia 12AM a 00 en formato 24 horas, no se puede usar 00
    elif TT == 'PM':
        if hh != 12:
            hh += 12  # Suma 12 a las horas para convertir de PM a formato 24 horas
    
    return f"{hh:02}:{mm}:{ss}"  # Devuelve la hora en formato 24 horas, :02 devuelve 2 digitos

# Ejemplo de uso
converted_time = timeConversion(s)
print(converted_time)  # Imprime '19:05:45' para '07:05:45PM'

"""

Index:  0  1  2  3  4  5  6  7  8  9
        |  |  |  |  |  |  |  |  |  |
Char:   0  7  :  0  5  :  4  5  P  M

"""