import time

import pytest
from selenium import webdriver
import openpyxl
import xlrd




# to Open browser
#@pytest.fixture
driver = webdriver
def launch_browser():
    driver = webdriver.Chrome("C:/Users/Tester/PycharmProjects/Drive_Chat/Chrome/chromedriver.exe")

    driver.maximize_window()
    driver.get(url)
    print("launch Chrome Browser")


launch_browser()

loc = ("C:/Users/Tester/PycharmProjects/Drive_Chat/Helping_Documents/URL_and_Login/Url_and_Credentials.xls")
wb = xlrd.open_workbook("C:/Users/Tester/PycharmProjects/Drive_Chat/Helping_Documents/URL_and_Login/Url_and_Credentials.xls")
sheet = wb.sheet_by_index(0)
#sheet = wb.sheet_names('Sheet1')
url = sheet.cell_value(1,1)
Email = sheet.cell_value(1,3)
Password = sheet.cell_value(1,4)


#webdriver.Chrome.get(url)
#time.sleep(10)
print(url)
print(Email)
print(Password)


#def get_url():

    #webdriver.get(url.hyperlink.target)





#get_url()

# # Give the location of the file
# loc = ("path of file")
#
# # To open Workbook
# wb = xlrd.open_workbook(loc)
# sheet = wb.sheet_by_index(0)
#
# # For row 0 and column 0
# print(sheet.cell_value(0, 0))
