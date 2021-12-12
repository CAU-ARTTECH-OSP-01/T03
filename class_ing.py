#opensource_전체 코드 클래스화 : png는 추후 그래픽 파일 완성시 변경하겠습니다.
#기존 코드&앞으로 구현될 코드 - 별도로 작업 중
#클래스화 병행 - 클래스 코드는 이 파일에 누적 업데이트할 예정입니다.
#***이미지 경로 - 깃허브가 기준이 되어야 합니다! 절대 개인 컴퓨터 경로로 바꾸지 말아주세요!***
#각 클래스가 유기적으로 연결 - 개별 함수, 개별 클래스를 실행한다고 단독 코드가 작동하는 것이 아님

import tkinter as tk
from PIL import Image
from functools import partial
from enum import Enum

class Vege(Enum):
    POLLO = 0
    PESCO = 1  
    LACTO_OVO = 2
    OVO = 3
    VEGAN = 4

sizeString = "1200x700+200+80"

VegeterianImageNameList = ["select-graphic/Pollo-vegetarian.png","select-graphic/Pesco-vegetarian.png","select-graphic/Lacto-ovo-vegetarian.png","select-graphic/Ovo-vegetarian.png","select-graphic/Vegan.png"]
IngredientimageNameList = [["mosaic/당근_moza.png","mosaic/감자_moza.png","mosaic/고추2_moza.png","mosaic/고등어조림2_moza.png","mosaic/무_moza.png"], #1단계
["mosaic/당근_moza.png","mosaic/감자_moza.png","mosaic/당근_moza.png"], #2단계
["mosaic/당근_moza.png","mosaic/감자_moza.png","mosaic/당근_moza.png"], #3단계
["mosaic/당근_moza.png","mosaic/감자_moza.png","mosaic/당근_moza.png"], #4단계
["mosaic/당근_moza.png","mosaic/감자_moza.png","mosaic/당근_moza.png"]] #5단계
currentSelect = {'Vege' : Vege.POLLO,
'Ingredient' : 0,
'Trim' : 0}

class SampleSample(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        tk.Tk.geometry(self,"1200x700+200+80")
        self._frame = None
        self.switch_frame(Start)

def switch_frame(self, frame_class):
    new_frame = frame_class(self)
    if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class Start(tk.Frame): #스타트 버튼 클릭하면
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.StartImage = tk.PhotoImage(file="select-graphic/starticon.png",master=self)
        self.StartButton = tk.Button(self, width=400, height=400, image=self.StartImage, command=lambda: master.switch_frame(Vegeterian))
        self.StartButton.grid(row=0, column=1)

class Vegeterian(tk.Frame): #단계 선택으로 창 전환 가능
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.VegeterianCnt = 5 #리스트 받아옴
        self.VegeterianImgList = []
        self.VegeterianBtnList = []

        for i in range(self.VegeterianCnt): #따라서 반복문 사용 가능 - 가시성이 떨어지는 코드 삭제할 수 있도록
            self.VegeterianImgList.append(tk.PhotoImage(file=VegeterianImageNameList[i],master=self).subsample(2))
            self.VegeterianBtnList.append(tk.Button(self,width=710, height=90, image=self.VegeterianImgList[i], command=partial(self.onClick,master,str(i))))
            self.VegeterianBtnList[i].grid(row=i, column=0)

    def onClick(self,master,index):
        currentSelect["Vege"] = index
        master.switch_frame(SelectAndGo)


class SelectAndGo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        # Open Button
        self.Openbutton = tk.Button(self, text='Hi Veginner! ' + str(currentSelect["Vege"] + '번 단계의 요리 공개!'),
                                    command=self.onClickChallenge)
        self.Openbutton.pack(anchor="center")
        # Openbutton.bind("<Button-1>", SelectAndGo.onClickChallenge)

        # Food Button
        self.FoodImage = tk.PhotoImage(file="mosaic/고등어조림2_moza.png", master=self) #이미지는 그래픽 완료 후 변경
        self.FoodBtn = tk.Button(self, padx=10, pady=10, image=self.FoodImage,
                                 command=lambda: master.switch_frame(SelectMaterial))

    def onClickChallenge(self):
        self.Openbutton.destroy()
        self.FoodBtn.pack()

class SelectMaterial(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.meterialCnt = 3
        self.materialImageList = []
        self.materialButtonList = []
        
        # material image button
        for i in range(self.meterialCnt):
            self.materialImageList.append(tk.PhotoImage(file=imageNameList[0][i], master=self).subsample(2)) #ing