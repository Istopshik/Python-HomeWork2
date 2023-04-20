"""Требуется вычислить, сколько раз встречается некоторое число X в массиве A[N].
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
Ввод: 5
Ввод: 3 2 3 7 5
Ввод: 3
-> 2"""

size = int(input("Введите размер массива: "))
random_list=[]
for i in range(size):
    random_list.append(int(input("Введите число в массив: ")))
print(random_list)
result = 0
searchNumber = int(input("Введите число, которое мы будем искать: "))
for i in range(size):
    if random_list[i] == searchNumber:
        result = result + 1
print(result)        

