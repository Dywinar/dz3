x = int(input("Введите число: "))
sum = 0
while x > 0:
    num = x % 10
    x //= 10
    sum += num
print(sum)
