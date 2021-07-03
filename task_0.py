import random
arrayRand = random.sample(range(-100, 100), 30)
print("\n")
print("Сформувати список з 30 випадкових чисел:",arrayRand)
print("\nМаксимальний елемент списку: ", max(arrayRand), "\nПорядковий номер: ", arrayRand.index(max(arrayRand)))
listForSort = [i for i in arrayRand if (i % 2) == 1]
if len(listForSort) == 0: 
    print("Непарних чисел не знайдено") 
print(sorted(listForSort, reverse=True)) 
print("\n")
