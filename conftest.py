import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    waits = WebDriverWait(pytest.driver, 5)
    pytest.driver.get('https://petfriends.skillfactory.ru/login')
    waits.until(EC.presence_of_element_located((By.ID, "email")))
    pytest.driver.find_element(By.ID, 'email').send_keys('fortesting@mail.ru')
    waits.until(EC.presence_of_element_located((By.ID, "pass")))
    pytest.driver.find_element(By.ID, 'pass').send_keys('123123')
    waits.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    yield

    pytest.driver.quit()