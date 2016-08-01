bigpal=0
paly = 0
for number1 in range(100,999):
    for number2 in range (100,999):
        prod = number1*number2
        product = str(prod)
        if product[0]==product[-1]:
            if product[1]==product[-2]:
                if product[2]==product[-3]:
                    paly = prod
        if paly > bigpal:
            bigpal = paly

print bigpal



