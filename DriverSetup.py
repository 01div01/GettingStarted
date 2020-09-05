

from selenium import webdriver

def setup_driver():
    #headless browser
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    driver = webdriver.Chrome(options=option)
    driver.implicitly_wait(10)
    driver.set_window_size('1200', '1000')
    driver.get('https://www.goindigo.in/')
    driver.set_page_load_timeout(10)

    #normal browser
    # driver= webdriver.Chrome("C:\\Users\\Softsuave\\git\\repository2\\MavenProject\\chromedriver.exe")
    # driver.implicitly_wait(10)
    # driver.maximize_window()
    # driver.get('https://www.goindigo.in/')
    # driver.set_page_load_timeout(10)
    # return driver

    return driver




