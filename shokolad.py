n = int(input("Введите размер шоколадки N: "))
m = int(input("Введите размер шоколадки M: "))
k = int(input("Введите количество долек которые надо отломить : "))
if k % n == 0 or k % m == 0:
    print("Yes")
else:
    print("No")