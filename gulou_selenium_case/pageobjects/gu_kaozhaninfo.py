import time
from framework.base_page import BasePage


class KaozhanInfo(BasePage):

    def click_kazhan(self):
        # 点击考站
        self.driver.find_element_by_xpath("//*[@id='stationRoomBox']/div/div/div[2]/img").click()
        time.sleep(1)

        """----------------------------------基本信息------------------------------"""

    def send_keys_name(self,text):
        # 输入考站名称
        self.driver.find_element_by_xpath(
            "//*[@id='stationMain']/span[3]/div[2]/div/div/div[2]/div/div[2]/form/div/div[1]/div/div/div/input").send_keys(
            text)
        time.sleep(1)

    def get_elements_name(self):
        kaozhanname = self.driver.find_element_by_xpath(
            "//*[@id='stationMain']/span[3]/div[2]/div/div/div[2]/div/div[2]/form/div/div[1]/div/div/div/input").text
        return kaozhanname

     # 选择抽题类型
    def click_chouti_type(self,type):
        self.driver.find_element_by_xpath("//*[@id='stationMain']/span[3]/div[2]/div/div/div[2]/div/div[2]/form/div/div[3]/div/div/div/div[1]/i").click()
        time.sleep(1)

        if type == 1:
            self.driver.find_element_by_xpath("/html/body/div[5]/div/div[1]/ul/li[1]/span").click()
            print("点击了自动抽题")
            time.sleep(1)
        elif type == 2:
            self.driver.find_element_by_xpath("/html/body/div[5]/div/div[1]/ul/li[2]/span").click()
            print("点击了考生抽题")
            time.sleep(1)
        elif type == 3:
            self.driver.find_element_by_xpath("/html/body/div[5]/div/div[1]/ul/li[3]/span").click()
            print("点击了教师抽题")
            time.sleep(1)
        elif type == 4:
            self.driver.find_element_by_xpath("/html/body/div[5]/div/div[1]/ul/li[4]/span").click()
            print("点击了不用抽题")
            time.sleep(1)
        else:
            print("没有可选的抽题类型!")

    def click_room(self):
        # 点击 选择房间 按钮
        room = self.driver.find_element_by_xpath(
            "//*[@id='stationMain']/span[3]/div[2]/div/div/div[2]/div/div[2]/form/div/div[6]")
        choseroom = room.find_element_by_xpath(
            "//*[@id='stationMain']/span[3]/div[2]/div/div/div[2]/div/div[2]/form/div/div[6]/div/div")
        choseroom.find_element_by_xpath(
            "//*[@id='stationMain']/span[3]/div[2]/div/div/div[2]/div/div[2]/form/div/div[6]/div/div/button").click()
        time.sleep(1)

    def click_nullroom(self,roomid):
        # 选择第一个房间
        self.driver.find_element_by_xpath(
            "//*[@id='stationMain']/span[3]/div[2]/div/div/div[2]/div/div[2]/span/div[2]/div/div/div[2]/div/div/div[2]/div/div[3]/table/tbody/tr[" +roomid+"]").click()
        time.sleep(1)

    def click_queding(self):
        # 点击确定按钮
        self.driver.find_element_by_xpath(
            "//*[@id='stationMain']/span[3]/div[2]/div/div/div[2]/div/div[2]/span/div[2]/div/div/div[2]/div/div/div[3]/div[1]/button").click()
        time.sleep(1)

    # 点击下一步按钮
    def click_onenext(self):
        self.driver.find_element_by_xpath("//*[@id='stationMain']/span[3]/div[2]/div/div/div[2]/div/div[2]/form/div/div[7]/button").click()
        time.sleep(1)

    """ -----------------------------------考核内容------------------------------------"""
    def send_keys_kaohename(self,text):
        # 输入考核名称
        inputname = self.driver.find_element_by_xpath(
            "//*[@id='stationMain']/span[3]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr/td[1]/div/div")
        inputname.find_element_by_xpath(
            "//*[@id='stationMain']/span[3]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr/td[1]/div/div/input").send_keys(
            text)
        time.sleep(1)

    def click_bingli(self):
        # 点击病例
        self.driver.find_element_by_xpath(
            "//*[@id='stationMain']/span[3]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr/td[4]/div/button[1]").click()
        time.sleep(1)

    def click_choosebingli(self):
        # 选择病例
        self.driver.find_element_by_xpath("//*[@id='tableData']/div/div[3]/table/tbody/tr[6]/td[1]/div/label").click()
        time.sleep(1)

    def get_elements_bingli(self):
        tr = self.driver.find_element_by_xpath(
            "//*[@id='stationMain']/span[3]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr")
        bingli = tr.find_element_by_xpath(
            "//*[@id='stationMain']/span[3]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr/td[3]").text
        return bingli
    def click_bingliqueding(self):
        # 点击确定按钮
        self.driver.find_element_by_xpath("//*[@id='content']/div[3]/div[1]/button").click()
        time.sleep(1)

    def click_nextbutton1(self):
        # 点击下一步
        nest_button = self.driver.find_element_by_xpath(
            "//*[@id='stationMain']/span[3]/div[2]/div/div/div[2]/div/div[2]/div[3]")
        nest_button.find_element_by_xpath(
            "//*[@id='stationMain']/span[3]/div[2]/div/div/div[2]/div/div[2]/div[3]/div[2]/button").click()
        time.sleep(1)

        """---------------------------------- 监考老师-----------------------------------------"""


     # 点击选择老师按钮
    def click_teacherbutton(self):
        self.driver.find_element_by_xpath(
            "//*[@id='stationMain']/span[3]/div[2]/div/div/div[2]/div/div[2]/form/div/div/div/button").click()
        time.sleep(1)

    def click_teacherfiles(self):
        # 点击选择老师文件夹 选择测试部门文件夹
        self.driver.find_element_by_xpath(
            "//*[@id='stationMain']/span[3]/div[2]/div/div/div[2]/div/div[2]/span[1]/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div[2]/div[13]/div[1]").click()
        time.sleep(1)

    def click_choseteacher(self):
        # 选择带教老师 选择老师00
        choseteacher = self.driver.find_element_by_xpath("//*[@id='content']/div[2]/div/div[1]/div[2]/ul")
        choseteacher.find_element_by_xpath("//*[@id='content']/div[2]/div/div[1]/div[2]/ul/li[5]/label").click()
        time.sleep(1)

    def click_rightbutton(self):
        # 点击向右移动按钮
        clickright = self.driver.find_element_by_xpath("//*[@id='content']/div[2]/div/div[2]")
        clickright.find_element_by_xpath("//*[@id='content']/div[2]/div/div[2]/button[2]").click()
        time.sleep(1)

    def click_submitbutton(self):
        # 点击提交按钮
        submitbutton = self.driver.find_element_by_xpath("//*[@id='content']/div[4]")
        submitbutton.find_element_by_xpath("//*[@id='content']/div[4]/button[1]").click()
        time.sleep(1)

    def click_pingfen(self):
        # 点击评分表按钮
        pingfenbutton = self.driver.find_element_by_xpath(
            "//*[@id='stationMain']/span[3]/div[2]/div/div/div[2]/div/div[2]/form/div/div/div/div/div[3]/table/tbody/tr/td[4]/div")
        pingfenbutton.find_element_by_xpath(
            "//*[@id='stationMain']/span[3]/div[2]/div/div/div[2]/div/div[2]/form/div/div/div/div/div[3]/table/tbody/tr/td[4]/div/button[1]").click()
        time.sleep(1)

    def click_pf_quren(self):
        # 点击评分表中的确定按钮
        pingfensubmitbutton = self.driver.find_element_by_xpath(
            "//*[@id='stationMain']/span[3]/div[2]/div/div/div[2]/div/div[2]/span[2]/div[2]/div/div/div[2]/div/div")
        pingfensubmitbutton.find_element_by_xpath(
            "//*[@id='stationMain']/span[3]/div[2]/div/div/div[2]/div/div[2]/span[2]/div[2]/div/div/div[2]/div/div/button[1]").click()
        time.sleep(1)

    def get_elements_teacher(self):
        tr = self.driver.find_element_by_xpath(
            "//*[@id='stationMain']/span[3]/div[2]/div/div/div[2]/div/div[2]/form/div/div/div/div/div[3]/table/tbody/tr")
        teacher = tr.find_element_by_xpath(
            "//*[@id='stationMain']/span[3]/div[2]/div/div/div[2]/div/div[2]/form/div/div/div/div/div[3]/table/tbody/tr/td[1]").text
        return teacher

    def click_nextbutton(self):
        # 点击下一步按钮
        nextbutton = self.driver.find_element_by_xpath(
            "//*[@id='stationMain']/span[3]/div[2]/div/div/div[2]/div/div[2]/div[2]")
        nextbutton.find_element_by_xpath(
            "//*[@id='stationMain']/span[3]/div[2]/div/div/div[2]/div/div[2]/div[2]/button").click()
        time.sleep(1)

    """--------------------------------信息预览-----------------------------"""
    def click_finishbutton(self):
        # 点击完成按钮

        finishbutton = self.driver.find_element_by_xpath(
            "//*[@id='stationMain']/span[3]/div[2]/div/div/div[2]/div/div[2]/div[3]/div")
        finishbutton.find_element_by_xpath(
            "//*[@id='stationMain']/span[3]/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/button").click()
        time.sleep(1)

    """--------------------------------设置权重------------------------------------"""

    def click_quanzhong(self):
        # 设置权重
        self.driver.find_element_by_xpath("//*[@id='stationMain']/div[3]/button[4]").click()
        time.sleep(1)

    def send_keys_quanzhong(self,text):
        # 输入权重值
        quanzhong = self.driver.find_element_by_xpath(
            "//*[@id='stationMain']/span[7]/div[2]/div/div/div[2]/div/table/tbody/tr/td[2]/div")
        quanzhong.find_element_by_xpath(
            "//*[@id='stationMain']/span[7]/div[2]/div/div/div[2]/div/table/tbody/tr/td[2]/div/form/div/div/div/input").send_keys(
            text)
        time.sleep(1)

    def click_save(self):
        # 点击保存按钮
        save = self.driver.find_element_by_xpath("//*[@id='stationMain']/span[7]/div[2]/div/div/div[2]/div/div/div")
        save.find_element_by_xpath("//*[@id='stationMain']/span[7]/div[2]/div/div/div[2]/div/div/div/button[1]").click()
        time.sleep(1)

    # 不用抽题时，点击选择房间按钮
    def click_notchouti_room(self):
        self.driver.find_element_by_xpath(
            "//*[@id='stationMain']/span[3]/div[2]/div/div/div[2]/div/div[2]/form/div/div[5]/div/div/button").click()
        time.sleep(1)

    # 不用抽题时，基本信息中的 下一步 按钮
    def click_notchouti_next(self):
        self.driver.find_element_by_xpath(
            "//*[@id='stationMain']/span[3]/div[2]/div/div/div[2]/div/div[2]/form/div/div[6]/button").click()
        time.sleep(1)

    # 不用抽题时点击病例按钮
    def click_notchouti_bingli(self):
        self.driver.find_element_by_xpath(
            "//*[@id='stationMain']/span[3]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr/td[5]/div/button[1]").click()
        time.sleep(1)

    def click_savekaohe(self):
        # 点击保存考核按钮
        self.driver.find_element_by_xpath("//*[@id='stationMain']/div[1]/form/div/div[3]/div/div/button[1]").click()

