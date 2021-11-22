# opensource_scene2
# 사진 파일의 크기에 오류가 있어 무작위로 사진을 넣었으니, 요리와 재료 종류는 무관합니다.

from tkinter import *
from PIL import Image

# 상희 : scene1 배치

window = Tk()
window.title("Veginner")

def press1():
    button.destroy()
    btn.pack()

def press2():
    window.destroy()

button = Button(window, text='Hi Veginner! 이번 단계의 요리 공개!', command=press1)
button.pack(side=TOP)
photo = PhotoImage(file="가지_moza.png")
btn = Button(window, width=200, height=200, image=photo, command=press2)
window.mainloop()


def pressed():
    window.quit()
    window.destroy()


window = Tk()
window.geometry("1000x1000")
window.title("재료 고르기")


# 아래 함수들과 버튼 작업은 단순 반복문의 경우와 다름 - 클래스 구현 시에 이 부분을 참고해서 구현해야함을 염두에 두어야 합니다.
# 해당 이미지를 클릭하면 이미지에 맞는 버튼이 등장하고, 그 버튼을 누르면 구현한 프로그램 마침.

def ingredient1():
    ibtn = Button(window, text="고추를 어떻게 요리하시겠습니까?", command=press2)
    ibtn.grid(row=1, column=0)

    # 그 재료를 어떻게 할 지 보여주는 화면으로 추후에 전환 필요
    # EX. 썰기/볶기 등 -> 이 과정에서 고건 : 점수 책정/누적 코드 들어와야 함.


def ingredient2():
    ibtn = Button(window, text="달걀을 어떻게 요리하시겠습니까?", command=press2)
    ibtn.grid(row=1, column=1)


def ingredient3():
    ibtn = Button(window, text="감자를 어떻게 요리하시겠습니까?", command=press2)
    ibtn.grid(row=1, column=2)


def ingredient4():
    ibtn = Button(window, text="고등어를 어떻게 요리하시겠습니까?", command=press2)
    ibtn.grid(row=1, column=3)


def ingredient5():
    ibtn = Button(window, text="당근 어떻게 요리하시겠습니까?", command=press2)
    ibtn.grid(row=1, column=4)


photo1 = PhotoImage(file="고추2_moza.png")
btn1 = Button(window, width=200, height=200, image=photo1, command=ingredient1)
btn1.grid(row=0, column=0)

photo2 = PhotoImage(file="달걀_moza.png")
btn2 = Button(window, width=200, height=200, image=photo2, command=ingredient2)
btn2.grid(row=0, column=1)

photo3 = PhotoImage(file="감자_moza.png")
btn3 = Button(window, width=200, height=200, image=photo3, command=ingredient3)
btn3.grid(row=0, column=2)

photo4 = PhotoImage(file="고등어조림2_moza.png")
btn4 = Button(window, width=200, height=200, image=photo4, command=ingredient4)
btn4.grid(row=0, column=3)

photo5 = PhotoImage(file="당근_moza.png")
btn5 = Button(window, width=200, height=200, image=photo5, command=ingredient5)
btn5.grid(row=0, column=4)

# btn7 = Button(window, text="다음 단계로", command=pressed)
# btn7.pack(pady=30)


window.mainloop()
