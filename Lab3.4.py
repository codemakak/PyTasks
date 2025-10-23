import math
n = int(input("Введите число: "))
i = 2
isSimple = True
while i <= math.sqrt(n):
    if n%i == 0:
        isSimple = False
    i+=1
if isSimple == True:
    print("Число простое")
else:
    print("Число составное")