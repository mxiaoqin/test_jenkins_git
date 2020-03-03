from framework.base_page import BasePage
import time


class LoginPage(BasePage):
    username = "name=>userName"
    password = "name=>password"
    submit = "id=>submitBtn"
    loginsubimt = "xpath=>//*[@id='login-wrap']/div/input[1]"
    name = "xpath=>//*[@id='app']/div/div[1]/div/div/div[3]/div/a[2]/span[1]"

    # 输入用户名
    def input_username(self, text):
        self.type(self.username, text)

    # 输入密码
    def input_password(self, text):
        self.type(self.password, text)

    # 点击点此进入按钮
    def send_submit_btn(self):
        self.click(self.submit)
        time.sleep(1)

    # 点击进入个人中心按钮
    def send_loginsubmit(self):
        self.click(self.loginsubimt)
        time.sleep(2)

    def get_username(self):
        text = self.get_text(self.name)
        return text
