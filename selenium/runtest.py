import time

from selenium import webdriver

options = webdriver.ChromeOptions()

options.enable_bidi = True
options.enable_webextensions = True
options.binary_location = "${CHROME_PATH}"

service = webdriver.ChromeService(
    service_args=['--log-level=ALL', '--enable-chrome-logs'],
    log_output=f'chromedriver.{time.time()}.log',
    executable_path='${CHROMEDRIVER_PATH}'
)

driver = webdriver.Chrome(options=options, service=service)
driver.webextension.install("extension")

driver.switch_to.new_window('tab')
driver.get('chrome-extension://mkeohjlfgalobdegbiheindkfjmgkiem/manifest.json')

driver.execute_script("window.close()")

driver.switch_to.window(driver.window_handles[0])
driver.switch_to.new_window('window')
print("!!@@## done")
