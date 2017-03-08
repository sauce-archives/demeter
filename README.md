# Demeter - Goddess of the harvest

Testing code which monitors and reports on the stability of Sauce Labs services.

This code is provided on an "AS-IS” basis without warranty of any kind, either express or implied, including without limitation any implied warranties of condition, uninterrupted use, merchantability, fitness for a particular purpose, or non-infringement. Your tests and testing environments may require you to modify this framework. Issues regarding this framework should be submitted through GitHub. For questions regarding Sauce Labs integration, please see the Sauce Labs documentation at https://wiki.saucelabs.com/. This framework is not maintained by Sauce Labs Support.

Dependencies

# Importnat Environment Variables
Demeter is designed to be run independanly but also to fit well into a Jeknins instance.  In order to run, the following enviornment varibales are needed.

SAUCE_USERNAME
SAUCE_ACCESS_KEY
TUNNEL_IDENTIFIER
ENABLE_SAUCE_REPORTING (optional)

# Required Python Packages
* pytest (3.0.5)
* pytest-xdist (1.15.0)
* sauceclient (0.2.1)
* selenium (3.0.1)

# How to run
* From the command prompt, navigate to the demeter/tests/ directory and enter '>py.test -n X' where x is the number of tests you would like to run in paralellel.
