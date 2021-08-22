from tkinter import *
def hi_fun1():
    print("hello Candy")
    display.config(text = "hi", fg = "#001970", bg = "#6A8BFF")
def hi_fun2():
    print("hello Candy")
    display.config(text = "hi", fg = "green", bg = "white")
windows = Tk()
windows.title("Candy")
btn1 = Button(windows, text = "show screen", command = hi_fun1)
btn1.pack()
btn2 = Button(windows, text = "clear screen", command = hi_fun2)
btn2.pack()
display = Label(windows,text = "hi", fg = "#B7FFDC", bg = "#FFFFDC")
display.pack()
windows.mainloop()