#  /home/pyvip/py_case
#  _*_ coding:utf-8 _*_
# # author : yellowsea  time:2018/3/14 0014
# import unittest
# import HTMLTestRunner
# test_dir=r'E:\activity\testcase'#测试用例文件路径
# test_case = unittest.TestSuite()
# discover=unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='test*.py')#匹配路径
# test_case.addTests(discover)
# print(test_case)
# # runner=unittest.TextTestRunner()#text形式报告
# # runner.run(discover)#跑用例
#
# reportFile=r'e:\test\report\result.html'#生成报告路径
# with open(reportFile,'wb') as fp:#写入的方式打开文件
#     runner1=HTMLTestRunner.HTMLTestRunner(stream=fp,title='自动化测试报告',description='第二课堂后台自动化测试报告')
#     runner1.run(discover)
#     fp.close()
# print('end-----')


import HTMLTestRunner
import unittest
import os,time


listaa = "E:\\activity\\testcase"
def createsuite1():
    testunit=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(listaa,pattern='test*.py',top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit

now = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime())
filename="E:\\activity\\report\\"+now+"_result.html"
fp=open(filename,'wb')

runner=HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'新增活动试报告',
    description=u'用例执行情况：')

runner.run(createsuite1())

#关闭文件流，不关的话生成的报告是空的
fp.close()
