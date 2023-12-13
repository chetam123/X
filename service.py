import threading
from selenium.webdriver.chrome.options import Options as ChromeOptions
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

import post
import userStorage
global indexUser
indexUser = 387
userURL = "ThoThanh49403"
likeID = 1725481928663654424
retweetID = 1725481928663654424
perform_action = "Follow"

def Follow(username):
    token = username['token']
    chrome_options = ChromeOptions()
    chrome_options.add_argument(f'/Users/dev/Desktop/XProjet/User/U1')
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument("--lang=vi")
    # Khởi tạo trình duyệt
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    driver.get(f"https://twitter.com")
    driver.maximize_window()
    # Đăng nhập bằng auth_token
    auth_token = token

    # Thêm auth_token vào cookies
    driver.add_cookie({'name': 'auth_token', 'value': auth_token})

    # Làm mới trang để áp dụng cookie mới
    driver.refresh()

    # try:
    #     # Đường dẫn XPath của phần tử span với văn bản "Đăng nhập"
    #     login_span_xpath = "//span[contains(@class, 'css-1qaijid') and contains(., 'Đăng nhập')]"
    #
    #     # Đợi cho đến khi phần tử span xuất hiện trong vòng 30 giây
    #     login_span = WebDriverWait(driver, 30).until(
    #         EC.presence_of_element_located((By.XPATH, login_span_xpath))
    #     )
    #
    #     # Kiểm tra nếu trang web hiển thị biểu tượng "Đăng nhập"
    #     if "Đăng nhập" in login_span.text:
    #         login(username)
    #     else:
    #         print("Trang web không hiển thị biểu tượng 'Đăng nhập'. Tiếp tục...")
    #         # Thực hiện các hành động khác nếu cần
    #
    # except Exception as e:
    #     print(f"Có lỗi xảy ra: {e}")
    #     print("Không tìm thấy phần tử span trong khoảng thời gian chờ.")
    #     # Xử lý trường hợp khi phần tử không được tìm thấy hoặc không xuất hiện (ví dụ: thử lại hoặc ném một ngoại lệ)

    # Tìm nút theo dõi với WebDriverWait
    wait = WebDriverWait(driver, 3000)
    driver.get(f"https://twitter.com/{userURL}")
    # -----------------------------------------------------------------------------------------------------------------
    # Kiểm tra xem bạn đã theo dõi tài khoản hay chưa
    try:
        follow_button = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[data-testid="placementTracking"]')))
        if "Following" in follow_button.get_attribute("innerText"):
            print(f"Bạn đã theo dõi tài khoản {userURL} rồi.")
        else:
            print(f"Bạn chưa theo dõi tài khoản {userURL}.")
            # Click nút theo dõi
            follow_button.click()
            print(f"Bạn đã bắt đầu theo dõi tài khoản {userURL}.")
            time.sleep(2)
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

    finally:
        # Đóng trình duyệt khi hoàn tất
        driver.quit()
        print(f"Đóng Twitter trong luồng {threading.current_thread().name}")
    # -----------------------------------------------------------------------------------------------------------------


def Like(username):
    token = username['token']
    chrome_options = ChromeOptions()
    # chrome_options.add_argument('--headless')

    chrome_options.add_argument(f'/Users/dev/Desktop/XProjet/User/U1')
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument("--lang=vi")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    driver.set_window_size(1900, 1080)
    driver.get(f"https://twitter.com/intent/like?tweet_id={likeID}")
    # Đăng nhập bằng auth_token
    auth_token = token

    # Thêm auth_token vào cookies
    driver.add_cookie({'name': 'auth_token', 'value': auth_token})

    # Làm mới trang để áp dụng cookie mới
    driver.refresh()
    # Tìm nút theo dõi với WebDriverWait
    wait = WebDriverWait(driver, 10)

    # -----------------------------------------------------------------------------------------------------------------
    try:
        # Tìm đối tượng <span> với văn bản "Like"
        like_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="Like" or text()="thích"]'))
        )

        # Click nút Like
        like_button.click()

        print("Bài viết đã được like.")

    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")
    finally:
        # Đóng trình duyệt khi hoàn tất
        time.sleep(4)
        driver.quit()
        print(f"Đóng Twitter trong luồng {threading.current_thread().name}")
    # -----------------------------------------------------------------------------------------------------------------


def retweet(username):
    token = username['token']
    chrome_options = ChromeOptions()
    # chrome_options.add_argument('--headless')

    # Khởi tạo trình duyệt
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    driver.get(f"https://twitter.com/intent/retweet?tweet_id={retweetID}")
    # Đăng nhập bằng auth_token
    auth_token = token

    # Thêm auth_token vào cookies
    driver.add_cookie({'name': 'auth_token', 'value': auth_token})

    # Làm mới trang để áp dụng cookie mới
    driver.refresh()
    # Tìm nút theo dõi với WebDriverWait
    wait = WebDriverWait(driver, 10)

    # -----------------------------------------------------------------------------------------------------------------
    try:
        # Tìm đối tượng <span> với văn bản "Like"
        like_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="Repost" or text()="Đăng lại"]'))
        )

        # Click nút Like
        like_button.click()

        print("Bài viết đã được retweet.")

    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")
    finally:
        # Đóng trình duyệt khi hoàn tất
        time.sleep(4)
        driver.quit()
        print(f"Đóng Twitter trong luồng {threading.current_thread().name}")
    # -----------------------------------------------------------------------------------------------------------------

def login(username):
    global indexUser
    indexUser = indexUser + 1
    print("----------------------------------------------------")
    print(f"indexUser: {indexUser}")
    id = username['id']
    mail = username['mail']
    name = username['name']
    token = username['token']
    chrome_options = ChromeOptions()
    # chrome_options.add_argument(f'user-data-dir=C:\\Users\\moret\\OneDrive\\デスクトップ\\py\\Link\\U2')
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument("--lang=vi")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    driver.set_window_size(1900, 1080)
    # Mở trang Google.com bằng Selenium
    driver.get('https://twitter.com/')
    driver.maximize_window()
    # Ngủ 3 giây (hoặc thời gian cần thiết) để đảm bảo trang web đã mở
    click_button(driver, 'Đăng nhập')
    try:
        # Đường dẫn XPath của trường nhập liệu có thuộc tính name là "text"
        text_input_xpath = "//input[@name='text']"

        # Đợi cho đến khi trường nhập liệu xuất hiện trong vòng 30 giây
        text_input = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, text_input_xpath))
        )

        # Gửi văn bản vào trường nhập liệu
        text_input.send_keys(mail)

    except Exception as e:
        print("Không tìm thấy trường nhập liệu trong khoảng thời gian chờ.")
        # Xử lý trường hợp khi trường nhập liệu không được tìm thấy hoặc không xuất hiện (ví dụ: thử lại hoặc ném một ngoại lệ)

    click_button(driver, 'Tiếp theo')

    try:
        # Đường dẫn XPath của trường nhập liệu có thuộc tính name là "text"
        text_input_xpath = "//input[@name='text']"

        # Đợi cho đến khi trường nhập liệu xuất hiện trong vòng 30 giây
        text_input = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, text_input_xpath))
        )

        # Gửi văn bản vào trường nhập liệu
        text_input.send_keys(name)

    except Exception as e:
        print("Không tìm thấy trường nhập liệu trong khoảng thời gian chờ.")
        # Xử lý trường hợp khi trường nhập liệu không được tìm thấy hoặc không xuất hiện (ví dụ: thử lại hoặc ném một ngoại lệ)

    click_button(driver, 'Tiếp theo')

    fill_input_field(driver, "password", "Congtam@779")



    click_button(driver, 'Đăng nhập')

    try:
        # Đường dẫn XPath của phần tử span
        span_xpath = "//span[contains(text(), 'Kiểm tra email của bạn')]"


        # Kiểm tra xem phần tử span có tồn tại trong vòng 30 giây
        span_element = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, span_xpath))
        )

        # Nếu phần tử tồn tại, đóng trình duyệt
        print("xác nhận code mail")
        driver.quit()
        return
    except Exception as e:
        userStorage.moveToPenddingUser(username)
        print("không cần xác nhận code mail ")

    try:
        # Đợi cho đến khi URL chứa từ khóa "home" trong vòng 10 giây
        WebDriverWait(driver, 10).until(
            EC.url_contains("home")
        )
        # Nếu URL chứa từ khóa "home", thực hiện hành động tương ứng (ví dụ: thoát khỏi trình duyệt)
        print(f"mail thanh cong: {mail}")
        # Thêm hành động tương ứng ở đây
        all_cookies = driver.get_cookies()
        # Tìm giá trị của 'auth_token' trong cookie
        auth_token = None
        for cookie in all_cookies:
            if cookie["name"] == "auth_token":
                auth_token = cookie["value"]
                break

        # In ra giá trị của auth_token
        if auth_token:
            driver.refresh()
            time.sleep(1)
            username['token'] = auth_token
            userStorage.updateUser(username)

        else:
            print("Không tìm thấy auth_token trong cookie.")

        time.sleep(1)
        post.post(driver)
    except Exception as e:
        userStorage.moveToAuthUser(username)
    #     try:
    #         # Đường dẫn XPath của phần tử span với văn bản "Đăng nhập"
    #         login_span_xpath = "//span[contains(@class, 'css-1qaijid') and contains(., 'Đăng nhập')]"
    #
    #         # Đợi cho đến khi phần tử span xuất hiện trong vòng 30 giây
    #         login_span = WebDriverWait(driver, 300).until(
    #             EC.presence_of_element_located((By.XPATH, login_span_xpath))
    #         )
    #
    #         # Thực hiện thao tác click trên phần tử span
    #         login_span.click()
    #
    #     except Exception as e:
    #         print("Không tìm thấy phần tử span trong khoảng thời gian chờ.1111")
    #         # Xử lý trường hợp khi phần tử không được tìm thấy hoặc không xuất hiện (ví dụ: thử lại hoặc ném một ngoại lệ)
    #     # Thực hiện hành động khi URL không phải "https://twitter.com/home"
    #     try:
    #         # Đường dẫn XPath của nút Submit với văn bản "Start"
    #         submit_button_xpath = "//input[@type='submit' and @value='Start']"
    #
    #         # Đợi cho đến khi nút Submit xuất hiện trong vòng 3 giây
    #         submit_button = WebDriverWait(driver, 300).until(
    #             EC.presence_of_element_located((By.XPATH, submit_button_xpath))
    #         )
    #
    #         # Thực hiện thao tác click trên nút Submit
    #         submit_button.click()
    #
    #     except Exception as e:
    #
    #         print("Không tìm thấy nút Submit trong khoảng thời gian chờ.")
    #         # Xử lý trường hợp khi nút Submit không được tìm thấy hoặc không xuất hiện (ví dụ: thử lại hoặc ném một ngoại lệ)
    #
    #     # try:
    #     #     # Đường dẫn XPath của phần tử với văn bản "Phone, email, or username"
    #     #     element_xpath = "//span[contains(text(), 'Phone, email, or username')]"
    #     #
    #     #     # Đợi cho đến khi phần tử xuất hiện trong vòng 30 giây
    #     #     element = WebDriverWait(driver, 30).until(
    #     #         EC.presence_of_element_located((By.XPATH, element_xpath))
    #     #     )
    #     #
    #     #     # Thực hiện các thao tác khác sau khi phần tử xuất hiện (nếu cần)
    #     #
    #     # except Exception as e:
    #     #     print(f"Không tìm thấy phần tử trong khoảng thời gian chờ 30 giây. Lỗi: {e}")
    #     #     # Xử lý trường hợp khi phần tử không được tìm thấy hoặc không xuất hiện (ví dụ: thử lại hoặc ném một ngoại lệ)
    #
    #     # try:
    #     #     # Đường dẫn XPath của phần tử input
    #     #     input_xpath = "//input[@data-testid='ocfEnterTextTextInput']"
    #     #
    #     #     # Đợi cho đến khi phần tử input xuất hiện trong vòng 30 giây
    #     #     input_element = WebDriverWait(driver, 30).until(
    #     #         EC.presence_of_element_located((By.XPATH, input_xpath))
    #     #     )
    #     #
    #     #     # Thực hiện các thao tác khác sau khi phần tử xuất hiện (nếu cần)
    #     #
    #     # except Exception as e:
    #     #     print(f"Không tìm thấy phần tử input trong khoảng thời gian chờ 30 giây. Lỗi: {e}")
    #     #     # Xử lý trường hợp khi phần tử không được tìm thấy hoặc không xuất hiện (ví dụ: thử lại hoặc ném một ngoại lệ)
    #
    #
    #     try:
    #         time.sleep(1)
    #         # Đường dẫn XPath của nút Submit với văn bản "Continue to X"
    #         submit_button_xpath = "//input[@type='submit' and @value='Continue to X']"
    #
    #         # Đợi cho đến khi nút Submit xuất hiện trong vòng 3 giây
    #         submit_button = WebDriverWait(driver, 300).until(
    #             EC.presence_of_element_located((By.XPATH, submit_button_xpath))
    #         )
    #
    #         # Thực hiện thao tác click trên nút Submit
    #         submit_button.click()
    #
    #     except Exception as e:
    #         print("Không tìm thấy nút Submit trong khoảng thời gian chờ.")
    #         # Xử lý trường hợp khi nút Submit không được tìm thấy hoặc không xuất hiện (ví dụ: thử lại hoặc ném một ngoại lệ)
    #
    #         all_cookies = driver.get_cookies()
    #         # Tìm giá trị của 'auth_token' trong cookie
    #
    #     time.sleep(1)
    #
    # finally:
    #     # Đóng trình duyệt (hoặc thực hiện các bước khác nếu cần thiết)
    #     driver.quit()


def click_button(driver, button_text):
    # Đường dẫn XPath của nút tiếp theo với văn bản mong muốn
    next_button_xpath = f"//span[contains(., '{button_text}')]"

    # Đợi cho đến khi nút tiếp theo xuất hiện
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, next_button_xpath)))

    # Tìm nút tiếp theo và thực hiện thao tác click
    next_button = driver.find_element(By.XPATH, next_button_xpath)
    next_button.click()
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

def run_threads(credentials_list, action):
    while credentials_list:
        chunk = credentials_list[:2]
        credentials_list = credentials_list[2:]
        threads = []
        for credentials in chunk:
            thread = threading.Thread(target=perform_action, args=(credentials, action), name=f"Thread-{credentials}")
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()

    print("Tất cả các luồng đã hoàn thành")

def perform_action(credentials, action):
    if action == "1":
        Follow(credentials)
    elif action == "2":
        Like(credentials)
    elif action == "3":
        retweet(credentials)
    elif action == "4":
        login(credentials)
    else:
        print("Hành động không hợp lệ. Đang bỏ qua.")

# Đọc nội dung từ file user.json
user_credentials = userStorage.getAllUser()
# Lấy danh sách người dùng bắt đầu từ vị trí thứ 3
user_credentials_starting_from_third = user_credentials[indexUser:]

# Chạy hàm chứa nhiều luồng để mở trang Twitter với các cặp tên người dùng và mật khẩu khác nhau
# Nhập số 1 để chạy Follow, số 2 để chạy Like, số 3 để chạy Retweet, số 4 để chạy Login
action = input("Nhập hành động (1: Follow, 2: Like, 3: Retweet, 4: Login): ")
run_threads(user_credentials_starting_from_third, action)