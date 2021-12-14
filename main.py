# opensource_scene1&2
from tkinter import *
import time

# from PIL import Image
window = Tk()
window.title("Veginner")


def next_level():
    btn.destroy()
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()
    btn4.destroy()
    window.destroy()


# window.title("재료 고르기")

def press1():
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


def press1():
    button.destroy()
    btn.pack()


def press2():
    window.destroy()


button = Button(window, text='Hi Veginner! 이번 단계의 요리 공개!', command=press1)
button.pack(side=TOP)

photo = PhotoImage(file="mosaic/고등어조림01.png")
btn = Button(window, width=200, height=200, image=photo, command=press2)
start = time.time()#########################################################################################시간 감점요소  시간시작
ingri = [0, 1, 2, 3]   ####################################################################################### 요리재료 감점용 정답 리스트
useringr = [0]    ########################################################################################## 사용자가 넣을 요리재료 리스트
window.mainloop()


def pressed():
    window.quit()
    window.destroy()


window = Tk()
window.geometry("1000x1000")
window.title("재료 고르기")



# 아래 함수들과 버튼 작업은 단순 반복문의 경우와 다름 - 클래스 구현 시에 이 부분을 참고해서 구현해야 함을 염두에 두어야 합니다
def ingredient1():
    ibtn = Button(window, text="고추를 어떻게 요리하시겠습니까?", command=press2)
    ibtn.grid(row=1, column=0)
    useringr.append(1)########################################################################################재료 하나 선택할때마다 리스트에 추가
    # 그 재료를 어떻게 할 지 보여주는 화면으로 전환
    # EX. 썰기/볶기 등


def ingredient2():
    ibtn = Button(window, text="생수를 어떻게 사용하시겠습니까?", command=press2)
    ibtn.grid(row=1, column=1)
    useringr.append(2)#############


def ingredient3():
    ibtn = Button(window, text="무를 어떻게 요리하시겠습니까?", command=press2)
    ibtn.grid(row=1, column=2)
    useringr.append(3)##############


def ingredient4():
    ibtn = Button(window, text="고등어를 어떻게 요리하시겠습니까?", command=press2)
    ibtn.grid(row=1, column=3)
    useringr.append(4)############


def ingredient5():
    ibtn = Button(window, text="당근을 어떻게 요리하시겠습니까?", command=press2)
    ibtn.grid(row=1, column=4)
    useringr.append(5)##############



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


def todo1():
    butt1.destroy()
    ibutt = Button(window, text="다지기 선택!", command=press2)
    ibutt.grid(row=3, column=3)
    butt = Button(window, text="다지기 완료!", command=press2)
    butt.grid(row=1, column=3)


def todo2():
    butt2.destroy()
    ibutt = Button(window, text="볶기 선택!", command=press2)
    ibutt.grid(row=3, column=3)
    butt = Button(window, text="볶기 완료!", command=press2)
    butt.grid(row=1, column=3)

######################################################################################################################요리재료 감점 리스트 비교하기
ie=0
for i in ingri :
    if i not in useringr :
        print("useringri not containing :")
        ie+=1
for i in useringr :
    if i not in ingri  :
        print("ingri not containing :")
        ie+=1

print(ie)

########################################################################################################################감점
e = 0
photo01 = PhotoImage(file="mosaic/채썰기,다지기_moza.png")
butt1 = Button(window, width=200, height=200, image=photo01, command=todo1)
butt1.grid(row=0, column=1)

photo02 = PhotoImage(file="mosaic/볶기_moza.png")
butt2 = Button(window, width=200, height=200, image=photo02, command=todo2)
butt2.grid(row=0, column=2)
window.mainloop()
###############################################################################################3단계


t=time.time() - start
print(t)
t1=t/600
window = Tk()
window.geometry("1000x1000")
window.resizable(True, True)
text = Text(window)

######기둥들과 사각형하나 이미지 불러오기 (사각형 이미지 하나 수정 필요)-사각형별 이미지 조정 필요
image1 = PhotoImage(file="sqr\빨간기둥1.png", master=window)
label1 = Label(window, image=image1)
label1.pack()

image2 = PhotoImage(file="sqr\노란기둥1.png", master=window)
label2 = Label(window, image=image2)
label2.pack()

image3 = PhotoImage(file="sqr\초록기둥1.png", master=window)
label3 = Label(window, image=image3)
label3.pack()

image0 = PhotoImage(file="sqr\sqe.png", master=window)
label0 = Label(window, image=image0)
label0.pack()

####흰 사각형 위치
label0.place(x=100, y=500)

####for문을 이용해 0.01초마다 사각형 위치 바꿔서 이동
for i in range(1, 50):
    label1.place(x=100, y=1000 / i + 220+50*ie)  ########  ie값 맞춰서 요리재료에 따른 사각형 줄어듬
    window.update()
    time.sleep(0.01)
    label2.place(x=219, y=1000 / i + 220)  ##############################################################################요리방범 아직 미구현
    window.update()
    time.sleep(0.01)
    label3.place(x=340, y=1000 / i + 220 +50*t1)  #########시간에 따른 600초마다 y 50만큼 감점
    window.update()
    time.sleep(0.01)

####텍스트 출력
label111 = Label(window, text=" GOOD JOB", font=("Times", "30"))
label11 = Label(window, text=" 토마토로 만든 참치, 가지로 만든 대체 장어 등 ‘식물 기반 대체 해산물 식품’ 분야가 새롭게 주목받고 있다.", font=("Times", "10"))  #####텍스트, 폰트, 크기가 있음. 위치 조정 필요, if문 이용한 상황별 메세지 출력 필요.
label22 = Label(window, text=" 이미 미국에서는 식물 기반 대체식품 중 약 29%를 대체 해산물이 차지할 정도로 널리 사용되고 있다.", font=("Times", "10"))
label33 = Label(window, text=" 해양 생태계 파괴나 중금속 및 미세 플라스틱 섭취 문제 등을 해결하기 위해 개발된 만큼 환경에 대한 경각심을 가지며", font=("Times", "10"))
label44 = Label(window, text=" 대체 해산물을 적극적으로 소비할 수 있게 되길 바란다.", font=("Times", "10"))
label111.pack()
label111.place(x=250, y=100)

label11.pack()
label11.place(x=470, y=300)
label22.pack()
label22.place(x=470, y=330)
label33.pack()
label33.place(x=470, y=360)
label44.pack()
label44.place(x=470, y=390)
######메뉴 돌아가는 버튼 제작 필요


window.mainloop()