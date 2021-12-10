#coding=utf-8
import unittest
import HTMLTestRunner
import time,os


def creatsuite():
	testunit = unittest.TestSuite()
	# 定义测试文件查找的目录
	test_dir = '../test_case'
	# 定义 discover 方法的参数
	discover = unittest.defaultTestLoader.discover(test_dir,
	pattern='test*.py',top_level_dir=None)
	# discover
	# 循环添加到测试套件中

	for test_suite in discover:
		for test_case in test_suite:
			testunit.addTests(test_case)
			print(test_case)
	return testunit

allcasenames=creatsuite()
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
print(now)
filename = '../report/html/' + now + "test_all.html"
fp = open(filename, 'wb')

if __name__ == '__main__':
	runner = unittest.TextTestRunner()
	runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'哇噻秀PC端自动化测试报告', description=u'测试用例结果')
	runner.run(allcasenames)
