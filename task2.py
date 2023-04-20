"""Задача 18: Требуется найти в массиве A[N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
Ввод: 5
Ввод: 1 2 6 4 9
Ввод: 8
-> 9"""

size = int(input("Введите размер массива: "))
random_list=[]
for i in range(size):
    random_list.append(int(input("Введите число в массив: ")))
print(random_list)
result = 0
index = 1
searchNumber = int(input("Введите число, которое мы будем искать: "))
for i in range(size):
    if random_list[i] == searchNumber:
        print("Такое число есть в массиве")
    elif random_list[i] - index == searchNumber:
        print("Мы получили число: ")
        print(random_list[i])
        index += 1
    elif random_list[i] + index == searchNumber:
        print("Мы получили число: ")
        print(random_list[i])
        index += 1

   
