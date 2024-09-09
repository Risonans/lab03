n = input("Введите числа: ").split()
n = [int(num) for num in n]
print("Изначальный массив:\n", n)
for i in range(len(n)-1):
    for j in range(len(n)-1-i):
        if n[j] > n[j+1]:
            n[j], n[j+1] = n[j+1], n[j]
print("Сортировка пузырьком:\n", n)
