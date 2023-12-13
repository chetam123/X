import threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os
import random
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import json
import asyncio
import time
import datetime

import post
import userStorage

# Tạo một Event để đồng bộ hóa giữa hai luồng
data_written_event = threading.Event()
global data
global reset
global path
global canRequestEmail , StartL1
StartL1 = True
path = "C:\\Users\\moret\\Downloads\\xmaster\\"
# data = []

# with open('C:\\Users\\moret\\Downloads\\X-master\\X-master\\user.json', 'r') as json_file:
#     data = json.load(json_file)

# data = userStorage.getAllUser()

global flag
flag = False

global code2
code2 = ""


# Hàm để chạy trong luồng 1 để thực hiện các thao tác Selenium và ghi dữ liệu vào file
def luong_1():
    global canRequestEmail
    print("run luong 1")
    global flag, code2, reset, path ,StartL1

    chrome_options = ChromeOptions()
    chrome_options.add_argument('--headless')

    # Khởi tạo trình duyệt
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    driver.set_window_size(1900, 1080)
    # Mở một trang web
    driver.get("https://internxt.com/temporary-email")

    while True:
        if StartL1 == True :
            reset = False
            code2 = ""
            # Chờ cho nút "Delete email" xuất hiện trong vòng 10 giây
            delete_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(., 'Delete email')]"))
            )

            # Thực hiện thao tác click vào nút "Delete email"
            delete_button.click()

            time.sleep(2)

            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                           "//div[contains(@class, 'flex') and contains(@class, 'h-full') and contains(@class, 'w-full') and contains(@class, 'cursor-pointer') and contains(@class, 'flex-row') and contains(@class, 'items-center') and contains(@class, 'justify-between') and contains(@class, 'rounded-xl') and contains(@class, 'bg-gray-1') and contains(@class, 'shadow-sm') and contains(@class, 'px-4') and contains(@class, 'py-3')]")))

            # Tìm phần tử bằng đường dẫn XPath đầy đủ
            email_div = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH,
                                                "//div[contains(@class, 'flex') and contains(@class, 'h-full') and contains(@class, 'w-full') and contains(@class, 'cursor-pointer') and contains(@class, 'flex-row') and contains(@class, 'items-center') and contains(@class, 'justify-between') and contains(@class, 'rounded-xl') and contains(@class, 'bg-gray-1') and contains(@class, 'shadow-sm') and contains(@class, 'px-4') and contains(@class, 'py-3')]"))
            )
            # Lấy nội dung văn bản của phần tử
            element_text = email_div.text

            # Ghi nội dung vào file a.txt
            with open(path + "User\\email.txt", "w", encoding="utf-8") as file:
                file.write(element_text)

            # Đóng file sau khi hoàn thành
            file.close()

            # Đặt sự kiện để thông báo cho luồng 2 rằng dữ liệu đã được ghi
            data_written_event.set()

            # In ra màn hình
            try:
                wait = WebDriverWait(driver, 3000)
                wait.until(lambda driver: flag)
                wait = WebDriverWait(driver, 15)
                wait.until(lambda driver: checkCode(driver))
            except:
                print("reset 1")
                reset = True
                flag = False
                return

            xpath_expression = "//p[contains(@class, 'flex-row') and contains(@class, 'text-sm') and contains(@class, 'font-semibold') and contains(@class, 'line-clamp-2')]"
            # Try to find the <p> element by XPath
            p_element = driver.find_element(By.XPATH, xpath_expression)

            # Get the text content of the <p> element
            text_content = p_element.text

            # Tách chuỗi thành danh sách các từ
            words_list = text_content.split()

            # Lấy phần tử đầu tiên của danh sách
            code2 = words_list[0]

            flag = False
            StartL1 = False
            # Close the WebDriver


def checkCode(driver):
    ct = datetime.datetime.now()
    print("current time:-", ct)
    driver.refresh()
    time.sleep(1)
    xpath_expression = "//p[contains(@class, 'flex-row') and contains(@class, 'text-sm') and contains(@class, 'font-semibold') and contains(@class, 'line-clamp-2')]"
    try:
        # Try to find the <p> element by XPath
        p_element = driver.find_element(By.XPATH, xpath_expression)

        # Get the text content of the <p> element
        text_content = p_element.text

        # Tách chuỗi thành danh sách các từ
        words_list = text_content.split()

        # Lấy phần tử đầu tiên của danh sách
        code2 = words_list[0]
        # Write to a file

        if code2 != "":
            code = True
            flag = False
            print("Extracted data:", code2)
        return code2 != ""

    except:
        # print("The element with XPath '{}' was not found.".format(xpath_expression))
        return False


# Hàm để chạy trong luồng 2 để mở trang Google.com sau khi dữ liệu đã được ghi vào file
async def luong_2():
    print("run luong 2")
    global flag  # Tham chiếu đến biến toàn cục
    global code2
    global reset , StartL1
    while True:
        # Đợi sự kiện cho biết dữ liệu đã được ghi
        data_written_event.wait()

        # Kiểm tra nếu file email.txt có dữ liệu
        if os.path.exists(path + "User\\email.txt") and os.path.getsize(
                path + "User\\email.txt") > 0:
            # Đọc nội dung từ file và in ra màn hình
            with open(path + "User\\email.txt", "r",
                      encoding="utf-8") as file:
                content = file.read()
                print("------------------------------------------------------------")
                print("Content in email.txt:", content)

            # Khởi tạo trình duyệt Selenium với user-data-dir được chỉ định
            chrome_options = ChromeOptions()
            chrome_options.add_argument(f'/Users/dev/Desktop/XProjet/User/U1')
            # chrome_options.add_argument('--headless')
            chrome_options.add_argument("--lang=vi")

            # Khởi tạo trình duyệt
            driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()),
                options=chrome_options
            )
            driver.set_window_size(1900, 1080)
            # Mở trang Google.com bằng Selenium

            driver.get('https://twitter.com/')
            driver.maximize_window()
            # Ngủ 3 giây (hoặc thời gian cần thiết) để đảm bảo trang web đã mở

            # nhấn nút Tạo tài khoản
            click_button(driver, 'Tạo tài khoản')

            # Đọc nội dung từ các file
            ho_list = read_file(path + "Name\\Ho\\Ho.txt")
            dem_list = read_file(path + 'Name\\Dem\\Dem.txt')
            ten_list = read_file(path + 'Name\\Ten\\Ten.txt')

            # Tạo và in kết quả cuối cùng
            full_name = generate_full_name(ho_list, dem_list, ten_list)
            print(full_name)

            # nhập tên người dùng
            fill_input_field(driver, "name", full_name)

            # nhấn nút Sử dụng email
            click_button(driver, 'Sử dụng email')

            # nhập mail
            fill_input_field(driver, "email", content)

            #  ngày sinh
            select_random_option(driver, "SELECTOR_1", 1, 12)

            #  tháng sinh
            select_random_option(driver, "SELECTOR_2", 1, 28)

            #  năm sinh
            select_random_option(driver, "SELECTOR_3", 1980, 1995)

            # nhấn nút tiếp theo
            click_button(driver, 'Tiếp theo')

            # nhấn nút tiếp theo
            click_button(driver, 'Tiếp theo')

            # nhấn nút đăng ký
            click_button(driver, 'Đăng ký')

            wait = WebDriverWait(driver, 300)
            wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Chúng tôi đã gửi mã cho bạn"]')))

            flag = True
            while True:
                if(reset):
                    print("reset 2")
                    # Close the WebDriver
                    driver.quit()
                    return
                if code2 != "":
                    time.sleep(1)
                    fill_input_field(driver, "verfication_code", code2)
                    # nhấn nút tiếp theo
                    click_button(driver, 'Tiếp theo')
                    break
            # nhâp Mật khẩu
            fill_input_field(driver, "password", "Congtam@779")

            time.sleep(1)

            # nhấn nút tiếp theo
            click_button(driver, 'Tiếp theo')

            try:
                # Đường dẫn XPath của nút Submit với văn bản "Start"
                submit_button_xpath = "//input[@type='submit' and @value='Start']"

                # Đợi cho đến khi nút Submit xuất hiện trong vòng 3 giây
                submit_button = WebDriverWait(driver, 300).until(
                    EC.presence_of_element_located((By.XPATH, submit_button_xpath))
                )

                # Thực hiện thao tác click trên nút Submit
                submit_button.click()

            except Exception as e:

                print("Không tìm thấy nút Submit trong khoảng thời gian chờ.")
                # Xử lý trường hợp khi nút Submit không được tìm thấy hoặc không xuất hiện (ví dụ: thử lại hoặc ném một ngoại lệ)

            try:
                # Đường dẫn XPath của nút Submit với văn bản "Continue to X"
                submit_button_xpath = "//input[@type='submit' and @value='Continue to X']"

                # Đợi cho đến khi nút Submit xuất hiện trong vòng 3 giây
                submit_button = WebDriverWait(driver, 300).until(
                    EC.presence_of_element_located((By.XPATH, submit_button_xpath))
                )

                # Thực hiện thao tác click trên nút Submit
                submit_button.click()

            except Exception as e:
                print("Không tìm thấy nút Submit trong khoảng thời gian chờ.")
                # Xử lý trường hợp khi nút Submit không được tìm thấy hoặc không xuất hiện (ví dụ: thử lại hoặc ném một ngoại lệ)

            try:
                # Đường dẫn XPath của phần tử div với thuộc tính data-testid là "confirmationSheetConfirm"
                confirmation_div_xpath = "//div[@data-testid='confirmationSheetConfirm']"

                # Đợi cho đến khi phần tử div xuất hiện trong vòng 3 giây
                confirmation_div = WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.XPATH, confirmation_div_xpath))
                )

                # Thực hiện các thao tác trên phần tử div
                confirmation_div.click()

            except Exception as e:
                print("Không tìm thấy phần tử div trong khoảng thời gian chờ.")
                # Xử lý trường hợp khi phần tử không được tìm thấy hoặc không xuất hiện (ví dụ: thử lại hoặc ném một ngoại lệ)

            wait = WebDriverWait(driver, 100)
            desired_url = "/home"
            wait.until(
                lambda driver: desired_url in driver.current_url)
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
                driver.refresh()
                time.sleep(1)
            else:
                print("Không tìm thấy auth_token trong cookie.")

            # Chờ cho phần tử xuất hiện trên trang (tối đa 10 giây)
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//span[text()="Profile"]'))
            )

            # Click vào phần tử
            element.click()

            # Lấy URL hiện tại
            current_url = driver.current_url
            # Tách chuỗi theo dấu "/"
            url_parts = current_url.split("/")

            # Lấy phần tử cuối cùng của danh sách
            last_part = url_parts[-1]

            # In ra phần tử cuối cùng
            print("Phần tử cuối cùng:", last_part)

            new_item = {
                "name": "@" + last_part,
                "mail": content,
                "pass": "Congtam@779",
                "token": auth_token
            }

            # Save the data list to user.json
            userStorage.pushUser(new_item)
            # Update and save the total user count
            update_total_user_count()

            StartL1 = True

            data_written_event.clear()

            ct = datetime.datetime.now()
            print("complete :-", ct)
            post.post(driver)
            # Đóng trình duyệt
            driver.quit()
            break


def select_random_option(driver, select_id, start, end):
    # Find the <select> element by its ID
    select_element = driver.find_element(By.ID, select_id)

    # Create a Select object
    select = Select(select_element)

    # Generate a random index between start and end (inclusive)
    random_index = random.randint(start, end)

    # Select the option at the random index
    select.select_by_value(str(random_index))
    time.sleep(random.uniform(0.1, 0.5))


def click_button(driver, button_text):
    # Đường dẫn XPath của nút tiếp theo với văn bản mong muốn
    next_button_xpath = f"//span[contains(., '{button_text}')]"

    # Đợi cho đến khi nút tiếp theo xuất hiện
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, next_button_xpath)))

    # Tìm nút tiếp theo và thực hiện thao tác click
    next_button = driver.find_element(By.XPATH, next_button_xpath)
    next_button.click()


def update_total_user_count():
    # Check if the totaluser.txt file exists
    total_user_file_path = path + 'totaluser.txt'

    if os.path.exists(total_user_file_path):
        with open(total_user_file_path, 'r') as total_user_file:
            # Read the current count from the file
            current_count = int(total_user_file.read().strip())
    else:
        # If the file doesn't exist, set the count to 0
        current_count = 0

    # Increment the count
    current_count += 1
    print(f"Current User Count Before Increment: {current_count}")
    # Update the totaluser.txt file with the new count
    with open(total_user_file_path, 'w') as total_user_file:
        total_user_file.write(str(current_count))

def fill_input_field(driver, input_name, input_value):
    element_found = False
    try:
        # Đợi cho đến khi phần tử được tìm thấy trong vòng 3 giây
        input_element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.NAME, input_name)))

        # Xóa giá trị hiện tại và nhập giá trị mới
        input_element.clear()
        input_element.send_keys(input_value)

        element_found = True
    except Exception as e:
        print(f"Không tìm thấy phần tử có tên '{input_name}' hoặc thẻ 'Mật khẩu' không xuất hiện.")
        # Xử lý trường hợp khi phần tử không được tìm thấy hoặc thẻ không xuất hiện (ví dụ: thử lại hoặc ném một ngoại lệ)


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


async def main():
    loop = asyncio.get_event_loop()
    loop.run_in_executor(None, luong_1)
    while True:
        task_2 = asyncio.create_task(luong_2())
        await asyncio.wait([task_2])

if __name__ == "__main__":
    asyncio.run(main())
