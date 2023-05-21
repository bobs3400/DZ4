number = int(input("Введите трехзначное число: "))
sum = number % 10 + number // 10 % 10 + number // 100 % 10
print(sum)