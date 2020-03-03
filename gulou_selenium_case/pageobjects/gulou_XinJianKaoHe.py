from framework.base_page import BasePage
import time


class XinJianKaoHe(BasePage):

    def jineng(self):
        jinen = self.driver.find_element_by_id("leftwrapperid")
        jnzx = jinen.find_element_by_xpath("//*[@id='leftwrapperid']/div[7]/div")  # 点击技能中心
        jnzx.click()
        time.sleep(2)

    def get_jnzx(self):
        text = self.driver.find_element_by_xpath("//*[@id='leftwrapperid']/div[7]/div/span[2]").text
        print("daying===" + text)
        return text

    def click_tab(self):
        jinen = self.driver.find_element_by_id("leftwrapperid")
        jnzx = jinen.find_element_by_xpath("//*[@id='leftwrapperid']/div[7]/div")  # 点击技能中心
        kaohe = jnzx.find_element_by_xpath("//*[@id='leftwrapperid']/div[7]/ul/li[2]")
        kaohe.find_element_by_xpath("//*[@id='leftwrapperid']/div[7]/ul/li[2]/a/span").click()  # 点击技能考核
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='subMeunwrapperid']/li[2]/div").click()  # 点击场次管理
        time.sleep(1)


        # 点击新建考核
    def click_xjkh(self):
        self.driver.find_element_by_xpath("//*[@id='interval']/div/div[1]/div[1]/button[1]").click()
        time.sleep(1)

    def click_guifan(self):
        # 点击规范考核
        sss = self.driver.find_element_by_xpath("//*[@id='interval']/div/span[1]/div[2]/div/div/div[2]/div/label[1]")
        sss.find_element_by_xpath(
            "//*[@id='interval']/div/span[1]/div[2]/div/div/div[2]/div/label[1]/span[2]").click()
        time.sleep(1)

    def click_queding(self):
        # 点击确定按钮
        mm = self.driver.find_element_by_xpath("//*[@id='interval']/div/span[1]/div[2]/div/div/div[2]/div/div")
        mm.find_element_by_xpath(
            "//*[@id='interval']/div/span[1]/div[2]/div/div/div[2]/div/div/button").click()
        time.sleep(1)

    def input_createinfo(self,text):
        # 输入考核名称
        aa = self.driver.find_element_by_xpath("//*[@id='stationMain']/div[1]/form/div/div[1]/div/div/div")
        aa.find_element_by_xpath("//*[@id='stationMain']/div[1]/form/div/div[1]/div/div/div/input").send_keys(
            text)
        time.sleep(1)

    def send_keys_xiuxi(self,text):
        # 每考几站休息
        kaojizhan = self.driver.find_element_by_xpath(
            "//*[@id='stationMain']/div[1]/form/div/div[4]/div/div/div[1]/div")
        kaojizhan.find_element_by_xpath(
            "//*[@id='stationMain']/div[1]/form/div/div[4]/div/div/div[1]/div/input").send_keys(text)
        time.sleep(1)

    def send_keys_xiuxitime(self,text):
        # 每次休息多长时间
        xiuxishichang = self.driver.find_element_by_xpath(
            "//*[@id='stationMain']/div[1]/form/div/div[5]/div/div/div[1]/div")
        xiuxishichang.find_element_by_xpath(
            "//*[@id='stationMain']/div[1]/form/div/div[5]/div/div/div[1]/div/input").send_keys(text)
        time.sleep(1)

    def send_keys_huanzhantime(self,text):
        # 换站时间
        huanzhanshijian = self.driver.find_element_by_xpath(
            "//*[@id='stationMain']/div[1]/form/div/div[6]/div/div/div/div")
        huanzhanshijian.find_element_by_xpath(
            "//*[@id='stationMain']/div[1]/form/div/div[6]/div/div/div[1]/div/input").send_keys(text)
        time.sleep(1)
    def click_gettime(self):
        # 获取时间
        starttime = self.driver.find_element_by_xpath("//*[@id='stationMain']/div[1]/form/div/div[2]/div/div/div")
        starttime.find_element_by_xpath("//*[@id='stationMain']/div[1]/form/div/div[2]/div/div/div/input").click()
        time.sleep(1)

        qr = self.driver.find_element_by_class_name("el-picker-panel__footer")
        qr.find_element_by_class_name("el-picker-panel__btn").click()
        time.sleep(1)



