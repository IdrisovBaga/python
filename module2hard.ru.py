result = []
n = int(input("Введите число от 3 до 20: "))
print(n)

for i in range(1, 21):
    for j in range(1, 21):
        k = i + j
        if n % k == 0 and i < j:
            result.append(i)
            result.append(j)
            print("i + j = ", i, "+", j)

result_st = ''.join(map(str, result))
print("Пароль для числа ", n, "_", result_st)