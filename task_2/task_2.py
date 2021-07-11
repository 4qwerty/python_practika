from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math

root = Tk()
root.title('Калькулятор')

root['bg'] = '#fafafa'
root.wm_attributes('-alpha', 0.9)
root.resizable(width=False, height=False)


# логіка калькулятора
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

    # обрахунок сінус
    elif key == "sin":
        sin = calcScreen.get()
        calcScreen.insert(END, math.sin(float(sin)))
        calcScreen.delete(0)

    # обрахунок косинус
    elif key == "cos":
        cos = calcScreen.get()
        calcScreen.insert(END, math.cos(float(cos)))
        calcScreen.delete(0)

    # обрахунок тангенс
    elif key == "tg":
        tg = calcScreen.get()
        calcScreen.insert(END, math.tan(float(tg)))
        calcScreen.delete(0)

    # обрахунок котангенс
    elif key == "ctg":
        sin = calcScreen.get()
        cos = calcScreen.get()
        calcScreen.insert(END, math.tan(float(cos))/math.tan(float(sin)))
        calcScreen.delete(0)

    # обрахунок натуральний логарифм
    elif key == "log":
        log = calcScreen.get()
        calcScreen.insert(END, math.log1p(float(log)))
        calcScreen.delete(0)

    # обрахунок десятковий логарифм
    elif key == "ln":
        ln = calcScreen.get()
        calcScreen.insert(END, math.log10(float(ln)))
        calcScreen.delete(0)
    
    # Стерти екран
    elif key == "C":
        calcScreen.delete(0, END)

    else:
        if "=" in calcScreen.get():
            calcScreen.delete(0, END)
        calcScreen.insert(END, key)   


# ствоюємо ліст з кнопками
buttonList = [
    "cos", "sin", "tg", "%",
    "ctg", "log", "ln", "/",
    "7", "8", "9", "*",
    "4", "5", "6", "-",
    "3", "2", "1", "+",
    "C", "0", ".", "="
]
r = 1
c = 0

for i in buttonList:
    rel = ""
    def cmd(x=i): return calc(x)
    ttk.Button(root, text=i, command=cmd).grid(row=r, column=c)
    c += 1
    if c > 3:
        c = 0
        r += 1

calcScreen = Entry(root, width=47)
calcScreen.grid(row=0, column=0, columnspan=5)

root.mainloop()
