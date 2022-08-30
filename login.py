from time import sleep
from selenium.webdriver.common.by import By
from constants import RETURN, PASSWORD, USERNAME, driver, WEBSITE_URL, SLEEP_TIME, ACCEPT_COOKIES_XPATH

def login():
  driver.get(WEBSITE_URL)
  driver.maximize_window()

  sleep(SLEEP_TIME)

  acceptCookiesButton = driver.find_element(By.XPATH, ACCEPT_COOKIES_XPATH)
  acceptCookiesButton.click()

  usernameField = driver.find_element(By.ID, 'username')
  usernameField.send_keys(USERNAME)

  passwordField = driver.find_element(By.ID, 'password')
  passwordField.send_keys(PASSWORD)
  passwordField.send_keys(RETURN)

if(__name__ == '__main__'):
  login()
  driver.close()
