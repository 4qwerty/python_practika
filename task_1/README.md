#  Пояснення роботи Task-1

Як було написано на [python-scripts.com ](https://python-scripts.com/import-re-regular-expression) 
>Регулярні вирази - це невеликий мову, Який ви можете використовувати всередині Python і багатьох інших мовах програмування. Python ж підтримує завдяки бібліотеки, яку вам потрібно імпортувати. Основне використання регулярних виразів - це зіставлення рядків.

```python
import re
```

Все що я зрозумів з тієї статті, те що `import re` це модуль для роботи з регулярними виразами, для роботи з текстом, пошуку і здійснення маніпуляцій з підрядками в тексті, якраз те що нам потрібно для виконанн завдання.


 `str = input("Введіть рядок: ")`
 Створюємо ліст для введення рядка, ну відповідно заповнюємо його
___
Виділямо цифри від слів
 ```python
numb = re.findall(r'\d+', str)
str = re.sub(r"\d+", "", str, flags=re.UNICODE)
numb = [int(i) for i in numb]
```
Виводимо окремо розділени лісти з текстом і числами
```python
print("\n Рядок без чисел:\n", str)
print("\n Числа з рядка:\n", numb)
```
Міняємо перші і остані букви в словах на великі
```python
str, result = str.title(), ""
for word in str.split():    
      result += word[:-1] + word[-1].upper() + " "
print("\n Кожне слово починається і закінчується великою літерою:")
print( " " + result[:-1])
```

Виводимо максимальне число в масиві
```python
max_numb = max(numb)
print("\n Максимальне число в масиві:", max_numb)
```

Робим масив з чисел піднятих в степінь по їх індексу
```python
arr_vals = []
for i in range(len(numb)):
    
    if i !=numb.index(max_numb):
        temp = numb[i] 
        stup=temp** i
        arr_vals.insert(i, stup)
print("Масив чисел в степені по їх індексу:\n", arr_vals)
```
___
## Результат
![изображение](https://user-images.githubusercontent.com/50421230/124647399-96bb7a00-de9e-11eb-8176-563fc0144837.png)
___

Ну а далі все по стандарту, прописуюємо `git add .` для відстежування нових файлів, `git status` для перевірки статуса файлів, `git commit -m""` для запису змін і за допомогою `git push` заливаємо всі гілки.


![изображение](https://user-images.githubusercontent.com/50421230/124450539-3557b600-dd8d-11eb-9022-50382b1dc5fc.png)

Як бачимо все спрацювало 

![изображение](https://user-images.githubusercontent.com/50421230/124649114-bfdd0a00-dea0-11eb-977f-ed3f08ee6ca1.png)



