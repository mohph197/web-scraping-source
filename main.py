from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

executable_path= '' # path to your chromedriver

# create a new Chrome session (Open the browser)
driver = webdriver.Chrome(executable_path)

# navigate to the page
driver.get("https://mohph197.github.io/web-scraping-workshop/task1.html")

# click on the download button
driver.find_element(By.CSS_SELECTOR, "#downloadButton").click()

# wait until the download is complete
WebDriverWait(driver, 30).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".progress-label"), "Complete!"))

print("Download complete!")