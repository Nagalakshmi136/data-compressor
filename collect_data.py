# Import the libraries
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
from urllib import request

# Initializing web browser
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com/")
# Fetching data from websites
wait = WebDriverWait(driver,500)

# Search for a specific term (e.g., "dog")
search_path = '//textarea[@id="APjFqb"]'
search = wait.until(EC.presence_of_element_located((By.XPATH,search_path)))
search.send_keys('images', Keys.ENTER)
images_path = '//div[@id="bqHHPb"]/div/div/div/div[1]/a'
images = wait.until(EC.presence_of_element_located((By.XPATH,images_path)))
images.click()
value = 0
for i in range(100):
    driver.execute_script("scrollBy(" + str(value) + ",+1000);")
    value += 1000
    time.sleep(3)
imgResults = wait.until(EC.presence_of_all_elements_located((By.XPATH,"//img[contains(@class,'Q4LuWd')]")))
for ind, img in enumerate(imgResults):
    try:
        request.urlretrieve(str(img.get_attribute('src')),"data/img{}.jpg".format(ind))
    except:
        continue

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
from urllib import request

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://pexels.com/search/beautiful/")
# Fetching data from websites
wait = WebDriverWait(driver,500)

# Search for a specific term (e.g., "dog")
# search_path = '//textarea[@id="APjFqb"]'
# search = wait.until(EC.presence_of_element_located((By.XPATH,search_path)))
# search.send_keys('images', Keys.ENTER)
# images_path = '//div[@id="bqHHPb"]/div/div/div/div[1]/a'
# images = wait.until(EC.presence_of_element_located((By.XPATH,images_path)))
# images.click()
images_path = "//img[contains(@class,'MediaCard_image__ljFAl')]"
# Scroll down to load more images
value = 0
for i in range(5):
    driver.execute_script("scrollBy(" + str(value) + ",+1000);")
    value += 1000
    time.sleep(5)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(10)
imgResults = wait.until(EC.presence_of_all_elements_located((By.XPATH,images_path)))

# driver.quit()
