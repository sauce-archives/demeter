from .base_test import *
import time

@on_platforms(browsers)
class SaucelabsWebTests(BaseTest):

    @classmethod
    def setup_class(cls):
        BaseTest.setup_class()

    #Verify that the SauceLabs.com homepage comes up
    def test_homepage(self):
        self.driver.get('https://saucelabs.com/')
        title = "Cross Browser Testing, Selenium Testing, and Mobile Testing | Sauce Labs"
        self.assertEqual(title, self.driver.title, "Homepage title does not match")

    #Verify that a user can login to the service and reach it's dashboard
    def test_dashboard_page(self):
        #login to Saucelabs.com
        self.driver.get('https://saucelabs.com/beta/login')
        self.driver.find_element_by_name('username').send_keys('testybesty10')
        self.driver.find_element_by_name('password').send_keys('testybesty10')
        self.driver.find_element_by_id('submit').click()
        #verify the title of the dashboard is present and correct
        title = "Sauce Labs | Dashboard"
        self.assertEqual(title, self.driver.title, "Dashboard title does not match")

    def test_manual_session(self):
        #login to Saucelabs.com
        self.driver.get('https://saucelabs.com/beta/login')
        self.driver.find_element_by_name('username').send_keys('testybesty10')
        self.driver.find_element_by_name('password').send_keys('testybesty10')
        self.driver.find_element_by_id('submit').click()
        #verify that we can reach a test detail page
        self.driver.get('https://saucelabs.com/beta/manual')
        self.driver.find_element_by_xpath("//input[@placeholder='URL you want to test']").send_keys('www.google.com')
        self.driver.find_element_by_id('icn-browser-chromesvg').click()
        #apparently that thing rmebers...dunno how to handle that but am getting bored so moving on for now.
        #self.driver.find_element_by_link_text('53').click()
        #self.driver.find_element_by_link_text('Windows 7').click()
        #self.driver.find_element_by_link_text('1024x768').click()
        self.driver.find_element_by_xpath("//button[contains(text(), 'Start Session')]").click()
        #self.driver.find_element_by_class_name('.btn-start-session').click()
        #self.driver.find_element_by_css_selector('button.btn btn-action btn-start-session').click()
        #abba = self.driver.page_source
        #print(abba.encode('utf-8'))
        time.sleep(10)



if __name__ == '__main__':
    unittest.main()