import time
from selenium import webdriver
from lib.GraphicalLocator import GraphicalLocator
from selenium.webdriver.common.action_chains import ActionChains

chrome_path = '..\\webdriver\\chromedriver.exe'
driver = webdriver.Chrome(chrome_path)
driver.get('https://www.python.org/')
time.sleep(5)


img_check = GraphicalLocator("..\\resource\\image\\python-logo.png")
img_check.find_me(driver)

# is_found = True if img_check.threshold['shape'] >= 0.8 and \
#                    img_check.threshold['histogram'] >= 0.4 else False
#
# if is_found:
#     print(img_check.center_x(), img_check.center_y())

print(img_check.center_x(), img_check.center_y())

action = ActionChains(driver)
action.move_by_offset(img_check.center_x(), img_check.center_y())
# action.move_by_offset(100, 100)
action.click()
action.perform()
