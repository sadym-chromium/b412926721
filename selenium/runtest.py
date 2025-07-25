from selenium import webdriver

options = webdriver.ChromeOptions()

options.enable_bidi = True
options.enable_webextensions = True
options.binary_location = "/Users/sadym/.cache/chromium-bidi/chrome/mac_arm-140.0.7312.0/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing"
# options.binary_location = "/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary"
options.add_argument(
    '--disable-features=HttpsFirstBalancedModeAutoEnable,HttpsUpgrades,LocalNetworkAccessChecks')
options.add_argument("--enable-features=WebBluetooth")
options.add_argument("--disable-infobars")

service = webdriver.ChromeService(service_args=['--log-level=DEBUG'],
                                  log_output='chromedriver.log')
driver = webdriver.Chrome(options=options, service=service)
driver.webextension.install("extension")

driver.switch_to.new_window('tab')
driver.get('chrome-extension://mkeohjlfgalobdegbiheindkfjmgkiem/manifest.json')
# driver.close()
driver.execute_script("window.close()")

driver.switch_to.window(driver.window_handles[0])
driver.switch_to.new_window('window')
print("!!@@## done")
