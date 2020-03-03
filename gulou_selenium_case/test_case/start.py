"""
@author: xiaoqin
@contact: lixiaoqin@ambuf.com
@software: garner
@file: start.py
@time: 2018/7/23 10:16
@desc:
"""

import HTMLTestRunner
import unittest


# 用例路径
case_path = "E:\\python_test\\gulou_selenium_case\\test_case"
# 报告存放路径
report_path = 'E:/python_test/gulou_selenium_case/report'


def all_case():
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py")
    print(discover)
    return discover


# 测试
if __name__ == "__main__":
    # runner = unittest.TextTestRunner()
    # runner.run(discover)
    report_abspath = 'E:/python_test/gulou_selenium_case/report/result.html'
    fp = open(report_abspath, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告,测试结果如下：',
                                           description=u'用例执行情况：')

    # 调用add_case函数返回值
    runner.run(all_case())
    fp.close()
