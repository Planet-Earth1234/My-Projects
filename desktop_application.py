from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import asksaveasfilename, askopenfilename

file_path = ""
window = Tk()
window.geometry("450x600")
window.title ("My Fanastic Notelab")
window.config(bg = "black")


def set_file_path(path):
    global file_path
    file_path = path

def save_as (path):
    if file_path == "":
        path = asksaveasfilename(filetypes=[("AllTypes","*.*"),("TextTypes","*.txt")])
    else:
        file_path = path

    with open(file_path, "w") as file:
        code = file.write()
        code1 = window.open(file_path)
        set_file_path(path)
def open(path):
    if file_path == ""  :
        path = askopenfilename([("AllTypes","*.*"), ("TextTypes","*.txt")])
    else:
        file_path = path

    with open(file_path, "w") as file:
        code = file.write()
        code1 = window.open(file_path) 
        set_file_path(path)

menu1 = Menu(window)
menu2 = Menu (window)
filemenu = Menu(menu1, tearoff = 0)
filemenu.add_command(label = "SAVE AS",command = save_as )
filemenu.add_command(label = "SAVE ",command = save_as )
filemenu.add_command(label = "Exit",command = exit)
filemenu.add_command(label = "Open",command = open )
menu1.add_cascade(label = "File", menu= filemenu)



mbtn = Menubutton(text='Text')
mbtn.pack()


frame = Frame(window)
frame.pack(padx = 10, pady = 5, anchor = "nw")
editor = Text(window)
editor.pack(window, height = 100, width = 100)

window.mainloop()





