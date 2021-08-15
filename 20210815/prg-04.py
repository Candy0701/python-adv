from tkinter import *
def hi_fun():
    print("hello Candy")
    display.config(text = "hi", fg = "#001970", bg = "#6A8BFF")
windows = Tk()
windows.title("Candy")
btn = Button(windows, text = "click me", command = hi_fun)
btn.pack()
display = Label(windows,text = "hi", fg = "#B7FFDC", bg = "#FFFFDC")
display.pack()
windows.mainloop()
