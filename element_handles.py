import time

from selenium import webdriver
import unittest

from selenium.webdriver import ActionChains


class Check_element(unittest.TestCase):
    def setUp(self):
        self.browser=webdriver.Firefox()

        self.url="http://test1.zmninfo.com/SimulationElement/"
        self.urll="https://www.baidu.com/"
        self.browser.implicitly_wait(30)
        self.browser.maximize_window()

    def tearDown(self):
        #self.browser.quit()
        pass


    def test_farm(self):


        self.browser.get(self.urll)
        time.sleep(3)

        self.browser._switch_to.frame(self.browser.find_element_by_xpath("//iframe[@name='frame1']"))
        #切换frame
        self.browser.find_element_by_name("q").send_keys("王岐山")
        time.sleep(2)
        self.browser.find_element_by_xpath("//input[@id='sb_form_go']").click()
        time.sleep(2)


        #使用百度进行搜索“江泽民”
        self.browser.switch_to.parent_frame()
        self.browser._switch_to.frame(self.browser.find_element_by_xpath("//iframe[@src='https://www.baidu.com']"))
        time.sleep(2)
        self.browser.find_element_by_xpath("//input[@id='kw']").send_keys("江泽民")
        time.sleep(2)
        self.browser.find_element_by_xpath("//input[@id='su']").click()
        time.sleep(2)
        self.browser._switch_to.parent_frame()
        time.sleep(2)


        #返回列表标题
        self.browser.find_element_by_link_text("返回演示官网").click()
        time.sleep(2)
        self.browser.back()
        time.sleep(2)
       
        self.browser.find_element_by_name("username").send_keys("admin")
        print("刚刚输入的用户名是：")
        time.sleep(3)
        print(self.browser.find_element_by_name("username").text)
        time.sleep(2)
        self.browser.find_element_by_name("password").send_keys("123456")

        self.browser.find_element_by_xpath("//*[@id='loginForm']/input[3]").click()
        time.sleep(2)
        
        self.browser.find_element_by_xpath("/html/body/form[2]/table/tbody/tr[2]/tb[2]/input[@name='t1']").\
            send_keys("hehe")
       
        #点击弹窗
        self.browser.find_element_by_xpath('//input[@name="b1"]').click()
        alert=self.browser.switch_to.alert
        time.sleep(3)
        alert.accept()
        
        # 点击提问窗
        self.browser.find_element_by_xpath('//*[@id="f2"]/input').click()
        time.sleep(3)
        alert=self.browser.switch_to.alert
        print(alert.text)
        alert.send_keys("zhuzhenghuo")
        time.sleep(3)
        alert.accept()
        
        self.browser.find_element_by_xpath('//*[@id="s1Id"]/option[2]').click()
        
        print(self.browser.find_element_by_xpath('//*[@id="t4"]/tbody/tr[2]/td[4]').text)

        target=self.browser.find_element_by_xpath('//*[@id="u1"]/a[8]')

        ActionChains(self.browser).move_to_element(target).click().perform()
        time.sleep(3)
        seting = self.browser.find_element_by_xpath('//*[@id="wrapper"]/div[6]/a[1]')
        seting.click()

        time.sleep(2)















if __name__ =="__main__":
    unittest.main()













