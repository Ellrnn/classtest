from time import sleep
from got_to_panel import goToPanel
from selenium.webdriver.common.by import By
from constants import SLEEP_TIME, driver

def message():
  goToPanel()

  sleep(SLEEP_TIME)

  messageUserButton = driver.find_element(By.ID, 'message-user-button')
  messageUserButton.click()


if (__name__ == '__main__'):
  message()
  driver.close()
