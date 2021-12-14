# coding:utf-8
import time
import pyautogui
import unittest
import cv2
import numpy as np
import pyautogui as auto


#
# 问题：鼠标点击无响应问题（需要管理员身份进行运行才能触发点击效果）
#

# @unittest.skip("skipping")
class testLogin(unittest.TestCase):
    # 手机号登录
    @unittest.skip("skipping")
    def testLogin01(self):
        # 移至应用程序桌面图标，双击打开运行应用程序
        pyautogui.moveTo(952, 540, duration=1)
        pyautogui.doubleClick()
        time.sleep(10)

        time.sleep(3)
        input_iphone = auto.locateOnScreen('../source_photoes/login/input_iphone.png')  # 校对登录按钮的图片位置
        time.sleep(3)
        pyautogui.typewrite('15112378424', interval=0.25)  # 用户账号不存在
        pyautogui.press('tab')
        pyautogui.typewrite('1111', interval=0.25)  # 用户账号不存在

        login_button = auto.locateOnScreen('../source_photoes/login/login_button1.png')  # 传入登录按钮的图片
        auto.click(login_button)
        time.sleep(5)
        tia = auto.locateOnScreen('../source_photoes/login/login_succeed.png')  # 传入登录按钮的图片
        # print(tia)
        auto.screenshot('../photoes/login/login_succeed.png', region=(1614, 23, 283, 34))

        # 图片断言
        image1 = cv2.imread("../source_photoes/login/login_succeed.png")
        image2 = cv2.imread("../photoes/login/login_succeed.png")
        difference = cv2.subtract(image1, image2)
        result = not np.any(difference)
        self.assertTrue(result, "图片飞走了~")

    # @unittest.skip("skipping")
    def testLogin02(self):
        # 移至应用程序桌面图标，双击打开运行应用程序
        pyautogui.moveTo(952, 540, duration=1)
        pyautogui.doubleClick()
        time.sleep(10)
        # 移至登录输入框，输入账号和密码
        pyautogui.moveTo(590, 432, duration=1)
        pyautogui.doubleClick()
        pyautogui.typewrite('110000000', interval=0.25)  # 用户账号不存在
        pyautogui.moveTo(611, 506, duration=1)
        pyautogui.doubleClick()
        pyautogui.typewrite('110016117', interval=0.25)
        login_button = auto.locateOnScreen('../source_photoes/login/login_button.png')  # 传入登录按钮的图片
        time.sleep(3)
        auto.screenshot('../photoes/login/login_button.png', region=(531, 647, 368, 60))  # 校对登录按钮的图片位置
        auto.click(login_button)  # 点击登录按钮
        user_error = auto.locateOnScreen('../source_photoes/login/user_error.png')  # 传入登录按钮的图片
        auto.screenshot('../photoes/login/user_error.png', region=(650, 750, 128, 48))  # 校对登录按钮的图片位置
        # print(user_error)
        time.sleep(3)
        # 图片断言
        image1 = cv2.imread("../source_photoes/login/user_error.png")
        image2 = cv2.imread("../photoes/login/user_error.png")
        difference = cv2.subtract(image1, image2)
        result = not np.any(difference)
        self.assertTrue(result, "图片飞走了~")

    # @unittest.skip("skipping")
    def testLogin03(self):
        # 移至应用程序桌面图标，双击打开运行应用程序
        pyautogui.moveTo(952, 540, duration=1)
        pyautogui.doubleClick()
        time.sleep(10)
        # 移至登录输入框，输入账号和密码
        pyautogui.moveTo(590, 432, duration=1)
        pyautogui.doubleClick()
        pyautogui.typewrite('110013889', interval=0.25)
        pyautogui.moveTo(611, 506, duration=1)  # 用户账号不存在
        pyautogui.doubleClick()
        pyautogui.typewrite('1100', interval=0.25)  # 密码少于6位小数
        login_button = auto.locateOnScreen('../source_photoes/login/login_button.png')  # 传入登录按钮的图片
        time.sleep(3)
        auto.screenshot('../photoes/login/login_button.png', region=(531, 647, 368, 60))  # 校对登录按钮的图片位置
        auto.click(login_button)  # 点击登录按钮
        password = auto.locateOnScreen('../source_photoes/login/password.png')  # 传入登录按钮的图片
        auto.screenshot('../photoes/login/password.png', region=(583, 754, 261, 43))  # 校对登录按钮的图片位置
        # print(password)
        # 图片断言
        image1 = cv2.imread("../source_photoes/login/password.png")
        image2 = cv2.imread("../photoes/login/password.png")
        difference = cv2.subtract(image1, image2)
        result = not np.any(difference)
        self.assertTrue(result, "图片飞走了~")

    # 密码错误
    @unittest.skip("skipping")
    def testLogin04(self):
        # 移至应用程序桌面图标，双击打开运行应用程序
        pyautogui.moveTo(952, 540, duration=1)
        pyautogui.doubleClick()
        time.sleep(10)
        # 移至登录输入框，输入账号和密码
        pyautogui.moveTo(590, 432, duration=1)
        pyautogui.doubleClick()
        pyautogui.typewrite('11001388', interval=0.25)
        pyautogui.moveTo(611, 506, duration=1)
        pyautogui.doubleClick()
        pyautogui.typewrite('110011', interval=0.25)  # 输入错误密码
        login_button = auto.locateOnScreen('../source_photoes/login/login_button.png')  # 传入登录按钮的图片
        time.sleep(3)
        auto.screenshot('../photoes/login/password.png', region=(531, 647, 368, 60))  # 校对登录按钮的图片位置
        auto.click(login_button)  # 点击登录按钮
        # 图片断言
        image1 = cv2.imread("../source_photoes/login/password.png")
        image2 = cv2.imread("../photoes/login/password.png")
        difference = cv2.subtract(image1, image2)
        result = not np.any(difference)
        self.assertTrue(result, "图片飞走了~")

    # @unittest.skip("skipping")
    def testLogin05(self):
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
        pyautogui.dragTo(743, 562, button='left')  # 勾选记住密码
        login_button = auto.locateOnScreen('../source_photoes/login/login_button.png')  # 传入登录按钮的图片
        time.sleep(3)
        auto.screenshot('../photoes/login/login_button.png', region=(531, 647, 368, 60))  # 校对图片位置
        auto.click(login_button)  # 点击登录按钮
        time.sleep(8)
        login = auto.locateOnScreen('../source_photoes/login/login_succeed.png')  # 传入按钮的图片
        print(login)
        auto.screenshot('../photoes/login/login_succeed.png', region=(1614, 23, 283, 34))
        auto.screenshot('../photoes/login/login_gui.png', region=(460, 185, 1000, 670))  # 截取登录界面图片
        # 图片断言
        image1 = cv2.imread("../source_photoes/login/login_succeed.png")
        image2 = cv2.imread("../photoes/login/login_succeed.png")
        difference = cv2.subtract(image1, image2)
        result = not np.any(difference)
        self.assertTrue(result, "图片飞走了~")


if __name__ == '__main__':
    unittest.main()  # unittest 的执行
