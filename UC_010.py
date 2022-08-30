from time import sleep
from login import login
from selenium.webdriver.common.by import By
from constants import SLEEP_TIME, driver, RETURN

SEARCH_QUERY = 'farmacologia'

def search():
  login()

  sleep(SLEEP_TIME)

  searchInput = driver.find_element(By.NAME, 'q')
  searchInput.send_keys(SEARCH_QUERY)
  searchInput.send_keys(RETURN)

if (__name__ == '__main__'):
  search()
  driver.close()
