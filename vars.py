from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeService

# NOTICE: Use of absolute paths is adviced.

# create signal_service and point it to correct version of preinstalled chromedriver
# version should match your electron framework and those can be downloaded from:
# https://github.com/electron/electron/releases under the version, from assets.
signal_service = ChromeService(executable_path=r"/Users/rasjani/src/omat/electron-test/venv/bin/chromedriver")

# And here we construct options that point to use your actual electron app.
signal_electron = Options()
signal_electron.binary_location = r"/Applications/Signal.app/Contents/MacOS/Signal"
