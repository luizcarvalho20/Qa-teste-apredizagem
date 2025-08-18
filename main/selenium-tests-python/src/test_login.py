from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://the-internet.herokuapp.com/login"

def test_login_invalido():
    # Abre o Chrome; Selenium Manager cuida do driver automaticamente
    with webdriver.Chrome() as driver:
        driver.get(URL)

        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "username")))

        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("wrongPassword")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Aguarda a mensagem de erro aparecer
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.flash.error")))

        assert "Your password is invalid!" in driver.page_source

if __name__ == "__main__":
    test_login_invalido()
