# Пояснення до Task2

В першу чергу потрібно підключити потрібні модулі і бібліотеки, одна з голоаних це __Tkinter__

> Tkinter - це пакет для Python, призначений для роботи з бібліотекою Tk. Бібліотека Tk містить компоненти графічного інтерфейсу користувача (графічний інтерфейс користувача - GUI).

Під графічним інтерфейсом користувача розуміються всі тs вікна, кнопки, текстові поля для вводу, списки, радіокнопки, флажки та ін. Через них ви взаємодієте з програмою та керуєте ним. Якраз те що потрібно для реалізації калькулятора.

Ну і звісно для математичних обрахунків таких як cos, sin, tan, ctg, log, ln потрібен модуль __math__

А ось і повний перелік викорастих модулів і бібліотек
```python
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math
```
Починаємо прорисувати логіку калькулятора в функції `def`, змінна `global memory` потрібна для того щоб передавати значення не блочно а гобально
```python
def calc(key):
    global memory
    if key == "=":
        try:
            result = eval(calcScreen.get())
            calcScreen.delete(0, END)
            calcScreen.insert(END, str(result))
        except:
            calcScreen.insert(END, "Error!")
            messagebox.showerror("Error!")
```
і трішки про `eval()` в цій строчці, у Python є вбудована функція `eval ()`, яка виконує строчку з кодом і повертає результат виконання, корисна, коли необхідно виконати динамічно оновлене вираження Python з якого-небудь вводу. Я її використав для того щоб зробити кнопку '=' і для простих математичніх дій таких як +, -, *, /.

```python
result = eval(calcScreen.get())
```

=, +, -, *, /, %, ми зробили залишилось cos, sin, tan, ctg, log, ln, для цього я використав таку костукцію, при натисканні на кнопку 'sin', данні з екрана передаються в однойменну змінну, потім передаємо цю змінну в __mat.sin()__, очищаємо екран і виводимо результат, в подальшому ця констукція буде використуватись для виконання всіх інших функцій.   
```python
elif key == "sin":
        sin = calcScreen.get()
        calcScreen.insert(END, math.sin(float(sin)))
        calcScreen.delete(0)
```
```python
elif key == "ctg":
        sin = calcScreen.get()
        cos = calcScreen.get()
        calcScreen.insert(END, math.tan(float(cos))/math.tan(float(sin)))
        calcScreen.delete(0)
```

```python
elif key == "ln":
        ln = calcScreen.get()
        calcScreen.insert(END, math.log10(float(ln)))
        calcScreen.delete(0)
```

Тут ми просто створюємо ліст в який розміщюємо всі кнопки

```python 
buttonList = [
    "cos", "sin", "tg", "%",
    "ctg", "log", "ln", "/",
    "7", "8", "9", "*",
    "4", "5", "6", "-",
    "3", "2", "1", "+",
    "C", "0", ".", "="
]
```

Елемент `Entry` представляє собою поле для введення тексту, чудово підходить для ролі екрану калькулятора, тут ми задаємо йомe ширину і позицію.
```python
calcScreen = Entry(root, width=47)
calcScreen.grid(row=0, column=0, columnspan=5)
```

## Результат

![изображение](https://user-images.githubusercontent.com/50421230/125207398-cb5f7500-e294-11eb-988d-d54421308b15.png)  ![изображение](https://user-images.githubusercontent.com/50421230/125207402-dca88180-e294-11eb-9c99-9606ebdac81c.png)


Прописуюємо `cd ...` для переходу в папку яки ви вкажете в адресі, `git add .` для відстежування нових файлів, `git status` для перевірки статуса файлів, `git commit -m""`для запису змін і за допомогою `git push`заливаємо всі гілки.

![изображение](https://user-images.githubusercontent.com/50421230/125200296-1a94ae00-e273-11eb-9ba3-4c8093ea4fc2.png)

Все успішно запушилось

![изображение](https://user-images.githubusercontent.com/50421230/125205471-196f7b00-e28b-11eb-9a5d-cc6bc0ee20aa.png)

