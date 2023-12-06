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
from selenium.webdriver.common.action_chains import ActionChains

# Tạo một Event để đồng bộ hóa giữa hai luồng
data_written_event = threading.Event()

global flag
flag = False

global code
code = False

global code2
code2 = ""


# Hàm để chạy trong luồng 1 để thực hiện các thao tác Selenium và ghi dữ liệu vào file
def luong_1():
    global flag  # Tham chiếu đến biến toàn cục
    global code  # Tham chiếu đến biến toàn cục
    global code2
    # Khởi tạo trình duyệt Selenium với user-data-dir được chỉ định
    chrome_options = ChromeOptions()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument(f'user-data-dir=C:\\Users\\moret\\OneDrive\\デスクトップ\\py\\Link\\U1')

    # Khởi tạo trình duyệt
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    # Mở một trang web
    driver.get("https://internxt.com/temporary-email")

    # Đợi 5 giây để trang web tải hoàn chỉnh
    time.sleep(3)

    # Tìm thẻ button có văn bản là "Delete email" và thực hiện thao tác click
    delete_button_xpath = "//button[contains(., 'Delete email')]"
    delete_button = driver.find_element(By.XPATH, delete_button_xpath)
    delete_button.click()

    time.sleep(3)

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
                code2 = words_list[0]
                # Write to a file

                if code2 != "":
                    code = True
                    flag = False
                    print("Extracted data:", code2)
                    break
                # Đóng file sau khi hoàn thành
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
    global code2
    while True:
        # Đợi sự kiện cho biết dữ liệu đã được ghi
        data_written_event.wait()

        # Kiểm tra nếu file email.txt có dữ liệu
        if os.path.exists('email.txt') and os.path.getsize('email.txt') > 0:
            # Đọc nội dung từ file và in ra màn hình
            with open("email.txt", "r", encoding="utf-8") as file:
                content = file.read()
                print("Content in email.txt:", content)

            # Khởi tạo trình duyệt Selenium với user-data-dir được chỉ định
            chrome_options = ChromeOptions()
            chrome_options.add_argument(f'/Users/dev/Desktop/XProjet/User/U1')
            # chrome_options.add_argument('--headless')

            # Khởi tạo trình duyệt
            driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()),
                options=chrome_options
            )
            # Mở trang Google.com bằng Selenium
            driver = webdriver.Chrome()  # Cần đảm bảo bạn đã cài đặt ChromeDriver và đường dẫn nó trong biến môi trường PATH
            driver.get('https://twitter.com/')

            # Ngủ 3 giây (hoặc thời gian cần thiết) để đảm bảo trang web đã mở
            time.sleep(3)

            # nhấn nút Tạo tài khoản
            click_button(driver, 'Tạo tài khoản')

            # Đọc nội dung từ các file
            ho_list = read_file('/Users/dev/Desktop/XProjet/Name/Ho/Ho.txt')
            dem_list = read_file('/Users/dev/Desktop/XProjet/Name/Dem/Dem.txt')
            ten_list = read_file('/Users/dev/Desktop/XProjet/Name/Ten/Ten.txt')

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

            flag = True
            while True:
                if code2 != "":
                    print(f"ma code2'{code2}' ")
                    time.sleep(1)
                    fill_input_field(driver, "verfication_code", code2)
                    # nhấn nút tiếp theo
                    click_button(driver, 'Tiếp theo')
                    break
            # nhâp Mật khẩu
            fill_input_field(driver, "password", "Congtam@779")
            # nhấn nút tiếp theo
            click_button(driver, 'Tiếp theo')

            time.sleep(random.uniform(0.1, 0.3))

            data_written_event.clear()

            # Ngủ 5 giây (hoặc thời gian cần thiết) để đảm bảo trang web đã mở
            time.sleep(50)

            # Đóng trình duyệt
            driver.quit()

        # Ngủ 1 giây trước khi lặp lại
        time.sleep(1)


def select_random_option(driver, select_id, start, end, sleep_time=1):
    time.sleep(sleep_time)

    # Find the <select> element by its ID
    select_element = driver.find_element(By.ID, select_id)

    # Create a Select object
    select = Select(select_element)

    # Generate a random index between start and end (inclusive)
    random_index = random.randint(start, end)

    # Select the option at the random index
    select.select_by_value(str(random_index))

    # Đặt lại sự kiện để chuẩn bị cho vòng lặp tiếp theo
    time.sleep(sleep_time)


def click_button(driver, button_text, sleep_time=2):
    next_button_xpath = f"//span[contains(., '{button_text}')]"
    next_button = driver.find_element(By.XPATH, next_button_xpath)
    next_button.click()
    time.sleep(sleep_time)


def fill_input_field(driver, input_name, input_value, sleep_time=3, typing_delay=0.1):
    element_found = False
    try:
        input_element = driver.find_element(By.NAME, input_name)
        input_element.clear()
        input_element.send_keys(input_value)
        # Use ActionChains to simulate typing with a delay between characters
        time.sleep(sleep_time)
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


# Tạo và bắt đầu các luồng
thread_1 = threading.Thread(target=luong_1)
thread_2 = threading.Thread(target=luong_2)

thread_1.start()
thread_2.start()
