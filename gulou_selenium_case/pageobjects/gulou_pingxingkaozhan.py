from framework.base_page import BasePage
import time


class PingXingKaoZhan(BasePage):
    def click_px_add(self):
        self.driver.find_element_by_xpath(
            "//*[@id='stationRoomBox']/div/div/div[1]/div[1]/button").click()
        time.sleep(1)

    def click_px_kaozhan(self):
        self.driver.find_element_by_xpath("//*[@id='stationRoomBox']/div/div[2]/div[2]/img").click()
        time.sleep(1)

    def click_px_room(self):
        self.driver.find_element_by_xpath(
            "//*[@id='stationMain']/span[3]/div[2]/div/div/div[2]/div/div[2]/form/div/div[6]/div/div/button").click()
        time.sleep(1)

    def get_elements_roomname(self):
        room = self.driver.find_element_by_xpath("//*[@id='stationRoomBox']/div/div[2]/div[2]")
        roomname = room.find_element_by_xpath("//*[@id='stationRoomBox']/div/div[2]/div[2]/p")
        return roomname

