import time


def selectMonthFromCalender(driver,Date,Month):
    flag = True
    falg1=True
    Month_Name = ''
    time.sleep(1)

    if Month == 'Jan':
        Month_Name = 'January'
    elif Month == 'Feb':
        Month_Name = 'February'
    elif Month == 'Mar':
        Month_Name = 'March'
    elif Month == 'Apr':
        Month_Name = 'April'
    elif Month == 'May':
        Month_Name = 'May'
    elif Month == 'Jun':
        Month_Name = 'June'
    elif Month == 'Jul':
        Month_Name = 'July'
    elif Month == 'Aug':
        Month_Name = 'August '
    elif Month == 'Sep':
        Month_Name = 'September'
    elif Month == 'Oct':
        Month_Name = 'October'
    elif Month == 'Nov':
        Month_Name = 'November'
    elif Month == 'Dec':
        Month_Name = 'December'
    print(Month_Name)
    Month_Text = driver.find_element_by_xpath("(//span[@class='ui-datepicker-month'])[1]").text
    time.sleep(1)
    print(Month_Text)


    while (flag == True):
        if (Month_Text != Month_Name):
            driver.find_element_by_xpath("(//a[text()='7'])[2]").click()
            time.sleep(0.5)
            if(driver.find_element_by_xpath("//i[@class='icon-close close-pass-tooltip']").is_displayed()):
                driver.find_element_by_xpath("//i[@class='icon-close close-pass-tooltip']").click()
            driver.find_element_by_xpath("(//input[@placeholder='Departure Date'])[1]").click()
            Month_Text = driver.find_element_by_xpath("(//span[@class='ui-datepicker-month'])[1]").text
            print(Month_Text)

        else:
            driver.find_element_by_xpath("//a[text()='"+Date+"']").click()
            flag = False



