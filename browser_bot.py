from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

url = "https://app.repositorabc.aplicativodeservicos.com.br/"

browser = webdriver.Chrome(r'C:\Users\João Vitor\Desktop\ChromeDriver\chromedriver.exe')
browser.get(url)
field = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div/div[2]/div/div/div/div/form/div[1]/div/input')))
field.click()
field.send_keys('joaovitor@dysrup.com.br')
