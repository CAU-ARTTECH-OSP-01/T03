# opensource_scene1&2
from tkinter import *

# from PIL import Image
window = Tk()
window.title("Veginner")


def next_level_pollo():
    btn_pollo.destroy()
    btn_pesco.destroy()
    btn_lacto_ovo.destroy()
    btn_ovo.destroy()
    btn_vegan.destroy()
    new_menu()

    def press_next():
        btn_open_menu.destroy()

        def fishdish():
            btn_fishdish.destroy()
            btn_chicken.destroy()

            def press2():
                window.destroy()

            def ingredient1():
                ibtn = Button(window, text="양파를 어떻게 요리하시겠습니까?", command=press2)
                ibtn.grid(row=0, column=0)
                # 그 재료를 어떻게 할 지 보여주는 화면으로 전환
                # EX. 썰기/볶기 등

            def ingredient2():
                ibtn = Button(window, text="고추를 어떻게 사용하시겠습니까?", command=press2)
                ibtn.grid(row=0, column=1)

            def ingredient3():
                ibtn = Button(window, text="대파를 어떻게 요리하시겠습니까?", command=press2)
                ibtn.grid(row=0, column=2)

            def ingredient4():
                ibtn = Button(window, text="무를 어떻게 요리하시겠습니까?", command=press2)
                ibtn.grid(row=0, column=3)

            def ingredient5():
                ibtn = Button(window, text="아보카도를 어떻게 요리하시겠습니까?", command=press2)
                ibtn.grid(row=0, column=4)
                # 그 재료를 어떻게 할 지 보여주는 화면으로 전환
                # EX. 썰기/볶기 등

            def ingredient6():
                ibtn = Button(window, text="손질된 고등어를 어떻게 사용하시겠습니까?", command=press2)
                ibtn.grid(row=1, column=0)

            def ingredient7():
                ibtn = Button(window, text="새우를 어떻게 요리하시겠습니까?", command=press2)
                ibtn.grid(row=1, column=1)

            def ingredient8():
                ibtn = Button(window, text="물을 어떻게 요리하시겠습니까?", command=press2)
                ibtn.grid(row=1, column=2)

            def ingredient9():
                ibtn = Button(window, text="피자치즈를 어떻게 요리하시겠습니까?", command=press2)
                ibtn.grid(row=1, column=3)

            def ingredient10():
                ibtn = Button(window, text="양념를 어떻게 요리하시겠습니까?", command=press2)
                ibtn.grid(row=1, column=4)



            photo1 = PhotoImage(file="mosaic/양파_moza.png")
            btn1 = Button(window, width=200, height=200, image=photo1, command=ingredient1)
            btn1.grid(row=0, column=0)

            photo2 = PhotoImage(file="mosaic/고추2_moza.png")
            btn2 = Button(window, width=200, height=200, image=photo2, command=ingredient2)
            btn2.grid(row=0, column=1)

            photo3 = PhotoImage(file="mosaic/대파,쪽파_moza.png")
            btn3 = Button(window, width=200, height=200, image=photo3, command=ingredient3)
            btn3.grid(row=0, column=2)

            photo4 = PhotoImage(file="mosaic/무_moza.png")
            btn4 = Button(window, width=200, height=200, image=photo4, command=ingredient4)
            btn4.grid(row=0, column=3)

            photo5 = PhotoImage(file="mosaic/아보카도_moza.png")
            btn5 = Button(window, width=200, height=200, image=photo5, command=ingredient5)
            btn5.grid(row=0, column=4)

            photo6 = PhotoImage(file="mosaic/생선_moza.png") #손질된 고등어
            btn6 = Button(window, width=200, height=200, image=photo6, command=ingredient6)
            btn6.grid(row=1, column=0)

            photo7 = PhotoImage(file="mosaic/해산물_moza.png") #새우
            btn7 = Button(window, width=200, height=200, image=photo7, command=ingredient7)
            btn7.grid(row=1, column=1)

            photo8 = PhotoImage(file="mosaic/물_moza.png")
            btn8 = Button(window, width=200, height=200, image=photo8, command=ingredient8)
            btn8.grid(row=1, column=2)

            photo9 = PhotoImage(file="mosaic/크림치즈_moza.png") #피자치즈
            btn9 = Button(window, width=200, height=200, image=photo9, command=ingredient9)
            btn9.grid(row=1, column=3)

            photo10 = PhotoImage(file="mosaic/케첩_moza.png") #양념
            btn10 = Button(window, width=200, height=200, image=photo10, command=ingredient10)
            btn10.grid(row=1, column=4)

            window.mainloop()

        def chicken():
            btn_chicken.destroy()
            btn_fishdish.destroy()

        photo_fishdish = PhotoImage(file="mosaic/고등어조림01.png")
        btn_fishdish = Button(window, width=200, height=200, image=photo_fishdish, command=fishdish)
        btn_fishdish.pack()

        photo_chicken = PhotoImage(file="mosaic/고등어조림01.png")  # 찜닭
        btn_chicken = Button(window, width=200, height=200, image=photo_chicken, command=chicken)
        btn_chicken.pack()

        window.mainloop()

    btn_open_menu = Button(window, text='Hi Veginner! 이번 단계의 요리 공개!', command=press_next)
    btn_open_menu.pack(side=TOP)


def next_level_pesco():
    btn_pollo.destroy()
    btn_pesco.destroy()
    btn_lacto_ovo.destroy()
    btn_ovo.destroy()
    btn_vegan.destroy()
    new_menu()


def next_level_lacto_ovo():
    btn_pollo.destroy()
    btn_pesco.destroy()
    btn_lacto_ovo.destroy()
    btn_ovo.destroy()
    btn_vegan.destroy()
    new_menu()


def next_level_ovo():
    btn_pollo.destroy()
    btn_pesco.destroy()
    btn_lacto_ovo.destroy()
    btn_ovo.destroy()
    btn_vegan.destroy()
    new_menu()


def next_level_vegan():
    btn_pollo.destroy()
    btn_pesco.destroy()
    btn_lacto_ovo.destroy()
    btn_ovo.destroy()
    btn_vegan.destroy()
    new_menu()


# window.title("재료 고르기")

def press1():
    button.destroy()
    btn_pollo.pack(side=TOP)
    btn_pesco.pack()
    btn_lacto_ovo.pack()
    btn_ovo.pack()
    btn_vegan.pack(side=BOTTOM)


def new_menu():
    window.geometry("1000x1000")
    window.title("Veginner")


photo = PhotoImage(file="select-graphic/starticon.png")
button = Button(window, width=400, height=400, image=photo, command=press1)
button.grid(row=0, column=1)

photo_pollo = PhotoImage(file="select-graphic/Pollo-vegetarian.png")
btn_pollo = Button(window, width=710, height=90, image=photo_pollo, command=next_level_pollo)

photo_pesco = PhotoImage(file="select-graphic/Pesco-vegetarian.png")
btn_pesco = Button(window, width=710, height=90, image=photo_pesco, command=next_level_pesco)

photo_lacto_ovo = PhotoImage(file="select-graphic/Lacto-ovo-vegetarian.png")
btn_lacto_ovo = Button(window, width=710, height=90, image=photo_lacto_ovo, command=next_level_lacto_ovo)

photo_ovo = PhotoImage(file="select-graphic/Ovo-vegetarian.png")
btn_ovo = Button(window, width=710, height=90, image=photo_ovo, command=next_level_ovo)

photo_vegan = PhotoImage(file="select-graphic/Vegan.png")
btn_vegan = Button(window, width=710, height=90, image=photo_vegan, command=next_level_vegan)

window.mainloop()


def pressed():
    window.quit()
    window.destroy()
