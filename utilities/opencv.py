import logging
from lib.GraphicalLocator import GraphicalLocator
from selenium.webdriver.common.action_chains import ActionChains


def find_image(browser, img_path):
    img_check = GraphicalLocator(img_path)
    img_check.find_me(browser)

    is_found = True if img_check.threshold['shape'] >= 0.8 and \
                       img_check.threshold['histogram'] >= 0.4 else False

    if is_found:
        logging.info('X of image center to click: {x}, Y of image center to click: {y}'
                     .format(x=img_check.center_x(), y=img_check.center_y()))
        return img_check
    else:
        raise AssertionError('Image is not found')


def click_img_obj(browser, img):
    assert img is not None, 'Image object is None'
    action = ActionChains(browser)
    action.move_by_offset(img.center_x(), img.center_y()).click().perform()
    action.reset_actions()