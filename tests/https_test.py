from .base_test import *
import time

@on_platforms(browsers)
class SaucelabsWebTests(BaseTest):

    @classmethod
    def setup_class(cls):
        connection_protocol = "https://"
        selenium_host = "ondemand.saucelabs.com"
        selenium_port = "443"
        BaseTest.setup_class(connection_protocol, selenium_host, selenium_port, None)

    #Verify that the SauceLabs.com homepage comes up
    def test_googleHomePage(self):
        self.driver.get('https://saucelabs.com/')
        title = "Cross Browser Testing, Selenium Testing, and Mobile Testing | Sauce Labs"
        self.assertEqual(title, self.driver.title, "Homepage title does not match")

    #Verify that the SauceLabs.com homepage comes up
    def test_sauceLabsHomePage(self):
        self.driver.get('https://saucelabs.com/')
        title = "Cross Browser Testing, Selenium Testing, and Mobile Testing | Sauce Labs"
        self.assertEqual(title, self.driver.title, "Homepage title does not match")

    #Verify that a user can login to the service and reach it's dashboard
    def test_sauceLabsDashboard(self):
        #login to Saucelabs.com
        self.driver.get('https://saucelabs.com/beta/login')
        self.driver.find_element_by_name('username').send_keys('testybesty10')
        self.driver.find_element_by_name('password').send_keys('testybesty10')
        self.driver.find_element_by_id('submit').click()
        #Verify 'new manual session' button is present, this ensures the page has completed loading before verifying the title
        self.driver.find_element_by_name('icn-tabbar-manual')
        #Verify dashboard title
        self.assertEqual("Sauce Labs | Dashboard", self.driver.title, "Dashboard title does not match")

if __name__ == '__main__':
    unittest.main()