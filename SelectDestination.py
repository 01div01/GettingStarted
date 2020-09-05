import time

from selenium.webdriver.common.keys import Keys

import GetFlightCount
import GetFlightDetails
import SelectMonth
import SelectPassengerDetails
from DestroyTheDriver import destroy
from DriverSetup import setup_driver


def capturedata(FlightData):
    driver = setup_driver()
    from_Source = driver.find_element_by_name('or-src')
    from_Source.click()
    input_array = FlightData.split(';')
    from_Source_Name= input_array[1]

    to_Destination_Name=input_array[2]
    date=input_array[3]
    date=date.split('-')
    Departure_Date_Value=date[0]
    Departure_Month_Value=date[1]
    Adults=int(input_array[5])
    Children=int(input_array[6])
    Infants=int(input_array[7])
    from_Source.send_keys(from_Source_Name)
    from_Source.send_keys(Keys.ENTER)

    to_Destination= driver.find_element_by_name('or-dest')
    time.sleep(1)

    to_Destination.send_keys(to_Destination_Name)
    to_Destination.send_keys(Keys.ENTER)


    if(Departure_Date_Value[0]=='0'):
       Departure_Date_Value= Departure_Date_Value.replace('0','')
       print(Departure_Date_Value)
    print(Departure_Date_Value)



    SelectMonth.selectMonthFromCalender(driver,Departure_Date_Value,Departure_Month_Value)

    SelectPassengerDetails.selectPassengerDetails(driver, Adults,Children,Infants)
    #SelectPassengerDetails.selectPassengerDetails(3, 1, 1)

    time.sleep(1)
    search_Flight = driver.find_element_by_xpath("//span[.='Search Flight']")
    search_Flight.click()

    Flight_Count=GetFlightCount.getFlightCount(driver)
    print(Flight_Count)
    Final_Result=GetFlightDetails.getFlightDetails(driver,Flight_Count)
    destroy(driver)
    print(type(Final_Result))
    return Final_Result



#Final_Result=capturedata('One;BLR;CCU;07-Nov-2020;;3;1;1')
# destroy()
#print("return result"+Final_Result)