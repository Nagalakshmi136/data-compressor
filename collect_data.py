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
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get("https://www.google.com/")
# Fetching data from websites
wait = WebDriverWait(driver,500)

# Search for a specific term (e.g., "dog")
search_path = '//textarea[@id="APjFqb"]'
search = wait.until(EC.presence_of_element_located((By.XPATH,search_path)))
search.send_keys('images', Keys.ENTER)

# Click on the "Images" link
# images_path = '//a[@class="LatpMc nPDzT T3FoJb"][@href="/search?sca_esv=5278b46dd4ebd301&sca_upv=1&q=images&uds=AMwkrPuHXmoY7BiPb7RTgtUZNCAPbhIQ27S1-evY-BJ4A1VwSffGROa1UDux1KSvlsJcvcT_MNn79N1xT7vAAESGrOrQJS7QOaotX0lk0v4YlQUa5UMgmZk&udm=2&sa=X&ved=2ahUKEwjNtKG9r6eEAxU_RWwGHc9yA1MQtKgLegQIDxAB""]'
# images = wait.until(EC.presence_of_element_located((By.XPATH,images_path)))
# images[0].click()
# # Scroll down to load more images
# value = 0
# for i in range(5):
#     driver.execute_script("scrollBy(" + str(value) + ",+1000);")
#     value += 1000
#     time.sleep(3)

# # Find the image thumbnails
# try:
#     elem1 = driver.find_element_by_class_name('Q4LuWd')
#     image_urls = elem1.get_attribute('src')
#     image_urls = image_urls.split('\n')
#     for i, src in enumerate(image_urls[:10]):  # Download the first 10 images
#         request.urlretrieve(str(src), f"image_{i}.jpg")
# except:
#     print("Error: Unable to locate image thumbnails.")

# # Close the driver
# driver.quit()

# time.sleep(5)
# driver.quit()
