
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
dict_store_detail=list()
dict_store_final_details=dict()
list_store_detail=list()
set_storedetail=set()
Final_Result=''
flight_No=0
countdebug=0
def getFlightDetails(driver,Flight_Count):
    get_From_Place_Code=driver.find_element_by_xpath("//div[@class='travelPlace']/div[1]").text
    get_From_Place_Name=driver.find_element_by_xpath("//div[@class='travelPlace']/div[1]/div/div").text
    get_To_Place_Code=driver.find_element_by_xpath("//div[@class='travelPlace']/div[3]").text
    get_To_Place_Name=driver.find_element_by_xpath("//div[@class='travelPlace']/div[3]/div/div").text
    get_From_Place_Code=get_From_Place_Code[0:3]
    get_To_Place_Code=get_To_Place_Code[0:3]
    print('fromcode is'+get_From_Place_Code)
    print('fromname is'+get_From_Place_Name)
    print('tocode is'+get_To_Place_Code)
    print('toname is'+get_To_Place_Name)
    count=0
    no=0
    for _ in range(1, 2):
        ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
        print("Fetching flight details started")
    for i in range(1, Flight_Count + 1):
        flight = {}
        no=no+1
        if (no == 14):
            for _ in range(0, 3):
                ActionChains(driver).send_keys(Keys.ARROW_UP).perform()
                no = 0

       # driver.find_element_by_xpath("(//label[@class='col price-details '])[1]").text
        check_Text=driver.find_element_by_xpath("(//*[@class='wrap d-flex'])["+str(i)+"]").text
        not_validation="Not Available"
        if(check_Text!=not_validation):
            button = driver.find_element_by_xpath("(//*[text()='Flight Details'])[" + str(i) + "]")
            driver.execute_script("arguments[0].click();", button)
            time.sleep(0.5)
            driver.find_element_by_xpath('//div[@class="flightSummary-cont"]').text
            rows = driver.find_elements_by_xpath("//li[@class='row']")
            rows_Count = len(rows)
            flight['Flight_Price'] = driver.find_element_by_xpath(
                "(//div[@class='flightSummary-cont']/div)[1]/div[1]/div[1]").text
            flight['Day_Date_Time'] = driver.find_element_by_xpath(
                "(//div[@class='flightSummary-cont']/div)[1]/div[2]").text
            for j in range(1, rows_Count + 1):

                text_Name = driver.find_element_by_xpath('(//li[@class="row"]/span[1])[' + str(j) + ']').text
                text_Data = (driver.find_element_by_xpath('(//li[@class="row"]/span[2])[' + str(j) + ']')).text
                text_Name + "=" + text_Data
                flight[text_Name] = text_Data

            count = count + 1
            # countdebug=countdebug+1

            list_store_detail.append(flight)

            # print(dict_store_detail)
            driver.find_element_by_xpath('(//i[@class="icon-close"])[3]').click()


       # element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "(//*[text()='Flight Details'])[" + str(i) + "]")))


        for _ in range(0, 2):
            ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()

    #print(dict_store_detail)
    # list_store_detail.append(dict_store_detail)
    dict_store_final_details['From']=get_From_Place_Name
    dict_store_final_details['fromCode']=get_From_Place_Code
    dict_store_final_details['To']=get_To_Place_Name
    dict_store_final_details['toCode']=get_To_Place_Code
    dict_store_final_details['Flights']=list_store_detail
    Final_Result=dict_store_final_details
   # Final_Result=Final_Result.replace("'",'"')
    print("fetching details finished")
    return Final_Result







