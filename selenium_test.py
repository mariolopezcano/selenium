from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome('./chromedriver')
#driver.get("https://www.python.org")
driver.get("https://dineshvelhal.github.io/testautomation-playground/advanced.html")
print(driver.title)
star_rating = driver.find_element(By.CSS_SELECTOR, "label.star-rating").get_attribute("innerHTML")
print(WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "label.star-rating"))).text)
print("hello",star_rating)
#print([star_rating.text for star_rating in driver.find_elements(By.CLASS_NAME,"star-rating")])
search_bar = driver.find_element(By.ID,"txt_rating")
print("hello search bar",search_bar)
search_bar.send_keys("**")
print("Value of input box: " + search_bar.get_attribute('value'))
my_button = driver.find_element(By.CSS_SELECTOR,"button.btn.btn-primary.shadow-sm").click()
time.sleep(1)
search_bar.send_keys(Keys.RETURN)
print(driver.current_url)
driver.close()