from tkinter import *


def paint_red():
    print("red")
    print("#ff0000")
    label_color_name.config(fg="red", text="red")
    entry_color_code.config(bg="red")
    entry_color_code.delete(0, END)
    entry_color_code.insert(0, "#ff0000")


def paint_orange():
    print("orange")
    print("#ff7d00")
    label_color_name.config(fg="orange", text="orange")
    entry_color_code.config(bg="orange")
    entry_color_code.delete(0, END)
    entry_color_code.insert(0, "#ff7d00")


def paint_yellow():
    print("yellow")
    print("#ffff00")
    label_color_name.config(fg="yellow", text="yellow")
    entry_color_code.config(bg="yellow")
    entry_color_code.delete(0, END)
    entry_color_code.insert(0, "#ffff00")


def paint_green():
    print("green")
    print("#00ff00")
    label_color_name.config(fg="green", text="green")
    entry_color_code.config(bg="green")
    entry_color_code.delete(0, END)
    entry_color_code.insert(0, "#00ff00")


def paint_lightblue():
    print("lightblue")
    print("007dff")
    label_color_name.config(fg="lightblue", text="lightblue")
    entry_color_code.config(bg="lightblue")
    entry_color_code.delete(0, END)
    entry_color_code.insert(0, "#007dff")


def paint_blue():
    print("blue")
    print("0000ff")
    label_color_name.config(fg="blue", text="blue")
    entry_color_code.config(bg="blue")
    entry_color_code.delete(0, END)
    entry_color_code.insert(0, "#0000ff")


def paint_purple():
    print("purple")
    print("7d00ff")
    label_color_name.config(fg="purple", text="purple")
    entry_color_code.config(bg="purple")
    entry_color_code.delete(0, END)
    entry_color_code.insert(0, "#7d00ff")


root = Tk()
root.title("Colors")
label_color_name = Label(root, text="Color name")
label_color_name.pack()
entry_color_code = Entry(root, width=30, font=20, justify=CENTER)
entry_color_code.insert(0, "Color code")
entry_color_code.pack()
button_red = Button(bg="#ff0000", width=30, text="1", command=paint_red)
button_red.pack(fill=X)
button_orange = Button(bg="#ff7d00", width=30, text="2", command=paint_orange)
button_orange.pack(fill=X)
button_yellow = Button(bg="#ffff00", width=30, text="3", command=paint_yellow)
button_yellow.pack(fill=X)
button_green = Button(bg="#00ff00", width=30, text="4", command=paint_green)
button_green.pack(fill=X)
button_lightblue = Button(bg="#007dff", width=30, text="5", command=paint_lightblue)
button_lightblue.pack(fill=X)
button_blue = Button(bg="#0000ff", width=30, text="6", command=paint_blue)
button_blue.pack(fill=X)
button_purple = Button(bg="#7d00ff", width=30, text="7", command=paint_purple)
button_purple.pack(fill=X)
root.mainloop()
