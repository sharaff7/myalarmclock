import datetime
import time
import tkinter
import threading
import winsound
from tkinter import font

window = tkinter.Tk()
window.geometry('500x300')
window.title("An Alarm Clock")

_currentTime = datetime.datetime.now()


def actual_time():
    _currentDate = _currentTime.date().today()
    _currentHour = _currentTime.hour
    _currentMin = _currentTime.minute
    return _currentHour, _currentMin, _currentDate


def set_alarm(hour_var=tkinter.StringVar(window), min_var=tkinter.StringVar(window)):
    _currentHour = datetime.datetime.now().hour
    Hour = hour_var.get()
    Min = min_var.get()
    alarm_time_hours = int(Hour)
    alarm_time_minutes = int(Min)
    change_day = datetime.date.today()
    return alarm_time_hours, alarm_time_minutes, change_day


def play_alarm(hour_var, min_var):
    while True:
        if actual_time() == set_alarm(hour_var, min_var):
            text.insert(tkinter.END, "Wake Up!\n")
            winsound.Beep(37, 1000)
            break
        elif actual_time() < set_alarm(hour_var, min_var):
            alarm_time = _currentTime.replace(hour=int(hour_var.get()), minute=int(min_var.get()))
            time_left = alarm_time - _currentTime
            time_In_seconds = datetime.timedelta.total_seconds(time_left)
            text.insert(tkinter.END, f"time left: {time_left}\n")
            time.sleep(time_In_seconds)
            text.insert(tkinter.END, "Wake Up!\n")
            winsound.Beep(37, 1000)
            break
        else:
            change_day = datetime.date.today() + datetime.timedelta(days=1)
            day = int(change_day.day)
            alarm_time = _currentTime.replace(day=day, hour=int(hour_var.get()), minute=int(min_var.get()))
            time_left = alarm_time - _currentTime
            time_In_seconds = datetime.timedelta.total_seconds(time_left)
            text.insert(tkinter.END, f"time left: {time_left}\n")
            time.sleep(time_In_seconds)
            text.insert(tkinter.END, "Wake Up!\n")
            winsound.Beep(37, 1000)
            break


def realtime():
    currentime = time.strftime("%H:%M:%S")
    c.config(text=currentime)
    window.after(1000, realtime)


def user_interface():
    add_time = tkinter.Label(window, text="Hour & Min", fg="black", font=("bell mt", 15))
    add_time.pack(pady=10)
    frame = tkinter.Frame(window)
    frame.pack()
    hour_var = tkinter.StringVar(value='00')
    min_var = tkinter.StringVar(value='00')
    hours = [str(i).zfill(2) for i in range(24)]
    hour_var.set(hours[0])
    mins = [str(i).zfill(2) for i in range(60)]
    min_var.set(mins[0])
    hour_dropdown = tkinter.OptionMenu(frame, hour_var, *hours)
    min_dropdown = tkinter.OptionMenu(frame, min_var, *mins)
    hour_dropdown.pack(side='left')
    min_dropdown.pack(side='right')
    setalarm = tkinter.Button(text="Set Alarm", command=lambda: start_thread(hour_var, min_var))
    setalarm.pack(padx=0, pady=20)


def start_thread(hour_var, min_var):
    threading.Thread(target=play_alarm, args=(hour_var, min_var)).start()


if _name_ == '_main_':
    fontt = font.Font(family="Ariel", size=20, underline=True)
    c = tkinter.Label(window, font=fontt, fg='red')
    c.pack(side='top')
    realtime()
    user_interface()
    text = tkinter.Text(window, width=60, height=17)
    text.pack(padx=50, pady=0)
    clear = tkinter.Button(window, text='Clear Screen', command=lambda :text.delete(1.0, tkinter.END))
    clear.pack(pady=20)
    window.mainloop()

