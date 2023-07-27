import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'

driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get('https://www.kinopoisk.ru/lists/movies/top250/')
    print(driver.page_source)
except Exception as err:
    print(err)
finally:
    driver.quit()

