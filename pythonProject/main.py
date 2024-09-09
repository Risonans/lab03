def puzir(n, x):
    if x == 1:
        for i in range(len(n) - 1):
            for j in range(len(n) - 1 - i):
                if n[j] > n[j + 1]:
                    n[j], n[j + 1] = n[j + 1], n[j]
        return n
    if x == 2:
        for i in range(len(n) - 1):
            for j in range(len(n) - 1 - i):
                if n[j] < n[j + 1]:
                    n[j], n[j + 1] = n[j + 1], n[j]
        return n

n = input("Введите числа: ").split()
n = [int(num) for num in n]
x = int(input("По возрастанию - 1 или по убыванию - 2: "))
print("Изначальный массив:\n", n)
print("Сортировка пузырьком:\n", puzir(n,x))
