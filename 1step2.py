# opensource_scene1&2
from tkinter import *
#from PIL import Image
window = Tk()
window.title("Veginner")

def next_level() :
    btn.destroy()
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()
    btn4.destroy()
    window.destroy()
# window.title("재료 고르기")

def press1() :
    button.destroy()
    btn.pack(side=TOP)
    btn1.pack()
    btn2.pack()
    btn3.pack()
    btn4.pack(side=BOTTOM)

def press2():
    next_level()


photo = PhotoImage(file="select-graphic/starticon.png")
button = Button(window, width=400, height=400, image=photo, command=press1)
button.grid(row=0, column=1)

photo1 = PhotoImage(file="select-graphic/Pollo-vegetarian.png")
btn = Button(window, width=710, height=90, image=photo1, command=press2)

photo2 = PhotoImage(file="select-graphic/Pesco-vegetarian.png")
btn1 = Button(window, width=710, height=90, image=photo2, command=press2)

photo3 = PhotoImage(file="select-graphic/Lacto-ovo-vegetarian.png")
btn2 = Button(window, width=710, height=90, image=photo3, command=press2)

photo4 = PhotoImage(file="select-graphic/Ovo-vegetarian.png")
btn3 = Button(window, width=710, height=90, image=photo4, command=press2)

photo5 = PhotoImage(file="select-graphic/Vegan.png")
btn4 = Button(window, width=710, height=90, image=photo5, command=press2)
 
window.mainloop()

window = Tk()
window.geometry("1000x1000")
window.title("Veginner")

def press1() :
    button.destroy()
    btn.pack()

def press2() :
    window.destroy()

button = Button(window, text='Hi Veginner! 이번 단계의 요리 공개!', command=press1)
button.pack(side=TOP)

photo = PhotoImage(file="mosaic/고등어조림01.png")
btn = Button(window, width=200, height=200, image=photo, command=press2)
window.mainloop()

def pressed() :
    window.quit()
    window.destroy()

window = Tk()
window.geometry("1000x1000")
window.title("재료 고르기")

#아래 함수들과 버튼 작업은 단순 반복문의 경우와 다름 - 클래스 구현 시에 이 부분을 참고해서 구현해야 함을 염두에 두어야 합니다
def ingredient1() :
    ibtn = Button(window, text="고추를 어떻게 요리하시겠습니까?", command=press2)
    ibtn.grid(row=1, column=0)
    #그 재료를 어떻게 할 지 보여주는 화면으로 전환
    #EX. 썰기/볶기 등

def ingredient2() :
    ibtn = Button(window, text="생수를 어떻게 사용하시겠습니까?", command=press2)
    ibtn.grid(row=1, column=1)

def ingredient3() :
    ibtn = Button(window, text="무를 어떻게 요리하시겠습니까?", command=press2)
    ibtn.grid(row=1, column=2)

def ingredient4() :
    ibtn = Button(window, text="고등어를 어떻게 요리하시겠습니까?", command=press2)
    ibtn.grid(row=1, column=3)

def ingredient5() :
    ibtn = Button(window, text="당근을 어떻게 요리하시겠습니까?", command=press2)
    ibtn.grid(row=1, column=4)

photo1 = PhotoImage(file="mosaic/고추2_moza.png")
btn1 = Button(window, width=200, height=200, image=photo1, command=ingredient1)
btn1.grid(row=0, column=0)

photo2 = PhotoImage(file="mosaic/물_moza.png")
btn2 = Button(window, width=200, height=200, image=photo2, command=ingredient2)
btn2.grid(row=0, column=1)

photo3 = PhotoImage(file="mosaic/무_moza.png")
btn3 = Button(window, width=200, height=200, image=photo3, command=ingredient3)
btn3.grid(row=0, column=2)

photo4 = PhotoImage(file="mosaic/고등어조림2_moza.png")
btn4 = Button(window, width=200, height=200, image=photo4, command=ingredient4)
btn4.grid(row=0, column=3)

photo5 = PhotoImage(file="mosaic/당근_moza.png")
btn5 = Button(window, width=200, height=200, image=photo5, command=ingredient5)
btn5.grid(row=0, column=4)
# btn7 = Button(window, text="다음 단계로", command=pressed)
# btn7.pack(pady=30)

window.mainloop()
window = Tk()
window.geometry("1000x1000")

def todo1() :
    butt1.destroy()
    ibutt = Button(window, text="다지기 선택!", command=press2)
    ibutt.grid(row=3, column=3)
    butt = Button(window, text="다지기 완료!", command=press2)
    butt.grid(row=1, column=3)

def todo2() :
    butt2.destroy()
    ibutt = Button(window, text="볶기 선택!", command=press2)
    ibutt.grid(row=3, column=3)
    butt = Button(window, text="볶기 완료!", command=press2)
    butt.grid(row=1, column=3)

photo01 = PhotoImage(file="mosaic/채썰기,다지기_moza.png")
butt1 = Button(window, width=200, height=200, image=photo01, command=todo1)
butt1.grid(row=0, column=1)

photo02 = PhotoImage(file="mosaic/볶기_moza.png")
butt2 = Button(window, width=200, height=200, image=photo02, command=todo2)
butt2.grid(row=0, column=2)


window.mainloop()