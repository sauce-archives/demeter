from .base_test import *
import os
import time

@on_platforms(browsers)
class SaucelabsWebTests(BaseTest):

    @classmethod
    def setup_class(cls):
        connection_protocol = "http://"
        selenium_host = "localhost"
        selenium_port = os.environ.get('SELENIUM_PORT', None)
        tunnel_identifier = os.environ.get('TUNNEL_IDENTIFIER', None)
        logger = logging.getLogger('sp_relay_test')
        logger.setLevel(logging.INFO)
        socketHandler = logging.handlers.SocketHandler('localhost',
                logging.handlers.DEFAULT_TCP_LOGGING_PORT)
        logger.addHandler(socketHandler)
        BaseTest.setup_class(connection_protocol, selenium_host, selenium_port, None, logger)

    #Verify that the google.com homepage comes up
    def test_googleHomePage(self):
        if self.enableReporting:
            name = self.id()
            self.logger.info(name + ', action, timestamp, result')
        self.driver.get('https://google.com/')
        title = "Google"
        self.assertEqual(title, self.driver.title, "Google Homepage title does not match")

    #Verify that the SauceLabs.com homepage comes up
    def test_sauceLabsHomePage(self):
        if self.enableReporting:
            name = self.id()
            self.logger.info(name + ', action, timestamp, result')
        self.driver.get('https://saucelabs.com/')
        title = "Cross Browser Testing, Selenium Testing, and Mobile Testing | Sauce Labs"
        self.assertEqual(title, self.driver.title, "Sauce labs Homepage title does not match")

    #Verify that a user can login to the service and reach it's dashboard
    def test_sauceLabsDashboard(self):
        if self.enableReporting:
            name = self.id()
            self.logger.info(name + ', action, timestamp, result')
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
