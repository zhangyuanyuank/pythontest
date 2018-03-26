import unittest
import time
import HTMLTestRunner
import os
import case


if __name__ == "__main__":
    # 报告存放路径
    report_path = os.path.join(os.getcwd(), 'report')

    # 1、获取当前时间，这样便于下面的使用。
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

    # 2、html报告文件路径
    report_nowpath = os.path.join(report_path, "result_" + now + ".html")

    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(case.MyTestSuite("testbaidu"))
    suite.addTest(case.MyTestSuite("testitao"))

    # 3、打开一个文件，将result写入此file中
    fp = open(report_nowpath, "wb")
    reporthtml = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'接口自动化测试报告,测试结果如下：',
                                           description=u'用例执行情况：')

    # 执行测试
    #runner = unittest.TextTestRunner()
    reporthtml.run(suite)
    fp.close()





