#opensource_전체 코드 클래스화 : png는 추후 그래픽 파일 완성시 변경하겠습니다.
#기존 코드&앞으로 구현될 코드 - 별도로 작업 중
#클래스화 병행 - 클래스 코드는 이 파일에 누적 업데이트할 예정입니다.
#***이미지 경로 - 깃허브가 기준이 되어야 합니다! 절대 개인 컴퓨터 경로로 바꾸지 말아주세요!***

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

class Start(tk.Frame): #구현 중