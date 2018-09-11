from selenium import webdriver


def go_to_url(url, size=None):
        driver = webdriver.Chrome()
        if size is not None:
                x, y = size
                driver.set_window_size(x, y)
        else:
                driver.maximize_window()
        driver.get(url)
        return driver

