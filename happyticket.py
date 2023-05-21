number = input("Введите номер билета: ")
if len(number) % 2 != 0:
    print("число не может быть счастливым")
else:
    i = 0
    sum_left = 0
    sum_right = 0 
    while i < len(number) // 2:
        sum_left = sum_left + int(number) // (10 ** (i + len(number) // 2))  % 10
        sum_right = sum_right + int(number) // 10 ** i % 10
        i += 1
    if sum_left == sum_right:
        print("Билет счастливый")
    else:
        print("Билет не счастливый")