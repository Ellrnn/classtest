from time import sleep
from got_to_panel import goToPanel
from selenium.webdriver.common.by import By
from constants import SLEEP_TIME, driver

CUSTOMIZE_PAGE_XPATH = '//*[@id="page"]/header/div/div/div/div[2]/div/div'

def customize():
  goToPanel()

  sleep(SLEEP_TIME)

  messageUserButton = driver.find_element(By.XPATH, CUSTOMIZE_PAGE_XPATH)
  messageUserButton.click()

  sleep(SLEEP_TIME)


if (__name__ == '__main__'):
  customize()
  driver.close()
