# coding:utf-8
import time
import pyautogui
import  unittest
#
#
#问题：鼠标点击无响应问题（需要管理员身份进行运行才能触发点击效果）
#
# abc = pyautogui.position()
# print(abc)

#
#public下可以运行所有test目录case
#
#
class TestPC(unittest.TestCase):
    @unittest.skip("skipping")
    def testlogin(self):
        #移至应用程序桌面图标，双击打开运行应用程序
        pyautogui.moveTo(1034,535, duration=1)
        pyautogui.doubleClick()
        time.sleep(5)
        #移至登录输入框，输入账号和密码
        pyautogui.moveTo(1061,447, duration=1)
        pyautogui.doubleClick()
        pyautogui.typewrite('110016117', interval=0.25)
        pyautogui.moveTo(1065 , 513, duration=1)
        pyautogui.doubleClick()
        pyautogui.typewrite('110016117', interval=0.25)
        pyautogui.moveTo(1155 , 559, duration=1)
        #勾选记住密码
        pyautogui.dragTo(1155, 559, button='left')
        # 点击登录按钮
        pyautogui.moveTo(1098 , 601, duration=1)
        pyautogui.doubleClick()
        time.sleep(5)
        pyautogui.screenshot() # 截图
        pyautogui.screenshot(r'../Photoes/login_sussce.png') #保存图片

    @unittest.skip("skipping")
    def testjinroom(self):
        for num in range(0, 1):
            # time.sleep(5)
            # pyautogui.dragTo(1308, 180, button='left')
            time.sleep(5)
            #进入房间操作
            pyautogui.moveTo(562 , 502, duration=1)
            pyautogui.doubleClick()
            time.sleep(10)
            #选择礼物
            pyautogui.moveTo(754, 845, duration=1)
            pyautogui.doubleClick()
            #发送礼物
            pyautogui.moveTo(1051, 619, duration=1)
            pyautogui.doubleClick()
            #关闭礼物弹窗
            pyautogui.moveTo(1077, 409, duration=1)
            pyautogui.doubleClick()
            time.sleep(10)
            #关闭房间窗口
            pyautogui.moveTo(1578, 88, duration=1)
            pyautogui.doubleClick()

if __name__ == '__main__':
    unittest.main() # unittest 的执行





