number=int(input("enter the number"))
sum_of_digit =0
while number>0:
    remainder=number%10
    sum_of_digit =sum_of_digit+ remainder
    number= number//10
print("sum of the given number:",sum_of_digit)