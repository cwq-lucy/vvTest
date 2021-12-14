# coding:utf-8
import time
import pyautogui
import unittest
import cv2
import numpy as np
import pyautogui as auto


# @unittest.skip("skipping")
class testOPlayer(unittest.TestCase):

    def login(self):
        # 移至应用程序桌面图标，双击打开运行应用程序
        pyautogui.moveTo(952, 540, duration=1)
        pyautogui.doubleClick()
        time.sleep(10)
        # 移至登录输入框，输入账号和密码
        pyautogui.moveTo(590, 432, duration=1)
        pyautogui.doubleClick()
        pyautogui.typewrite('110028893', interval=0.25)
        pyautogui.moveTo(611, 506, duration=1)
        pyautogui.doubleClick()
        pyautogui.typewrite('110016117', interval=0.25)
        login_button = auto.locateOnScreen('../source_photoes/login/login_button.png')  # 传入登录按钮的图片
        time.sleep(3)
        auto.screenshot('../photoes/login/login_button.png', region=(531, 647, 368, 60))  # 校对图片位置
        auto.click(login_button)  # 点击登录按钮

    # 编辑公告
    # @unittest.skip("skipping")
    def testRoom01(self):
        # self.login()
        edit_affiche = auto.locateOnScreen('../source_photoes/room/edit_affiche.png')
        auto.click(edit_affiche)
        time.sleep(1)
        pyautogui.typewrite('huanyinglaidaolvsezhibojian1')
        save = auto.locateOnScreen('../source_photoes/room/save.png')
        auto.click(save)
        time.sleep(3)
        audit = auto.locateOnScreen('../source_photoes/room/audit.png')
        print(audit)
        time.sleep(1)
        auto.screenshot('../photoes/room/audit.png', region=(831, 436, 258, 145))
        time.sleep(3)
        roger = auto.locateOnScreen('../source_photoes/room/roger.png')
        auto.click(roger)

        # 图片断言
        image1 = cv2.imread("../source_photoes/room/audit.png")
        image2 = cv2.imread("../photoes/room/audit.png")
        difference = cv2.subtract(image1, image2)
        result = not np.any(difference)
        self.assertTrue(result, "图片飞走了~")

    # 使用表情包
    # @unittest.skip("skipping")
    def testRoom02(self):
        # self.login()
        Magic_Emotion = auto.locateOnScreen('../source_photoes/room/Magic_Emotion.png')
        auto.click(Magic_Emotion)
        time.sleep(1)
        pyautogui.click(1191, 881)
        time.sleep(1)
        pyautogui.click(1306, 779)
        time.sleep(3)
        pyautogui.scroll(-2000)
        time.sleep(3)

        pyautogui.click(1199, 816)
        time.sleep(5)
        pyautogui.click(1265, 817)
        time.sleep(5)
        pyautogui.click(1332, 813)
        time.sleep(5)
        pyautogui.click(1404, 814)
        time.sleep(5)

        pyautogui.click(1105, 489)
        time.sleep(3)

    # 房间上锁
    # @unittest.skip("skipping")
    def testRoom03(self):
        # self.login()
        menus = auto.locateOnScreen('../source_photoes/room/menus.png')
        auto.click(menus)
        time.sleep(3)
        pyautogui.click(839, 779, button='left')  # 房间上锁 # 842 782
        pyautogui.doubleClick(961, 538, button='left')
        time.sleep(3)
        pyautogui.typewrite('1111', interval=0.25)
        ensure = auto.locateOnScreen('../source_photoes/room/ensure.png')
        auto.click(ensure)

        menus = auto.locateOnScreen('../source_photoes/room/menus.png')
        auto.click(menus)
        pyautogui.click(839, 779, button='left')  # 房间解锁
        sure = auto.locateOnScreen('../source_photoes/room/sure.png')
        auto.click(sure)

    # 心动值开关
    # @unittest.skip("skipping")
    def testRoom04(self):
        menus = auto.locateOnScreen('../source_photoes/room/menus.png')
        auto.click(menus)
        time.sleep(3)
        pyautogui.click(840, 839)
        time.sleep(3)
        pyautogui.click(1086, 502)
        time.sleep(3)
        pyautogui.click(1073, 544)
        pyautogui.scroll(10)
        time.sleep(3)
        pyautogui.click(981, 592)
        time.sleep(3)

        # 关闭心动值开关
        menus = auto.locateOnScreen('../source_photoes/room/menus.png')
        auto.click(menus)
        time.sleep(3)
        pyautogui.click(840, 839)
        time.sleep(3)
        pyautogui.click(1086, 502)
        time.sleep(3)
        pyautogui.click(981, 592)
        time.sleep(3)

    # 编辑欢迎词
    # @unittest.skip("skipping")
    def testRoom05(self):
        menus = auto.locateOnScreen('../source_photoes/room/menus.png')
        auto.click(menus)
        time.sleep(3)
        pyautogui.click(907, 839)
        time.sleep(1)
        pyautogui.doubleClick(920, 472)
        pyautogui.typewrite('huanyinglaidaolvsezhibojian1')
        time.sleep(3)
        pyautogui.click(1012, 612)
        time.sleep(1)
        pyautogui.click(961, 545)

    # 编辑房间标题
    # @unittest.skip("skipping")
    def testRoom06(self):
        menus = auto.locateOnScreen('../source_photoes/room/menus.png')
        auto.click(menus)
        time.sleep(3)
        pyautogui.click(979, 782)
        time.sleep(1)
        pyautogui.doubleClick(920, 472)
        pyautogui.typewrite('huanyinglaidaolvsezhibojian1')
        time.sleep(3)
        pyautogui.click(1012, 612)
        time.sleep(1)
        pyautogui.click(961, 545)

    # 设置房间管理员
    # @unittest.skip("skipping")
    def testRoom07(self):
        menus = auto.locateOnScreen('../source_photoes/room/menus.png')
        auto.click(menus)
        time.sleep(3)
        pyautogui.click(1046, 777)
        time.sleep(3)
        pyautogui.click(960, 635)
        time.sleep(3)
        pyautogui.click(915, 394)
        pyautogui.typewrite('110013889')
        time.sleep(3)
        pyautogui.click(1064, 394)
        time.sleep(1)
        pyautogui.click(1078, 347)

    # 移除管理员
    # @unittest.skip("skipping")
    def testRoom08(self):
        menus = auto.locateOnScreen('../source_photoes/room/menus.png')
        auto.click(menus)
        time.sleep(3)
        pyautogui.click(1046, 777)
        time.sleep(3)
        pyautogui.click(1070, 460)
        time.sleep(3)
        pyautogui.click(1089, 392)

    # 用户进入直播间,进房记录
    # @unittest.skip("skipping")
    def testRoom09(self):
        pyautogui.click(1400, 94)
        self.login()
        time.sleep(3)
        pyautogui.click(1636, 40)
        time.sleep(3)
        pyautogui.doubleClick(1417, 372)
        time.sleep(3)

    # 用户上麦,@人,发送消息
    # @unittest.skip("skipping")
    def testRoom10(self):
        pyautogui.click(1145, 864)
        time.sleep(3)
        pyautogui.click(1105, 384)
        pyautogui.doubleClick(1145, 864)
        time.sleep(1)
        pyautogui.click(1195, 821)
        time.sleep(3)
        pyautogui.click(1231, 708)
        time.sleep(3)
        pyautogui.typewrite('110013889')
        time.sleep(3)
        pyautogui.click(1404, 904)
        time.sleep(3)

    # 送礼物（小星星，包裹礼物，盖章，送礼记录）
    # @unittest.skip("skipping")
    def testRoom11(self):
        pyautogui.click(1138, 903)
        time.sleep(3)
        pyautogui.click(1210, 658)
        time.sleep(3)
        pyautogui.click(1476, 884)
        time.sleep(3)

        pyautogui.click(1194, 615)
        time.sleep(3)
        pyautogui.click(1210, 658)
        time.sleep(3)
        pyautogui.click(1476, 884)
        time.sleep(3)

        pyautogui.click(1447, 616)
        time.sleep(3)
        pyautogui.click(1210, 658)
        time.sleep(3)
        pyautogui.click(1487, 888)
        time.sleep(3)

        pyautogui.click(1105, 489)
        time.sleep(3)

    # 选择贵族气泡发送消息
    # @unittest.skip("skipping")
    def testRoom12(self):
        pyautogui.click(1229, 818)
        time.sleep(3)
        pyautogui.click(1019, 422)
        time.sleep(3)
        pyautogui.click(1047, 662)
        time.sleep(3)
        pyautogui.click(957, 545)
        time.sleep(3)
        pyautogui.click(1217, 850)
        time.sleep(3)
        pyautogui.typewrite('110013889')
        time.sleep(3)
        pyautogui.click(1404, 906)

        pyautogui.click(1229, 818)
        time.sleep(3)
        pyautogui.click(776, 426)
        time.sleep(3)
        pyautogui.click(1047, 662)
        time.sleep(3)
        pyautogui.click(957, 545)
        time.sleep(3)
        pyautogui.click(1217, 850)
        time.sleep(3)
        pyautogui.typewrite('110013889')
        time.sleep(3)
        pyautogui.click(1404, 906)

    # 送礼记录列表(价值排序&时间排序) 切换 进房记录列表
    def testRoom13(self):
        pyautogui.click(1216, 284)
        time.sleep(1)
        pyautogui.click(1310, 284)
        time.sleep(1)
        pyautogui.click(1216, 284)
        time.sleep(1)
        pyautogui.click(1436, 286)
        time.sleep(1)
        pyautogui.click(1414, 329)
        time.sleep(1)
        pyautogui.click(1436, 286)
        time.sleep(1)
        pyautogui.click(1410, 356)

    # 查看贵族列表、守护列表
    def testRoom14(self):
        pyautogui.click(821, 190)
        time.sleep(3)
        pyautogui.click(853, 229)
        time.sleep(3)
        pyautogui.moveTo(916, 276)
        time.sleep(3)
        pyautogui.scroll(-2000)
        time.sleep(3)
        pyautogui.click(927, 229)
        time.sleep(3)
        pyautogui.moveTo(916, 276)
        time.sleep(3)
        pyautogui.scroll(-2000)

    # 查看豪客榜：日榜、周榜、月榜
    def testRoom15(self):
        time.sleep(3)
        pyautogui.click(499, 148)
        time.sleep(3)
        pyautogui.click(548, 182)
        time.sleep(3)
        pyautogui.click(615, 337)
        time.sleep(3)
        pyautogui.click(612, 185)
        time.sleep(3)
        pyautogui.click(687, 181)
        time.sleep(3)
        pyautogui.click(614, 876)
        time.sleep(3)

    # 查看心动榜：日榜、周榜、月榜
    def testRoom16(self):
        time.sleep(3)
        pyautogui.click(594, 147)
        time.sleep(3)
        pyautogui.click(551,179)
        time.sleep(3)
        pyautogui.click(617, 339)
        time.sleep(3)
        pyautogui.click(622, 182)
        time.sleep(3)
        pyautogui.click(685, 181)
        time.sleep(3)
        pyautogui.click(611, 873)




if __name__ == '__main__':
    unittest.main()  # unittest 的执行
