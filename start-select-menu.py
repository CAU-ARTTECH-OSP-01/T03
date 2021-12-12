# opensource_scene1
from tkinter import *
#from PIL import Image

window = Tk()
window.title("Veginner")

def next_level(): # 다음 창으로 고고
    btn.destroy()
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()
    btn4.destroy()
    window.geometry("1000x1000")
    window.title("단계 고르기")

def press1():
    button.destroy()
    btn.pack(side=TOP)
    btn1.pack()
    btn2.pack()
    btn3.pack()
    btn4.pack(side=BOTTOM)

def press2():
    next_level()

def press3():
    next_level()

def press4():
    next_level()

def press5():
    next_level()

def press6():
    next_level()


photo = PhotoImage(file="select-graphic/starticon.png")
button = Button(window, width=400, height=400, image=photo, command=press1)
button.grid(row=0, column=1)

photo1 = PhotoImage(file="select-graphic/Pollo-vegetarian.png")
btn = Button(window, width=710, height=90, image=photo1, command=press2)

photo2 = PhotoImage(file="select-graphic/Pesco-vegetarian.png")
btn1 = Button(window, width=710, height=90, image=photo2, command=press3)

photo3 = PhotoImage(file="select-graphic/Lacto-ovo-vegetarian.png")
btn2 = Button(window, width=710, height=90, image=photo3, command=press4)

photo4 = PhotoImage(file="select-graphic/Ovo-vegetarian.png")
btn3 = Button(window, width=710, height=90, image=photo4, command=press5)

photo5 = PhotoImage(file="select-graphic/Vegan.png")
btn4 = Button(window, width=710, height=90, image=photo5, command=press6)

window.mainloop()
