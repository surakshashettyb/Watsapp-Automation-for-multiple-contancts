from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import datetime
import time
import openpyxl as excel


driver = webdriver.Chrome(r'C:\Users\hp\Desktop\chromedriver.exe')

def readContacts(fileName):
    lst = []
    file = excel.load_workbook(fileName)
    sheet = file.active
    firstCol = sheet['A']
    for cell in range(len(firstCol)):
        contact = (firstCol[cell].value).encode('utf-8')
        lst.append(contact)
    return lst

# Replace below path with the absolute path of the \
#chromedriver in your computer
targets = readContacts(r"C:\Users\hp\Desktop\tt.xlsx")
#print(targets)

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)
wait5 = WebDriverWait(driver, 5)
# Replace the below string with your own message
msg = 'Like and share - Nati Tadka'
#targets =['Mona 1','School']
for target in targets:
    x_arg = '//span[contains(@title,' +'"' +target.decode('utf-8') + '"' +')]' #.decode('utf-8') 
    group_title = wait.until(EC.presence_of_element_located((
        By.XPATH, x_arg)))
    group_title.click()


    message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]

    message.send_keys(msg)
    sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
    sendbutton.click()
driver.close()