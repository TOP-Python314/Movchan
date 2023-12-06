numbers = int(input ())
num1 = numbers%10
num2 = numbers%100//10
num3 = numbers//100
print("Сумма цифр = " + str(num1+num2+num3), "Произведение цифр = " + str(num1*num2*num3),sep='\n')
