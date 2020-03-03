from framework.base_page import BasePage
import time


class GetCankaorenyuanInfo(BasePage):

    # 选择参考人员加号
    def click_add_button(self):

        self.driver.find_element_by_xpath("//*[@id='stationMain']/div[2]/div[1]/div[2]/fieldset/legend/button").click()
        #self.click(self.add_button)
    def get_textrenyuan(self):
        text = self.driver.find_element_by_xpath("//*[@id='selectUserId']").text
        return text

    # 点击参考人员文件夹
    def click_files(self):
        treeContent = self.driver.find_element_by_class_name("treeContent")
        treeContent.find_element_by_xpath(
            "//*[@id='stationMain']/span[1]/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div[2]/div[10]/div[1]").click()
        time.sleep(3)



    # 点击源列表按钮
    def click_yuanliebiao(self):
        yuanliebiao = self.driver.find_element_by_xpath(
            "//*[@id='content']/div[2]/div/div[1]/div[1]/label/span/span")
        yuanliebiao.find_element_by_xpath(
            "//*[@id='content']/div[2]/div/div[1]/div[1]/label/span/input").click()
        time.sleep(1)

    def get_button_state(self):
        text = self.driver.find_element_by_xpath("//*[@id='content']/div[2]/div/div[1]/div[1]/span[2]")
        return text

    def get_element_display(self):
        ul = self.driver.find_element_by_xpath("//*[@id='content']/div[2]/div/div[1]/div[2]/ul")
        students = ul.find_element_by_xpath("//*[@id='content']/div[2]/div/div[1]/div[2]/ul/li[1]").text
        return students
        # 点击向右移动按钮
    def click_right_button(self):
        #self.click(self.right_button)
        self.driver.find_element_by_xpath("//*[@id='content']/div[2]/div/div[2]/button[2]").click()
        time.sleep(1)

        # 点击提交按钮
    def click_commit_button(self):
        #self.click(self.commit_button)
        self.driver.find_element_by_xpath("//*[@id='content']/div[4]/button[1]").click()
        time.sleep(1)
