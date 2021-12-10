# coding:utf-8
import time
import pyautogui
import  unittest
import cv2
import numpy as np
import pyautogui as auto

class testOPlayer(unittest.TestCase):

    def login(self):
        # 移至应用程序桌面图标，双击打开运行应用程序
        pyautogui.moveTo(952, 540, duration=1)
        pyautogui.doubleClick()
        time.sleep(10)
        # 移至登录输入框，输入账号和密码
        pyautogui.moveTo(590, 432, duration=1)
        pyautogui.doubleClick()
        pyautogui.typewrite('110028553', interval=0.25)
        pyautogui.moveTo(611, 506, duration=1)
        pyautogui.doubleClick()
        pyautogui.typewrite('110028553', interval=0.25)
        pyautogui.moveTo(743, 562, duration=1)
        login_button = auto.locateOnScreen('../source_photoes/login/login_button.png')  # 传入登录按钮的图片
        print(login_button)
        time.sleep(3)
        auto.screenshot('../photoes/login/login_button.png', region=(531, 647, 368, 60))  # 校对图片位置
        auto.click(login_button)  # 点击登录按钮

    # @unittest.skip("skipping")
    def testOPlayer01(self):
        # self.login()
        myRoom = auto.locateOnScreen('../source_photoes/OPlayer/myroom.png')
        auto.click(myRoom)
        time.sleep(3)
        oplayer_Button = auto.locateOnScreen('../source_photoes/OPlayer/OPlayer_button.png')
        auto.click(oplayer_Button)
        time.sleep(5)
        OPlayer_succeed = auto.locateOnScreen('../source_photoes/OPlayer/OPlayer_succeed.png')
        print(OPlayer_succeed)
        auto.screenshot('../photoes/OPlayer/OPlayer_succeed.png', region=(473, 72, 299, 47))  # 校对图片位置

        # 图片断言
        image1 = cv2.imread("../source_photoes/OPlayer/OPlayer_succeed.png")
        image2 = cv2.imread("../photoes/OPlayer/OPlayer_succeed.png")
        difference = cv2.subtract(image1, image2)
        result = not np.any(difference)
        self.assertTrue(result, "图片飞走了~")

    @unittest.skip("skipping")
    def testOPlayer02(self):
        # #self.login()
        myroom = auto.locateOnScreen('../source_photoes/OPlayer/myroom.png')
        auto.click(myroom)
        time.sleep(3)
        pyautogui.click(762, 360, button='left')  # 单击左键
        time.sleep(3)
        pyautogui.typewrite('test.png', interval=0.25)
        pyautogui.press('enter')
        pyautogui.press('enter')
        time.sleep(3)
        pyautogui.click(912, 507, button='left')  # 单击左键
        time.sleep(3)
        pyautogui.moveTo(835, 590, duration=1)
        pyautogui.doubleClick()
        time.sleep(1)
        oplayer_button = auto.locateOnScreen('../source_photoes/OPlayer/OPlayer_button.png')
        auto.click(oplayer_button)
        time.sleep(5)
        OPlayer_succeed = auto.locateOnScreen('../source_photoes/OPlayer/OPlayer_succeed.png')
        # print(OPlayer_succeed)
        pyautogui.click(958, 550, button='left')  # 单击左键
        auto.screenshot('../photoes/OPlayer/OPlayer_succeed.png', region=(474, 71, 219, 48))  # 校对图片位置


        # 图片断言
        image1 = cv2.imread("../source_photoes/OPlayer/OPlayer_succeed.png")
        image2 = cv2.imread("../photoes/OPlayer/OPlayer_succeed.png")
        difference = cv2.subtract(image1, image2)
        result = not np.any(difference)
        self.assertTrue(result, "图片飞走了~")


if __name__ == '__main__':
    unittest.main()    # unittest 的执行