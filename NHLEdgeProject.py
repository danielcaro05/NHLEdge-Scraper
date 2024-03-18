from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
url = 'https://edge.nhl.com/en/skater/20232024-regular-8478569'

Overview_XPATH = {'Overview': '//*[@id="overview-section-content"]/div[1]/div/table/tbody'}
SkatingSpeed_XPATH = {'SkatingSpeed': '//*[@id="skatingspeed-section-content"]/div[1]/div/table/tbody'}
SkatingDistance_XPATH = {'SkatingDistance': '//*[@id="skatingdistance-section-content"]/div[1]/div/table/tbody'}
ShotSpeed_XPATH = {'ShotSpeed': '//*[@id="shotspeed-section-content"]/div[1]/div/table/tbody'}
ShotLocation_XPATH = {'ShotLocation': '//*[@id="shotlocation-section-content"]/div[1]/div/table/tbody'}
ZoneTime_XPATH = {'ZoneTime': '//*[@id="zonetime-section-content"]/div[1]/div/table/tbody'}

XPATHS = [Overview_XPATH, SkatingSpeed_XPATH, SkatingDistance_XPATH, ShotSpeed_XPATH, ShotLocation_XPATH,
          ZoneTime_XPATH]


driver.get(url)

wait = WebDriverWait(driver, 45)

for XPATH in XPATHS:
    element = wait.until(EC.visibility_of_element_located((By.XPATH, XPATH[list(XPATH.keys())[0]])))
    print(list(XPATH.keys())[0])
    print(element.text)
    print(f'\n')

print('Testing')

driver.quit()