import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys



def selectPassengerDetails(driver,Adults,Children,Infants):
    driver.find_element_by_xpath("(//input[@name='passenger'])[1]").click()
    for _ in range(1, Adults):
        driver.find_element_by_xpath("(//li[@class='adult-pax-list extra-seat'])[1]//button[@title='Up']").click()
    time.sleep(0.5)
    for _ in range(0, Children):
        driver.find_element_by_xpath("(//li[@class='child-pax-list extra-seat'])[1]//button[@title='Up']").click()
    time.sleep(1)
    for _ in range(0, 4):
        ActionChains(driver).send_keys(Keys.ARROW_DOWN, Keys.ARROW_DOWN).perform()
    time.sleep(0.5)
    for _ in range(0, Infants):
        driver.find_element_by_xpath("(//li[@class='infant-pax-list'])[1]//button[@title='Up']").click()
    time.sleep(0.5)
    driver.find_element_by_xpath("(//button[text()='Done'])[1]").click()


