import threading

import pyautogui
import pyperclip
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import os
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

# Tạo một Event để đồng bộ hóa giữa hai luồng
data_written_event = threading.Event()

global flag
flag = False

global code
code = False


# Hàm để chạy trong luồng 1 để thực hiện các thao tác Selenium và ghi dữ liệu vào file
def luong_1():
    global flag  # Tham chiếu đến biến toàn cục
    global code # Tham chiếu đến biến toàn cục
    # Khởi tạo trình duyệt Selenium với user-data-dir được chỉ định
    chrome_options = ChromeOptions()
    chrome_options.add_argument('--headless')
    # chrome_options.add_argument(f'user-data10-dir=C:\\Users\\moret\\OneDrive\\デスクトップ\\py\\Link\\U1')

    # Khởi tạo trình duyệt
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    # Mở một trang web
    driver.get("https://internxt.com/temporary-email")

    # Tìm thẻ button có văn bản là "Delete email" và thực hiện thao tác click
    delete_button_xpath = "//button[contains(., 'Delete email')]"
    delete_button = driver.find_element(By.XPATH, delete_button_xpath)
    delete_button.click()

    time.sleep(2)

    # Tìm thẻ button có văn bản là "Delete email" và thực hiện thao tác click
    delete_button_xpath = "//button[contains(., 'Copy email')]"
    delete_button = driver.find_element(By.XPATH, delete_button_xpath)
    delete_button.click()

    time.sleep(2)

    # Tìm phần tử bằng đường dẫn XPath đầy đủ
    email_div = driver.find_element(By.XPATH,
                                    "//div[contains(@class, 'flex') and contains(@class, 'h-full') and contains(@class, 'w-full') and contains(@class, 'cursor-pointer') and contains(@class, 'flex-row') and contains(@class, 'items-center') and contains(@class, 'justify-between') and contains(@class, 'rounded-xl') and contains(@class, 'bg-gray-1') and contains(@class, 'shadow-sm') and contains(@class, 'px-4') and contains(@class, 'py-3')]")

    # Lấy nội dung văn bản của phần tử
    element_text = email_div.text

    # Ghi nội dung vào file a.txt
    with open("email.txt", "w", encoding="utf-8") as file:
        file.write(element_text)

    # Đóng file sau khi hoàn thành
    file.close()

    # Đặt sự kiện để thông báo cho luồng 2 rằng dữ liệu đã được ghi
    data_written_event.set()

    # In ra màn hình
    print("Element text:", element_text)

    while True:
        if flag:
            driver.refresh()
            time.sleep(1)

            # Find the <p> element by XPath with class
            xpath_expression = "//p[contains(@class, 'flex-row') and contains(@class, 'text-sm') and contains(@class, 'font-semibold') and contains(@class, 'line-clamp-2')]"
            try:
                # Try to find the <p> element by XPath
                p_element = driver.find_element(By.XPATH, xpath_expression)

                # Get the text content of the <p> element
                text_content = p_element.text

                # Tách chuỗi thành danh sách các từ
                words_list = text_content.split()

                # Lấy phần tử đầu tiên của danh sách
                first_word = words_list[0]

                # Write to a file
                if first_word:
                    with open("code.txt", "w") as file:
                        file.write(first_word)
                        code = True
                        flag = False
                        break
                    # Print the extracted data on the console
                    print("Extracted data:", first_word)

            except:
                # Handle the case when the element is not found
                print("The element with XPath '{}' was not found.".format(xpath_expression))

            # Close the WebDriver
    time.sleep(3)
    driver.quit()


# Hàm để chạy trong luồng 2 để mở trang Google.com sau khi dữ liệu đã được ghi vào file
def luong_2():
    global flag  # Tham chiếu đến biến toàn cục
    global code  # Tham chiếu đến biến toàn cục

    # Đợi sự kiện cho biết dữ liệu đã được ghi
    data_written_event.wait()

    # Kiểm tra nếu file email.txt có dữ liệu
    if os.path.exists('email.txt') and os.path.getsize('email.txt') > 0:
        # Đọc nội dung từ file và in ra màn hình
        with open("email.txt", "r", encoding="utf-8") as file:
            content = file.read()

            print("Content in email.txt:", content)

        # Ngủ 3 giây (hoặc thời gian cần thiết) để đảm bảo trang web đã mở
        # click vào tạo ac mới
        time.sleep(1)
        image_NewAC = 'IMG/NewAC.png'
        click_image(image_NewAC)

        # Đọc nội dung từ các file
        ho_list = read_file('Name/Ho/Ho.txt')
        dem_list = read_file('Name/Dem/Dem.txt')
        ten_list = read_file('Name/Ten/Ten.txt')

        # Tạo và in kết quả cuối cùng
        full_name = generate_full_name(ho_list, dem_list, ten_list)
        pyperclip.copy(full_name)
        # điền tên vào
        time.sleep(1)
        pyautogui.hotkey('command', 'v')  # Dán nội dung từ clipboard

        # chọn kiểu nhập là mail
        image_StypeMail = 'IMG/StypeMail.png'
        click_image(image_StypeMail)

        # điền mail vào
        image_mail = 'IMG/Mail.png'
        click_image(image_mail)

        # điền mail vào
        pyperclip.copy(content)
        pyautogui.hotkey('command', 'v')  # Dán nội dung từ clipboard

        # điền tháng vào
        image_Month = 'IMG/Month.png'
        click_image(image_Month)

        #  chọn tháng 6
        image_Friday = 'IMG/Friday.png'
        click_image(image_Friday)

        # điền chọn ngày
        image_Date = 'IMG/Date.png'
        click_image(image_Date)

        # điền chọn ngày 7
        image_7 = 'IMG/7.png'
        click_image(image_7)

        #  chọn năm
        image_year = 'IMG/year.png'
        click_image(image_year)

        #  chọn năm
        image_1994 = 'IMG/1994.png'
        while True:
            image_location = pyautogui.locateOnScreen(image_1994)

            if image_location is not None:
                center_x, center_y = pyautogui.center(image_location)
                pyautogui.moveTo(center_x, center_y)
                time.sleep(random.uniform(0.1, 1.0))
                pyautogui.click()
                break  # Kết thúc vòng lặp nếu hình ảnh được tìm thấy

            # Thực hiện cuộc scroll xuống nếu hình ảnh không được tìm thấy
            pyautogui.scroll(-5)  # 1 đơn vị là một cuộc scroll xuống
            time.sleep(random.uniform(0.1, 0.3))

        #  chọn next1
        time.sleep(random.uniform(0.1, 0.3))
        click_image('IMG/Next1.png')

        #  chọn next1
        time.sleep(random.uniform(0.1, 0.3))
        click_image('IMG/Next2.png')

        #  chọn đăng ky
        time.sleep(random.uniform(0.1, 0.3))
        click_image('IMG/DK.png')
        time.sleep(5)
        flag = True
        while True:
            if code:
                if os.path.exists('code.txt') and os.path.getsize('code.txt') > 0:
                    # Đọc nội dung từ file và in ra màn hình
                    with open("code.txt", "r", encoding="utf-8") as file:
                        code = file.read()

                    time.sleep(2)
                    pyautogui.write(code, interval=0.1)
                    break
        time.sleep(random.uniform(0.1, 0.3))
        click_image('IMG/Next3.png')


def click_image(image_filename):
    image_location = pyautogui.locateOnScreen(image_filename)

    if image_location is not None:
        center_x, center_y = pyautogui.center(image_location)
        pyautogui.moveTo(center_x, center_y)
        time.sleep(1)
        pyautogui.click()

    else:
        print(f"Hình ảnh {image_filename} không được tìm thấy trên màn hình.")

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def generate_full_name(ho, dem, ten):
    ho_chon = random.choice(ho)
    dem_chon = random.choice(dem)
    ten_chon = random.choice(ten)

    full_name = f"{ho_chon} {dem_chon} {ten_chon}"
    return full_name

# Tạo và bắt đầu các luồng
thread_1 = threading.Thread(target=luong_1)
thread_2 = threading.Thread(target=luong_2)

thread_1.start()
thread_2.start()
