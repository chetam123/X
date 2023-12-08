from selenium import webdriver
import time
import threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import os
import random
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import os
import random
from selenium.webdriver.support.ui import Select
chrome_options = ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument(f'user-data-dir=C:\\Users\\moret\\OneDrive\\デスクトップ\\py\\Link\\U1')

# Khởi tạo trình duyệt
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)

# Mở một trang web và đăng nhập vào Twitter thủ công
driver.get("https://twitter.com/home")
# Bạn cần đăng nhập thủ công ở đây trước khi chạy tiếp mã JavaScript để lấy cookie
time.sleep(20)
# Chờ cho phần tử xuất hiện trên trang (tối đa 10 giây)
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//span[text()="Profile"]'))
)
# Click vào phần tử
element.click()
time.sleep(220)
