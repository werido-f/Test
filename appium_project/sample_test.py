from appium import webdriver
caps = {
    "deviceName": "Redmi 6A",
    "automationName": "Appium",
    "platformName": "Android",
    "platformVersion": "9",
    "appPackage": "com.meizu.flyme.flymebbs",
    "appActivity": ".ui.LoadingActivity",
    "noReset": True,
    "unicodeKeyboard": True,
    "resetKeyboard": True
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
el1 = driver.find_element_by_id("android:id/navigationBarBackground")
el1.click()
el2 = driver.find_element_by_id("com.meizu.flyme.flymebbs:id/nx")
el2.send_keys("手机")
el3 = driver.find_element_by_id("com.meizu.flyme.flymebbs:id/o2")
el3.click()
driver.quit()