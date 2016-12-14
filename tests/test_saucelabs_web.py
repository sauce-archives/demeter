from .base_test import *
import time

@on_platforms(browsers)
class SaucelabsWebTests(BaseTest):

    @classmethod
    def setup_class(cls):
        BaseTest.setup_class()

    #Verify that google.com can be reached
    def test_googleHomePage(self):
        self.driver.get('https://google.com/')
        self.assertEqual("Google", self.driver.title, "google is not locding correclty")

    #Verify that SauceLabs.com can be reached
    def test_sauceLabsHomePage(self):
        self.driver.get('https://saucelabs.com/')
        self.assertEqual("Cross Browser Testing, Selenium Testing, and Mobile Testing | Sauce Labs", self.driver.title, "sauce labs is not loading correctly")

    #Verify that a user can login to the service and reach it's dashboard
    def test_sauceLabsDashboard(self):
        #login to Saucelabs.com
        self.driver.get('https://saucelabs.com/beta/login')
        self.driver.find_element_by_name('username').send_keys('testybesty10')
        self.driver.find_element_by_name('password').send_keys('testybesty10')
        self.driver.find_element_by_id('submit').click()
        #Verify 'new manual session' button is present, this ensures the page has completed loading before verifying the title
        self.driver.find_element_by_name('icn-tabbar-manual')
        #verify the title of the dashboard is present and correct
        self.assertEqual("Sauce Labs | Dashboard", self.driver.title, "Dashboard is not loading correctly")

if __name__ == '__main__':
    unittest.main()
