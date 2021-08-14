# -*- coding: utf-8 -*-
"""

Created on Thu Apr 23 02:25:45 2020

@author: agent-home
"""
import tkinter as tk
from datetime import datetime

def cont():
    btn1.grid_forget()
    btn2.grid_forget()
    stop_but.grid(row=1, columnspan=2, sticky="ew")
    tick()

def reset():
    global temp
    btn1.grid_forget()
    btn2.grid_forget()
    temp = 0
    label1.configure(text="00:00")
    start_but.grid(row=1, columnspan=2, sticky="ew")

def stop_sw():
    stop_but.grid_forget()
    btn1.grid(row=1, column=0, sticky="ew")
    btn2.grid(row=1, column=1, sticky="ew")
    root.after_cancel(after_id)

def tick():
    global temp, after_id
    after_id = root.after(1000, tick)
    f_temp = datetime.fromtimestamp(temp).strftime("%M:%S")
    label1.configure(text=str(f_temp))
    temp +=1

def start_sw():
    start_but.grid_forget()
    stop_but.grid(row=1, columnspan=2, sticky="ew")
    tick()

temp = 0
after_id = ''

root= tk.Tk()
root.title("секундомер")
root.configure(bg="black")

label1 = tk.Label(root, width=7, font=('Ubuntu', 100), text="00:00")
label1.grid(row=0, columnspan=2, padx=2, pady=2)

start_but = tk.Button(text="Старт", font=('Ubuntu', 30), command=start_sw)
stop_but = tk.Button(text="Стоп", font=('Ubuntu', 30), command=stop_sw)
btn1 = tk.Button(text="Продолжить", font=('Ubuntu', 30), command=cont)
btn2 = tk.Button(text="Сброс", font=('Ubuntu', 30), command=reset)

start_but.grid(row=1, columnspan=2, sticky="ew")

root.mainloop()
