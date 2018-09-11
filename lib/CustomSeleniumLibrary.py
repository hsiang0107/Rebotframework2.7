from SeleniumLibrary import SeleniumLibrary
from SeleniumLibrary.base import keyword


class CustomSeleniumLibrary(SeleniumLibrary):

    @keyword
    def get_webdriver_instance(self):
        return self._current_browser()
