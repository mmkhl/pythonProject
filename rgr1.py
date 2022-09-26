# Необходимо написать любую игру на питоне
# игра "Угадай число" представляет из себя программу с консольным вводом выводом

from random import randint
from tkinter import *
from tkinter import messagebox

someNum = randint(1, 42)
myNum = 0
flagGame = True
sumAttempt = 0

def startGame():
    global sumAttempt
    myNum = int(message.get())
    if myNum > someNum:
        messagebox.showinfo("Подсказка", "Ваше число больше загаданного")
        sumAttempt += 1
    elif myNum < someNum:
        messagebox.showinfo("Подсказка", "Ваше число меньше загаданного")
        sumAttempt += 1
    elif message.get() == "":
        messagebox.showinfo("Подсказка", "Вы не ввели число")
    elif myNum == someNum:
        messagebox.showinfo("Победа", "Вы угадали, это число: " + str(someNum) +"\n Количество попыток: " + str(sumAttempt))

def show_message():
    messagebox.showinfo("Подсказка", message.get())
def clear():
    result_entry.delete(0, END)
root = Tk()
root.title("Угадай число")
root.geometry("300x200")

message = StringVar()
result_entry = Entry(textvariable=message)
result_entry.place(relx=.5, rely=.2,  anchor="c")

programm_button = Button(text="Очистить", font=("Times New Roman", 15), command=clear)
programm_button.place(relx=.3, rely=.5, anchor="c")

programm_button = Button(text="Проверить", font=("Times New Roman", 15), command=startGame)
programm_button.place(relx=.7, rely=.5, anchor="c")
root.mainloop()


