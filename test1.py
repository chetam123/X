from selenium import webdriver
import time
import threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import os
import random
from selenium.webdriver.support.ui import Select
chrome_options = ChromeOptions()
# chrome_options.add_argument('--headless')
chrome_options.add_argument(f'user-data-dir=C:\\Users\\moret\\OneDrive\\デスクトップ\\py\\Link\\U2')

# Khởi tạo trình duyệt
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)

driver.get("https://twitter.com/home")

# Đóng trình duyệt
driver.quit()
