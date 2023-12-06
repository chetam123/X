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
# Lấy tất cả các cookie từ trang web hiện tại
all_cookies = driver.get_cookies()

# Tìm giá trị của 'auth_token' trong cookie
auth_token = None
for cookie in all_cookies:
    if cookie["name"] == "auth_token":
        auth_token = cookie["value"]
        break

# In ra giá trị của auth_token
if auth_token:
    print("Auth Token:", auth_token)
else:
    print("Không tìm thấy auth_token trong cookie.")

# Đóng trình duyệt
driver.quit()
