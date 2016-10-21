x = int(input("Give me a three digit number or else: "))
hundreds = x // 100 % 10
tens = x // 10 % 10
ones = x % 10
print("Hundreds:"+str(hundreds))
print("Tens:"+str(tens))
print("Ones:"+str(ones))
