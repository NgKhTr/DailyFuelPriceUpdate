import constants

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import requests
import gc

import time

def is_url_accessible(url):
    try:
        response = requests.get(url)
        status_code = response.status_code
        print("Status code:", status_code)
        return status_code == 200
    except requests.exceptions.RequestException as e:
        return False

def open_web():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(constants.URL)

    time.sleep(1)
    return driver

def get_datetimes(driver):
    
    select_element = driver.find_element(By.ID, "ctl00_mainContent_ctl03_ddlDate")

    select = Select(select_element)
    datetimes = [option_ele.get_attribute('value') for option_ele in select.options]
    datetimes.reverse()
    return datetimes

def get_data(after_date: pd.Timestamp = None):
    driver = open_web()

    datetimes = get_datetimes(driver)

    data = []
    for scan_datetime in datetimes:
        pd_date = pd.to_datetime(scan_datetime.split()[0])
        if after_date is None or pd_date > after_date:
            select_ele = driver.find_element(By.ID, "ctl00_mainContent_ctl03_ddlDate")
            select = Select(select_ele)
            select.select_by_value(scan_datetime)
            time.sleep(5)
            
            row = {}
            row["Date"] = pd_date.strftime(constants.DATE_FORMAT)
            tbody_ele = driver.find_element(By.XPATH, r"//div[@id='cctb-1']/table/tbody")
            for i, row_ele in enumerate(tbody_ele.find_elements(By.TAG_NAME, "tr")):
                item_eles = row_ele.find_elements(By.TAG_NAME, "td")
                name = item_eles[1].text

                if name in ["Xăng RON 95-III", "Xăng E5 RON 92-II"]:
                    price = item_eles[2].text
                    if len(price) > 0:
                        row[name] = float(price)
            data.append(row)
    print(len(data))
    driver.quit()
    del driver
    gc.collect()
    return data
if __name__ == "__main__":
    pass
