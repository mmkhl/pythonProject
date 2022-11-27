# Необходимо написать любую игру на питоне
# игра "Угадай число" представляет из себя программу с консольным вводом выводом
import tkinter as tk
from random import randint
from tkinter import messagebox

someNum = randint(1, 42)
sumAttempt = 0
def game_Process():
    def get_entry(result_entry):
        s = result_entry.get()
        return int(s)

    myNum = get_entry(result_entry)
    if myNum == '':
        messagebox.showinfo("Подсказка", "Вы не ввели число")
    else:
        global sumAttempt
        myNum = get_entry(result_entry)
        if myNum > someNum:
            messagebox.showinfo("Подсказка", "Ваше число больше загаданного")
            sumAttempt += 1
        elif myNum < someNum:
            messagebox.showinfo("Подсказка", "Ваше число меньше загаданного")
            sumAttempt += 1
        elif myNum == someNum:
            messagebox.showinfo("Победа", "Вы угадали, это число: " + str(someNum) +"\n Количество попыток: " + str(sumAttempt))
            f = open('results.txt', 'a')
            f.write(str(sumAttempt))
            f.close()

def startGame():
    message = tk.StringVar()
    def clear():
        result_entry = tk.Entry(textvariable=message)
        result_entry.delete(0, tk.END)



    newWindow = tk.Toplevel(app)
    newWindow.title("Игра")
    newWindow.geometry("400x300")
    global result_entry

    result_entry = tk.Entry(newWindow, textvariable=message)
    result_entry.place(relx=.5, rely=.5 )
    lableStart = tk.Label(newWindow,  text = "Угадай число ${}")
    buttonCheck = tk.Button(newWindow, text = "Проверить", command=game_Process)
    buttonClear = tk.Button(newWindow, text="Очистить", command=clear)
    lableStart.pack(expand=True)
    result_entry.pack(expand=True)
    buttonCheck.pack(expand=True)
    buttonCheck.invoke()
    buttonClear.pack(expand=True)


app = tk.Tk()
app.title("Игра УГАДАЙ ЧИСЛО")
app.geometry("300x250")

menu_lable = tk.Label(text="Угадай число")
btnStart = tk.Button(app, text="Начать", command=startGame)
btnEnd = tk.Button(app, text="Выйти", command=quit)
menu_lable.pack(expand=True)

btnStart.pack(expand=True)
btnEnd.pack(expand=True)

app.mainloop()



