*** Settings ***
Documentation    Suite description
Library  SeleniumLibrary
Library  ..\\utilities\\opencv.py

*** Variables ***
${URL}  https://www.python.org/
${BROWSER}  Chrome
${IMG_PATH}  ${CURDIR}\\..\\resource\\image

*** Test Cases ***
001 Image should be clickable
    [Tags]  Normal
    Set Selenium Speed  0.5
    Open Browser  ${URL}  ${BROWSER}
    Maximize Browser Window
    Sleep  5s
    Find Image  ${drv}  ${IMG_PATH}\\python-logo.png

*** Keywords ***
