from datetime import datetime
from random import randint

def div(a,b):
    return a / b


def analyze_pesel(pesel):
    weights = [1,3,7,9,
    1, 3, 7, 9, 1, 3]
    weight_index=0
    digits_sum= 0
    for digit in pesel[ : -1 ]:
        digits_sum +=int(digit)*weights[weight_index]
        weight_index+=1
    pesel_modulo = digits_sum % 10
    validate = 10-pesel_modulo
    if validate == 10:
        validate = 0
    gender = "male" if int(pesel[-2]) % 2==1 else "female"
    month = int(pesel[2:4])

    if month > 80:
        year_beginig = "18"
        month_minus = 80
    elif month > 60:
        year_beginig = "22"
        month_minus = 60
    elif month > 40:
        year_beginig = "21"
        month_minus = 40
    elif month > 20:
        year_beginig = "20"
        month_minus = 20
    else:
        month_minus = 0
        year_beginig = '19'

    month = int(month) - month_minus
    year = int(year_beginig + pesel[0: 2])
    birth_date = datetime(year, month,int(pesel[4 :6]))
    result = {
        "pesel":pesel,
        "valid":validate == int(pesel[-1]),
        "gender":gender,
        "birth_date": birth_date
            }
    return result