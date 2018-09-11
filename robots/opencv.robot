*** Settings ***
Documentation    Suite description
#Library  SeleniumLibrary
Library  ..\\utilities\\opencv.py
Library  ..\\utilities\\selenium_util.py
Library  ..\\lib\\CustomSeleniumLibrary.py

*** Variables ***
${URL}  https://www.python.org/
${BROWSER}  Chrome
${IMG_PATH}  ${CURDIR}\\..\\resource\\image

*** Test Cases ***
#Open browser by Selenium webdriver
001 Image should be clickable - selenium
    [Tags]  Normal
    ${driver}=  Go To Url  ${URL}
    Sleep  5s
    ${img_obj}=  Find Image  ${driver}  ${IMG_PATH}\\python-logo.png
    Click Img Obj  ${driver}  ${img_obj}

#Open browser by Robot keyword
002 Image should be clickable - robot
    [Tags]  Normal
    Open Browser  ${URL}  ${BROWSER}
    Maximize Browser Window
    Sleep  5s
    ${driver}=  Get Webdriver Instance
    ${img_obj}=  Find Image  ${driver}  ${IMG_PATH}\\python-logo.png
    Click Img Obj  ${driver}  ${img_obj}

*** Keywords ***
