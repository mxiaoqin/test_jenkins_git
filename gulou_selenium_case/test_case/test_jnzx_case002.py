"""
@author: xiaoqin
@contact: lixiaoqin@ambuf.com
@software: garner
@file: __init__.py.py
@time: 2018/7/23 10:11
@desc:
"""

import unittest
import time

from pageobjects.gulou_loginpage import LoginPage
from pageobjects.gulou_XinJianKaoHe import XinJianKaoHe
from pageobjects.gulou_GetCankaorenyuanInfo import GetCankaorenyuanInfo
from pageobjects.gu_kaozhaninfo import KaozhanInfo
from framework.browser_engine import BrowserEngine


class Test_Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.quit()

    def test_login(self):
        # 登录
        linage = LoginPage(self.driver)
        linage.input_username('01')
        linage.input_password('666666')
        linage.send_submit_btn()
        linage.send_loginsubmit()
        if linage.get_username() == "教育处(教育处)":
            print("成功登录到首页")
            self.jnzx()
        else:
            nametext = linage.get_username()
            print("未获取到正确的页面断言文字: " + nametext)
            linage.get_windows_img()
            self.driver.quit()

    def jnzx(self):
        # 点击技能中心
        XinJianKaoHe.jineng(self)
        if XinJianKaoHe.get_jnzx(self) == "技能中心":
            print("成功点击技能中心菜单！")
            # 点击技能考核
            XinJianKaoHe.click_tab(self)
            # 点击新建考核按钮
            XinJianKaoHe.click_xjkh(self)
            # 点击规范考核、确定按钮
            XinJianKaoHe.click_guifan(self)
            XinJianKaoHe.click_queding(self)
            self.inputinfo()
            self.renyuanInfo()
            # self.kaozhan()

        else:
            nametext = XinJianKaoHe.get_jnzx(self)
            print("未获取到正确的页面断言文字: " + nametext)
            XinJianKaoHe.get_windows_img(self)
            self.driver.quit()

    def inputinfo(self):
        # 输入考站基本信息
        XinJianKaoHe.input_createinfo(self, '规范考核-考生抽题')
        XinJianKaoHe.send_keys_xiuxi(self, '5')
        XinJianKaoHe.send_keys_xiuxitime(self, '1')
        XinJianKaoHe.send_keys_huanzhantime(self, '1')
        XinJianKaoHe.click_gettime(self)

    def renyuanInfo(self):
        # 获取参考人员
        GetCankaorenyuanInfo.click_add_button(self)
        if GetCankaorenyuanInfo.get_textrenyuan(self) == "选择人员":
            print("成功跳转至选择人员弹窗")
            # 点击参考人员文件夹
            GetCankaorenyuanInfo.click_files(self)
            # 点击源列表按钮
            GetCankaorenyuanInfo.click_yuanliebiao(self)

            if GetCankaorenyuanInfo.get_element_display(self) is not None:
                print("参考人员存在！")
                # 点击向右移动按钮
                GetCankaorenyuanInfo.click_right_button(self)
                # 点击提交按钮
                GetCankaorenyuanInfo.click_commit_button(self)
                self.kaozhan()

            else:
                nametext = GetCankaorenyuanInfo.get_element_display(self)
                print("未显示参考人员列表: " + nametext)
                XinJianKaoHe.get_windows_img(self)
                self.driver.quit()

        else:
            nametext = GetCankaorenyuanInfo.get_textrenyuan(self)
            print("未获取到正确的页面断言文字: " + nametext)
            XinJianKaoHe.get_windows_img(self)
            self.driver.quit()

    def kaozhan(self):
        # 点击考站
        KaozhanInfo.click_kazhan(self)
        KaozhanInfo.send_keys_name(self, '考站1')
        KaozhanInfo.click_chouti_type(self, 1)
        KaozhanInfo.click_room(self)
        KaozhanInfo.click_nullroom(self, '1')
        KaozhanInfo.click_queding(self)
        if KaozhanInfo.get_elements_name(self) is not None:
            print("考站基本信息已填写")
            self.kaozhan_two()

        else:
            nametext = GetCankaorenyuanInfo.get_textrenyuan(self)
            print("未获取到正确的页面断言文字: " + nametext)
            XinJianKaoHe.get_windows_img(self)
            self.driver.quit()

    def kaozhan_two(self):
        KaozhanInfo.click_onenext(self)
        KaozhanInfo.send_keys_kaohename(self, '考核1')
        KaozhanInfo.click_bingli(self)
        KaozhanInfo.click_choosebingli(self)
        KaozhanInfo.click_bingliqueding(self)
        if KaozhanInfo.get_elements_bingli(self) is not None:
            print("考核内容已填写")
            self.kaozhan_three()
        else:
            nametext = GetCankaorenyuanInfo.get_textrenyuan(self)
            print("未获取到正确的页面断言文字: " + nametext)
            XinJianKaoHe.get_windows_img(self)
            self.driver.quit()

    def kaozhan_three(self):
        KaozhanInfo.click_nextbutton1(self)
        KaozhanInfo.click_teacherbutton(self)
        KaozhanInfo.click_teacherfiles(self)
        KaozhanInfo.click_choseteacher(self)
        KaozhanInfo.click_rightbutton(self)
        KaozhanInfo.click_submitbutton(self)
        KaozhanInfo.click_pingfen(self)
        KaozhanInfo.click_pf_quren(self)
        if KaozhanInfo.get_elements_teacher(self) is not None:
            self.kaozhan_quanzhong()
        else:
            nametext = GetCankaorenyuanInfo.get_textrenyuan(self)
            print("未获取到正确的页面断言文字: " + nametext)
            XinJianKaoHe.get_windows_img(self)
            self.driver.quit()

    def kaozhan_quanzhong(self):
        KaozhanInfo.click_nextbutton(self)
        KaozhanInfo.click_finishbutton(self)
        KaozhanInfo.click_quanzhong(self)
        KaozhanInfo.send_keys_quanzhong(self, '100')
        KaozhanInfo.click_save(self)

        # 点击保存考核按钮
        KaozhanInfo.click_savekaohe(self)


if __name__ == '__main__':
    unittest.main()
    # creat_report()
