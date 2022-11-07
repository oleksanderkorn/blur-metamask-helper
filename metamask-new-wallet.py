from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


def clickxp(xpath):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath))).click()


opt = webdriver.ChromeOptions()
opt.add_extension('./metamask.crx')

driver = webdriver.Chrome(options=opt)

driver.switch_to.window(driver.window_handles[0])
original_window = driver.current_window_handle

# Get started button
clickxp("//*[@id='app-content']/div/div[2]/div/div/div/button")
# No thanks button
clickxp(
    "//*[@id='app-content']/div/div[2]/div/div/div/div[5]/div[1]/footer/button[1]")
# # Create wallet button
clickxp('//*[@id="app-content"]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/button')

time.sleep(1)

# Create Password
driver.find_element(By.ID, "create-password").send_keys("password")
# Accept terms
driver.find_element(By.ID, "confirm-password").send_keys("password")
clickxp('//*[@id="app-content"]/div/div[2]/div/div/div[2]/form/div[3]/div')
# Create button
clickxp('//*[@id="app-content"]/div/div[2]/div/div/div[2]/form/button')

# Next checkbox
clickxp('//*[@id="app-content"]/div/div[2]/div/div/div[2]/div/div[1]/div[2]/button')

# Show Seed
clickxp('//*[@id="app-content"]/div/div[2]/div/div/div[2]/div[1]/div[1]/div[5]')

seed = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
    (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div[2]/div[1]/div[1]/div[5]/div[1]'))).text

print(seed)
driver.save_screenshot(f'./{seed}.png')

driver.close()
