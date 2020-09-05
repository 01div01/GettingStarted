

def getFlightCount(driver):
    flights = driver.find_elements_by_xpath('//div[.="Flight Details"]/../../../../..')
    no_Of_Flight = len(flights)
    print('No of flights available :' + str(no_Of_Flight))
    return no_Of_Flight