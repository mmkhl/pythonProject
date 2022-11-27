
from tkinter import *
from tkcalendar import *
import datetime

dt_now = datetime.datetime.now()
print(dt_now)


win= Tk()
win.title("Calendar")
win.geometry("700x600")

cal= Calendar(win, selectmode="day", year=int(2022), month=3, day=3)
cal.pack(pady=40)

def get_date():
   label.config(text=cal.get_date())


button= Button(win, text= "Select the Date", command= get_date)
button.pack(pady=20)

label= Label(win, text="")

label.pack(pady=20)

labelCurDate = Label(win, text=datetime.datetime.now())

labelCurDate.pack(pady=50)
win.mainloop()