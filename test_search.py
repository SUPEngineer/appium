# @Time : 2021/3/1
# @Author : qiulingfeng
# @File : test_search.py
from appium import webdriver

desire_cap = {
    "deviceName": "127.0.0.1:7555",
    "platformName": "Android",
    "unicodeKeyBoard": "ture"
}


class TestSearch:
    def setup(self):
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.back()
        # self.driver.back()

    def test_search(self):
        """
        1.搜索框中输入阿里巴巴
        2.选择 阿里巴巴-SW
        3.判断股价是否>200
        :return:
        """
        # 点击搜索输入框
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        # 输入阿里巴巴
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        # 点击阿里巴巴-SW
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴-SW']").click()
        # 获取价格
        current_price = float(
            self.driver.find_elements_by_xpath("//*[@resource-id='com.xueqiu.android:id/current_price']")[1].text)
        assert current_price > 200