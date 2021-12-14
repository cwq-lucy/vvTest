import pyautogui as auto
import cv2
import numpy as np
import  pyautogui
import time
import  unittest
# try:
#     number7_location = auto.locateOnScreen('../source_photoes/login_gui.png')   #传入按钮的图片
#     print(number7_location)  # 返回屏幕所在位置
#     x,y = auto.center(number7_location)  # 转化为 x,y坐标
#     print(x,y)  #按键7的坐标是1441,582
#     auto.click(number7_location)
#     # 点击坐标，click()它是支持元组格式的坐标传入的
#
# except:
#     print("找不到图片")


###
#image图像比较
###
#@unittest.skip("skipping")
class TestPC(unittest.TestCase):
    @unittest.skip("skipping")
    def test01(self):
        image1 = cv2.imread("../source_photoes/login.png")
        image2 = cv2.imread("../Photoes/login_button.png")

        difference = cv2.subtract(image1, image2)
        print(difference)
        result = not np.any(difference)
        print(result)

    #@unittest.skip("skipping")
    def test02(self):
        try:
            while 1:
                time.sleep(10)
                x, y = pyautogui.position()
                print(x,y)
        except:
            pass

if __name__ == '__main__':
    unittest.main() # unittest 的执行