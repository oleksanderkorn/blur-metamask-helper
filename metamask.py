from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import argparse
parser = argparse.ArgumentParser()

# CONFIGURATION DEFAULTS
seed = "ENTER 12 WORDS SEED PHRASE HERE PLEASE PLEASE PLEASE PLEASE PLEASE PLEASE"
collection = "https://blur.io/collection/dotbit"
listPrice = "0.01"

parser.add_argument("--url", default=collection,
                    required=False, help="Blur collection URL, e.g. https://blur.io/collection/dotbit")
parser.add_argument("--price", default=listPrice, required=False,
                    help="NFT listt price in ETH, defaults to 0.01")
parser.add_argument("--seed", default=seed, required=False,
                    help="Mnemonic seed of the wallet to import in MetaMask")

args = parser.parse_args()

if args.seed != None:
    seed = args.seed

if args.url != None:
    collection = args.url

if args.price != None:
    listPrice = args.price


def clickxp(xpath):
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))).click()
    except StaleElementReferenceException:
        print("stale element reference ignored")


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
# Import wallet button
clickxp("//*[@id='app-content']/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button")

time.sleep(1)

seedArr = seed.split(' ')

# Seed Phrase
for x in range(12):
    driver.find_element(
        By.ID, f'import-srp__srp-word-{x}').send_keys(seedArr[x])

# Password
driver.find_element(By.ID, "password").send_keys("password")
driver.find_element(By.ID, "confirm-password").send_keys("password")

# Terms checkbox
clickxp("//*[@id='create-new-vault__terms-checkbox']")
# Import button
clickxp("//*[@id='app-content']/div/div[2]/div/div/div[2]/form/button")
# All Done button
clickxp("//*[@id='app-content']/div/div[2]/div/div/button")
# Click x
clickxp('//*[@id="tippy-tooltip-2"]/div/div[2]/div/div[1]/button')

EXTENSION_ID = 'nkbihfbeogaeaoehlefnkodbefgpgknn'
driver.get('chrome-extension://{}/popup.html'.format(EXTENSION_ID))

# Click x on what's new
clickxp('//*[@id="popover-content"]/div/div/section/div[1]/div/button')

# Open blur
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[2])
driver.get("https://blur.io")

# Connect Wallet
clickxp('//*[@id="__next"]/div/div[3]/div[2]/div[2]/button')
clickxp('//*[@id="METAMASK"]')

# Refresh Metamask Window
driver.switch_to.window(driver.window_handles[0])
driver.refresh()

# Next button
clickxp('//*[@id="app-content"]/div/div[2]/div/div[3]/div[2]/button[2]')
# Connect button
clickxp(
    '//*[@id="app-content"]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]')

time.sleep(5)

driver.refresh()
clickxp('//*[@id="app-content"]/div/div[2]/div/div[3]/button[2]')

time.sleep(1)

driver.switch_to.window(driver.window_handles[2])
driver.refresh()

# Go to collection
driver.get(collection)

# Select cheapest NFT
clickxp(
    '//*[@id="collection-main"]/div[2]/div/div[2]/div/div/div[1]/div[1]/div/input')
# Click Buy Button
clickxp('//*[@id="__next"]/div/main/div/div[4]/button')
time.sleep(2)

# Switch to MetaMask
driver.switch_to.window(driver.window_handles[0])
time.sleep(2)
driver.refresh()

# Click on pending approval
clickxp('//*[@id="app-content"]/div/div[2]/div/div[4]/div/button')

# Scroll to bottom
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)

# Click Confirm Button
clickxp('//*[@id="app-content"]/div/div[2]/div/div[4]/div[3]/footer/button[2]')
time.sleep(1)

driver.switch_to.window(driver.window_handles[2])

time.sleep(5)

# Go to portfolio
driver.get('https://blur.io/portfolio')
time.sleep(5)

driver.refresh()

# Select NFT to list
clickxp('//*[@id="portfolio-main"]/div[2]/div/div[2]/div/div/div/div[1]/div/input')

# Click List Button
clickxp('//*[@id="__next"]/div/main/div/div[6]/div/button[1]')

# Enable LooksRare
clickxp('//*[@id="__next"]/div/main/div/div[8]/div/div[1]/div[2]/div[4]/button')
# Enable OpenSea
clickxp('//*[@id="__next"]/div/main/div/div[8]/div/div[1]/div[2]/div[5]/button')

# Enter price 00.1 ETH
driver.find_element(
    By.XPATH, '//*[@id="__next"]/div/main/div/div[8]/div/div[2]/div[2]/div[3]/input').send_keys(listPrice)

# Click list button
clickxp('//*[@id="__next"]/div/main/div/div[8]/div/div[6]/button')

# Switch to MetaMask
driver.switch_to.window(driver.window_handles[0])
time.sleep(1)

# close what's new label
clickxp('//*[@id="popover-content"]/div/div/section/div[1]/div/button')

time.sleep(20)

# Click on pending approvals three times
for x in range(3):
    driver.refresh()
    time.sleep(3)
    # Scroll to bottom
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    # Click Confirm Allow access to and transfer of all your [Collection]?
    clickxp('//*[@id="app-content"]/div/div[2]/div/div[7]/footer/button[2]')
    time.sleep(10)

time.sleep(20)

# click on sign messages
for x in range(3):
    driver.refresh()
    time.sleep(3)
    # Click arrow on sign message
    clickxp('//*[@id="app-content"]/div/div[2]/div/div[3]/div[1]')
    # Click Sign
    clickxp('//*[@id="app-content"]/div/div[2]/div/div[4]/button[2]')
    time.sleep(10)

# Back to portfolio
driver.switch_to.window(driver.window_handles[2])
time.sleep(20)
driver.refresh()
