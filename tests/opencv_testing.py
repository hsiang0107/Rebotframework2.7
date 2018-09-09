import time
from selenium import webdriver
from utilities.opencv import *
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

URL = 'https://www.python.org/'
# URL = 'http://www.theautomatedtester.co.uk/demo1.html'
img_resource_path = '..\\resource\\image\\'
python_logo = img_resource_path + 'python-logo.png'
# Go_btn = driver.find_element_by_id('submit')
# Download_btn = driver.find_element_by_id('downloads')
# Logo = driver.find_element_by_css_selector('#touchnav-wrapper > header > div > h1')
chrome_path = '..\\webdriver\\chromedriver.exe'
driver = webdriver.Chrome(chrome_path)
driver.maximize_window()
driver.get(URL)
time.sleep(5)
logging.info('Current browser window size: {0}'.format(driver.get_window_size()))
# driver.get_screenshot_as_file('python_base_img.png')

img_obj = find_image(driver, python_logo)
click_img_obj(driver, img_obj)


