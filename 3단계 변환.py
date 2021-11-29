#######기본 명령어
import tkinter
import time
window=tkinter.Tk()
window.geometry("1000x1000")
window.title("Veginner")
window.resizable(True, True)
text=tkinter.Text(window)

######기둥들과 사각형하나 이미지 불러오기 (사각형 이미지 하나 수정 필요)-사각형별 이미지 조정 필요
image1=tkinter.PhotoImage(file="빨간기둥1.png")
label1=tkinter.Label(window, image=image1)
label1.pack()

image2=tkinter.PhotoImage(file="노란기둥1.png")
label2=tkinter.Label(window, image=image2)
label2.pack()

image3=tkinter.PhotoImage(file="초록기둥1.png")
label3=tkinter.Label(window, image=image3)
label3.pack()

image0=tkinter.PhotoImage(file="sqe.png")
label0=tkinter.Label(window, image=image0)
label0.pack()


####흰 사각형 위치
label0.place(x=100, y=500)

####for문을 이용해 0.01초마다 사각형 위치 바꿔서 이동
for i in range(1, 50):
    label1.place(x=100, y=1000/i+300)########   +뒤에 오는 값들은 앞선 코드에서 불러온 정보들을 이용해서 계산 추후 수정 필요
    window.update()
    time.sleep(0.01)
    label2.place(x=219, y=1000 / i + 250)
    window.update()
    time.sleep(0.01)
    label3.place(x=340, y=1000 / i + 250)
    window.update()
    time.sleep(0.01)


####텍스트 출력
label=tkinter.Label(window, text="Good Job!", font=("Times", "16"))  #####텍스트, 폰트, 크기가 있음. 위치 조정 필요, if문 이용한 상황별 메세지 출력 필요.
label.pack()

######메뉴 돌아가는 버튼 제작 필요

window.mainloop()