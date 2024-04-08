import tkinter as tk #GUI-->>Graphical User Interface
from time import strftime

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

root = tk.Tk()
root.title('Digital Clock')
root.geometry('300x100')

label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
label.pack(anchor='center')

time()
root.mainloop()
