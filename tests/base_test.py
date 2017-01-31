import unittest
import os
import sys
import new
import time
import json
from selenium.webdriver.remote.remote_connection import RemoteConnection
from selenium import webdriver
from sauceclient import SauceClient

with open('browsers.json') as browsers:
   browsers = json.loads(browsers.read())

# This decorator is required to iterate over browsers
def on_platforms(platforms):
    def decorator(base_class):
        module = sys.modules[base_class.__module__].__dict__
        for i, platform in enumerate(platforms):
            d = dict(base_class.__dict__)
            d['desired_capabilities'] = platform
            name = "%s_%s" % (base_class.__name__, i + 1)
            module[name] = new.classobj(name, (base_class,), d)

    return decorator


class BaseTest(unittest.TestCase):
    username = None
    access_key = None
    selenium_port = None
    selenium_host = None
    connection_protocol = None
    upload = True
    tunnel_identifier = None
    build_tag = None

    # setUp runs before each test case
    def setUp(self):
        name = self.id().split('.')
        self.desired_capabilities['name'] = name[-3] + '.' + name[-1]
        if BaseTest.tunnel_identifier:
            self.desired_capabilities['tunnel-identifier'] = BaseTest.tunnel_identifier
        if BaseTest.build_tag:
            self.desired_capabilities['build'] = BaseTest.build_tag

        #Generate complete remote connection string
        complete_connection_string = "%s%s:%s@%s:%s/wd/hub" % (BaseTest.connection_protocol,BaseTest.username,BaseTest.access_key,BaseTest.selenium_host,BaseTest.selenium_port)
        
        #due to a bug in the python version of selenium, when using an encrypted endpoint we must disable IP resolution or else it fails with an SSL name mismatch error
        if self.connection_protocol=="https://":
            executor = RemoteConnection(complete_connection_string, resolve_ip=False)
        else:
            executor = RemoteConnection(complete_connection_string)

        self.driver = webdriver.Remote(executor, self.desired_capabilities)
        self.driver.implicitly_wait(60)

    # tearDown runs after each test case
    def tearDown(self):
        self.driver.quit()
        sauce_client = SauceClient(BaseTest.username, BaseTest.access_key)
        status = (sys.exc_info() == (None, None, None))
        sauce_client.jobs.update_job(self.driver.session_id, passed=status)

    @classmethod
    def setup_class(cls, connection_protocol, selenium_host, selenium_port, tunnel_identifier):
        cls.connection_protocol = connection_protocol
        cls.selenium_port = selenium_port
        cls.selenium_host = selenium_host
        cls.tunnel_identifier = tunnel_identifier
        cls.username = os.environ.get('SAUCE_USERNAME', None)
        cls.access_key = os.environ.get('SAUCE_ACCESS_KEY', None)
        cls.build_tag = os.environ.get('BUILD_TAG', None)
