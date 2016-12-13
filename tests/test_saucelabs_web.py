from .base_test import *
import time

@on_platforms(browsers)
class SaucelabsWebTests(BaseTest):

    @classmethod
    def setup_class(cls):
        BaseTest.setup_class()

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
        #verify the title of the dashboard is present and correct
        title = "Sauce Labs | Dashboard"
        self.assertEqual(title, self.driver.title, "Dashboard title does not match")

if __name__ == '__main__':
    unittest.main()
