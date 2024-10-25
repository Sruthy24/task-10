

tem1=int(input("enter temperature"))
unit=(input("Is this in (C)elsius or (F)ahrenheit? "))
if unit=="C":
    f = (9/5*tem1) + 32
    print(tem1," Celsius is",f," Fahrenheit")
else:
    C = 5/9*(tem1-32)
    print(tem1," Fahrenheit is ",C," Celsius.")

