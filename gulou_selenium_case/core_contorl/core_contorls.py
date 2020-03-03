"""
@author: xiaoqin
@contact: lixiaoqin@ambuf.com
@software: garner
@file: core_contorls.py
@time: 2018/7/23 10:13
@desc:
"""
import time


# 将报错的页面截图并保存
def screenshot(driver):
    scrpath = 'E:/python_test/gulou_selenium_case/screenshots'  # 指定的保存目录
    rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    capturename = '\\' + rq + '.png'  # 自定义命名截图
    wholepath = scrpath + capturename
    from pathlib import Path
    if Path(scrpath).is_dir():  # 判断文件夹路径是否已经存在
        pass
    else:
        Path(scrpath).mkdir()  # 如果不存在，创建文件夹
    while Path(wholepath).exists():  # 判断文件是否已经存在，也可使用is_file()判断
        capturename = '\\' + rq + '.png'
        wholepath = scrpath + capturename
    driver.get_screenshot_as_file(wholepath)  # 不能接受Path类的值，只能是字符串，否则无法截图


