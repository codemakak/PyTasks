v = int(input("Введите v "))
k = int(input("Введите k "))

if v > k:
    Z = v - k + 1
elif v < k:
    Z = k**2 - v**2
else:
    Z = k**2 - k

print("Z равно",Z)