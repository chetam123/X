
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import datetime
global indexUser

import random
def post(driver):

    morning_greetings = [
        "Chào buổi sáng! Bạn đã ngủ ngon chưa?",
        "Buổi sáng an lành! Bạn đã sẵn sàng cho một ngày mới chưa?",
        "Chúc bạn một buổi sáng tràn đầy năng lượng!",
        "Buổi sáng tốt lành nhất! Bạn đã thức dậy với tâm trạng tốt chưa?",
        "Chào buổi sáng mới! Bạn đã có kế hoạch gì cho hôm nay chưa?",
        "Buổi sáng tươi mới! Bạn đã thư giãn đủ chưa?",
        "Chúc bạn có một buổi sáng đẹp như mơ!",
        "Buổi sáng an nhiên! Bạn đã cảm nhận được không khí mới của ngày mới chưa?",
        "Chào buổi sáng! Bạn đã chuẩn bị tinh thần cho mọi thách thức chưa?",
        "Buổi sáng tỉnh táo! Bạn đã thức dậy với năng lượng đầy đủ chưa?",
        "Chào ngày mới! Bạn đã uống một cốc nước ấm chưa?",
        "Buổi sáng hạnh phúc! Bạn đã cảm nhận được niềm vui từ ánh nắng mặt trời chưa?",
        "Chào buổi sáng an lành! Bạn đã đánh răng rồi chưa?",
        "Buổi sáng yên bình! Bạn đã dành thời gian cho bản thân chưa?",
        "Chúc bạn có một buổi sáng tràn đầy sự tích cực!",
        "Buổi sáng tốt lành nhất! Bạn đã đặt mục tiêu cho hôm nay chưa?",
        "Chào buổi sáng! Bạn đã thức dậy với tâm hồn bình yên chưa?",
        "Buổi sáng mới! Bạn đã tận hưởng hương vị của cà phê chưa?",
        "Chúc bạn có một ngày mới đầy năng lượng và thành công!",
        "Buổi sáng an lành nhất! Bạn đã lên kế hoạch cho một ngày tuyệt vời chưa?",
        "Chào buổi sáng! Bạn đã tập thể dục sáng chưa?",
        "Buổi sáng tươi mới! Bạn đã cảm ơn cho những điều tích cực trong cuộc sống chưa?",
        "Chào buổi sáng mới! Bạn đã đọc một đoạn sách tích cực chưa?",
        "Buổi sáng hạnh phúc! Bạn đã dành thời gian để cười chưa?",
        "Chúc bạn có một ngày mới đầy ý nghĩa và hạnh phúc!",
        "Buổi sáng an lành! Bạn đã lắng nghe âm nhạc nhẹ nhàng chưa?",
        "Chào buổi sáng! Bạn đã tận hưởng hơi thở của một buổi sáng trong lành chưa?",
        "Buổi sáng tốt lành nhất! Bạn đã gửi một tin nhắn tích cực cho người thân chưa?",
        "Chào ngày mới! Bạn đã dành vài phút để thiền định chưa?",
        "Buổi sáng tỉnh táo! Bạn đã dự định một hoạt động tích cực cho ngày hôm nay chưa?",
        "Chào buổi sáng an nhiên! Bạn đã đặt một mục tiêu nhỏ để đạt được hôm nay chưa?",
        "Buổi sáng hạnh phúc! Bạn đã nói lời cảm ơn cho cuộc sống chưa?",
        "Chúc bạn có một buổi sáng tràn đầy niềm vui và tươi mới!",
        "Buổi sáng tốt lành nhất! Bạn đã thưởng thức hương thơm của hoa chưa?",
        "Chào buổi sáng! Bạn đã dành thời gian để đọc một bài viết tích cực chưa?",
        "Buổi sáng mới! Bạn đã nói xin chào với người xung quanh chưa?",
        "Chúc bạn có một ngày mới tràn đầy sự sáng tạo và đổi mới!",
        "Buổi sáng an lành nhất! Bạn đã thiết lập tâm lý tích cực cho ngày hôm nay chưa?",
        "Chào buổi sáng! Bạn đã dành vài phút để viết ra một số điều bạn cảm ơn chưa?",
        "Buổi sáng tươi mới! Bạn đã dự định một kế hoạch cho thành công hôm nay chưa?",
        "Chào buổi sáng mới! Bạn đã thức dậy với năng lượng tích cực chưa?",
        "Buổi sáng tỉnh táo! Bạn đã làm một điều tích cực ngay từ bước chân đầu tiên chưa?",
        "Chúc bạn có một buổi sáng an lành và đáng nhớ!",
        "Buổi sáng tốt lành nhất! Bạn đã đặt một mục tiêu lớn cho tuần này chưa?",
        "Chào ngày mới! Bạn đã nhìn thấy bình minh chưa?",
        "Buổi sáng hạnh phúc! Bạn đã dành thời gian để thư giãn và đắm chìm trong sự yên bình chưa?",
        "Chào buổi sáng an nhiên! Bạn đã dùng điện thoại di động chưa?",
        "Buổi sáng an lành nhất! Bạn đã chuẩn bị một bữa sáng lành mạnh chưa?",
        "Chúc bạn có một ngày mới đầy năng lượng và đam mê!",
        "Buổi sáng tốt lành nhất! Bạn đã tận hưởng giọt sương buổi sáng chưa?",
        "Chào buổi sáng! Bạn đã dành thời gian để tự thưởng cho bản thân chưa?",
        "Buổi sáng tươi mới! Bạn đã nhận ra những điều tích cực xung quanh mình chưa?",
        "Chúc bạn có một buổi sáng tràn đầy năng lượng và khởi đầu mới!",
    ]

    noon_greetings = [
        "Chào buổi trưa! Bạn đã có bữa trưa ngon chưa?",
        "Buổi trưa an lành! Bạn đang cảm thấy như thế nào sau giờ làm việc đầu tiên?",
        "Chúc bạn một buổi trưa tràn đầy năng lượng và sự sáng tạo!",
        "Buổi trưa tốt lành nhất! Bạn đã thưởng thức một bữa trưa ngon chưa?",
        "Chào buổi trưa mới! Bạn đã nghỉ ngơi đủ chưa?",
        "Buổi trưa tươi mới! Bạn đã thư giãn chút chưa?",
        "Chúc bạn có một buổi trưa đầy ý nghĩa và thoải mái!",
        "Buổi trưa an nhiên! Bạn đã dành thời gian cho bản thân chưa?",
        "Chào buổi trưa! Bạn đã thư giãn vài phút chưa?",
        "Buổi trưa hạnh phúc! Bạn đã chia sẻ một bữa trưa với người thân hay đồng nghiệp chưa?",
        "Chào buổi trưa mới! Bạn đã thưởng thức đủ nước chưa?",
        "Buổi trưa tỉnh táo! Bạn đã dành thời gian nghỉ ngơi chưa?",
        "Chúc bạn có một buổi trưa đầy năng lượng và sự sáng tạo!",
        "Buổi trưa tốt lành nhất! Bạn đã thư giãn vài phút chưa?",
        "Chào buổi trưa! Bạn đã thưởng thức một bữa trưa lành mạnh chưa?",
        "Buổi trưa tươi mới! Bạn đã nghỉ ngơi đủ chưa?",
        "Chúc bạn có một buổi trưa an lành và thư giãn!",
        "Buổi trưa an nhiên! Bạn đã dành thời gian cho bản thân chưa?",
        "Chào buổi trưa mới! Bạn đã nghỉ ngơi vài phút chưa?",
        "Buổi trưa hạnh phúc! Bạn đã chia sẻ niềm vui với người khác chưa?",
        "Chào buổi trưa! Bạn đã thưởng thức một bữa trưa ngon lành chưa?",
        "Buổi trưa tốt lành nhất! Bạn đã dành thời gian cho sức khỏe của mình chưa?",
        "Chúc bạn có một buổi trưa tràn đầy năng lượng và sự hứng khởi!",
        "Buổi trưa tươi mới! Bạn đã thưởng thức đủ nước và thức ăn dinh dưỡng chưa?",
        "Chào buổi trưa! Bạn đã thư giãn vài phút để làm mới tinh thần chưa?",
        "Buổi trưa an nhiên! Bạn đã tận hưởng thời gian bình yên chưa?",
        "Chúc bạn có một buổi trưa vui vẻ và thoải mái!",
        "Buổi trưa tốt lành nhất! Bạn đã nghỉ ngơi đủ để đối mặt với phần còn lại của ngày chưa?",
        "Chào buổi trưa mới! Bạn đã có kế hoạch gì cho phần còn lại của ngày chưa?",
        "Buổi trưa tươi mới! Bạn đã dành thời gian nghỉ ngơi và làm mới năng lượng chưa?",
    ]

    evening_greetings = [
        "Chào buổi tối! Bạn đã có một ngày tuyệt vời chưa?",
        "Buổi tối an lành! Bạn đang thư giãn thế nào?",
        "Chúc bạn có một buổi tối tràn đầy hạnh phúc và thư giãn!",
        "Buổi tối tốt lành nhất! Bạn đã thưởng thức bữa tối chưa?",
        "Chào buổi tối mới! Bạn đã dành thời gian cho sở thích của mình chưa?",
        "Buổi tối tươi mới! Bạn đang tận hưởng khoảnh khắc yên bình chưa?",
        "Chúc bạn có một buổi tối an nhiên và đáng nhớ!",
        "Buổi tối an nhiên! Bạn đã dành thời gian với gia đình chưa?",
        "Chào buổi tối! Bạn đã thư giãn vài phút chưa?",
        "Buổi tối hạnh phúc! Bạn đã chia sẻ niềm vui với người thân chưa?",
        "Chào buổi tối mới! Bạn đã tận hưởng cảm giác yên bình chưa?",
        "Buổi tối tỉnh táo! Bạn đã dành thời gian cho sức khỏe của mình chưa?",
        "Chúc bạn có một buổi tối đầy năng lượng và sự sáng tạo!",
        "Buổi tối tốt lành nhất! Bạn đã thư giãn vài phút chưa?",
        "Chào buổi tối! Bạn đã dành thời gian với người bạn thân chưa?",
        "Buổi tối tươi mới! Bạn đã thưởng thức cảm giác của không khí buổi tối chưa?",
        "Chúc bạn có một buổi tối an lành và tràn đầy hạnh phúc!",
        "Buổi tối an nhiên! Bạn đã dành thời gian cho bản thân chưa?",
        "Chào buổi tối mới! Bạn đã nghỉ ngơi vài phút chưa?",
        "Buổi tối hạnh phúc! Bạn đã chia sẻ niềm vui với người thân chưa?",
        "Chào buổi tối! Bạn đã thư giãn vài phút chưa?",
        "Buổi tối tốt lành nhất! Bạn đã thưởng thức bữa tối chưa?",
        "Chào buổi tối mới! Bạn đã dành thời gian cho sở thích của mình chưa?",
        "Buổi tối tươi mới! Bạn đang tận hưởng khoảnh khắc yên bình chưa?",
        "Chúc bạn có một buổi tối an nhiên và đáng nhớ!",
        "Buổi tối an nhiên! Bạn đã dành thời gian với gia đình chưa?",
        "Chào buổi tối! Bạn đã thư giãn vài phút chưa?",
        "Buổi tối hạnh phúc! Bạn đã chia sẻ niềm vui với người thân chưa?",
        "Chào buổi tối mới! Bạn đã tận hưởng cảm giác của không khí buổi tối chưa?",
        "Chúc bạn có một buổi tối an lành và tràn đầy hạnh phúc!",
    ]
    # --------------------------------------------------------
    morning_icons = [
        "☀️", "🌅", "🌞", "🌤️", "🌼", "🌷", "🌻", "🌅", "🍀", "🌈",
        "🍵", "🌞", "🌅", "🌺", "🌸", "🌅", "🌞", "🌿", "🌄", "🌞",
        "🍃", "🌞", "🌄", "🌺", "🌅", "🌞", "🌼", "🌷", "🌈", "🌄",
    ]

    noon_icons = [
        "🍲", "🍛", "🥗", "🍜", "🍝", "🥙", "🍱", "🍚", "🥪", "🥘",
        "🍔", "🍕", "🥗", "🍲", "🍝", "🍚", "🌮", "🍜", "🍛", "🍱",
        "🍣", "🍙", "🌭", "🍚", "🥘", "🍜", "🍲", "🍱", "🍛", "🌮",
    ]

    evening_icons = [
        "🌙", "🌠", "🌆", "🌌", "🌃", "🌇", "🌠", "🌙", "🌌", "🌆",
        "🌃", "🌇", "🌌", "🌆", "🌙", "🌃", "🌠", "🌇", "🌌", "🌆",
        "🌃", "🌙", "🌌", "🌆", "🌇", "🌠", "🌃", "🌙", "🌌", "🌆",
    ]
    # --------------------------------------------------------
    morning_greetings_icons = [
        "꧁༺🌞 H͙e͙l͙l͙o͙ 🌞༻꧂",
        "(🌅🌼 G͙o͙o͙d͙ m͙o͙r͙n͙i͙n͙g͙) 🌼🌅",
        "✧*。🍀 M͙o͙r͙n͙i͙n͙g͙ 🍀｡*✧",
        "꧁༺🌞 H͙a͙v͙e͙ a͙ b͙e͙a͙u͙t͙i͙f͙u͙l͙ d͙a͙y͙ 🌞༻꧂",
        "☆*:.｡.o(🌅 G͙o͙o͙d͙ )o.｡.:*☆",
        "꧁༺☀️ H͙i͙ t͙h͙e͙r͙e͙ ☀️༻꧂",
        "(🌞🌷 M͙o͙r͙n͙i͙n͙g͙) 🌷🌞",
        "✧*。🍃 G͙o͙o͙d͙ m͙o͙r͙n͙i͙n͙g͙ 🍃｡*✧",
        "꧁༺🌞 H͙i͙ e͙v͙e͙r͙y͙o͙n͙e͙ 🌞༻꧂",
        "(🍀🌼 G͙o͙o͙d͙ ) m͙o͙r͙n͙i͙n͙g͙ 🌼🍀",
        "✧*。🌄 H͙e͙l͙l͙o͙ 🌄｡*✧",
        "꧁༺🌞 G͙o͙o͙d͙ m͙o͙r͙n͙i͙n͙g͙ 🌞༻꧂",
        "☆*:.｡.o(🌇 H͙a͙v͙e͙ a͙ n͙i͙c͙e͙ )o.｡.:*☆",
        "꧁༺☀️ H͙i͙ t͙h͙e͙r͙e͙ ☀️༻꧂",
        "(🌞🌸 M͙o͙r͙n͙i͙n͙g͙) 🌸🌞",
        "✧*。🌅 G͙o͙o͙d͙ m͙o͙r͙n͙i͙n͙g͙ 🌅｡*✧",
        "꧁༺🌞 H͙i͙ e͙v͙e͙r͙y͙o͙n͙e͙ 🌞༻꧂",
        "(🍀🌼 G͙o͙o͙d͙ ) m͙o͙r͙n͙i͙n͙g͙ 🌼🍀",
        "✧*。🌄 H͙e͙l͙l͙o͙ 🌄｡*✧",
        "꧁༺🌞 G͙o͙o͙d͙ m͙o͙r͙n͙i͙n͙g͙ 🌞༻꧂",
        "☆*:.｡.o(🌇 H͙a͙v͙e͙ a͙ n͙i͙c͙e͙ )o.｡.:*☆",
        "꧁༺☀️ H͙i͙ t͙h͙e͙r͙e͙ ☀️༻꧂",
        "(🌞🌸 M͙o͙r͙n͙i͙n͙g͙) 🌸🌞",
        "✧*。🌅 G͙o͙o͙d͙ m͙o͙r͙n͙i͙n͙g͙ 🌅｡*✧",
        "꧁༺🌞 H͙i͙ e͙v͙e͙r͙y͙o͙n͙e͙ 🌞༻꧂",
        "(🍀🌼 G͙o͙o͙d͙ ) m͙o͙r͙n͙i͙n͙g͙ 🌼🍀",
        "✧*。🌄 H͙e͙l͙l͙o͙ 🌄｡*✧",
    ]

    noon_greetings_icons = [
        "꧁༺🍲 H͙a͙v͙e͙ a͙ d͙e͙l͙i͙c͙i͙o͙u͙s͙ l͙u͙n͙c͙h͙ 🍲༻꧂",
        "(🥗🍜 G͙o͙o͙d͙ n͙o͙o͙n͙) 🍜🥗",
        "✧*。🍱 E͙n͙j͙o͙y͙ y͙o͙u͙r͙ l͙u͙n͙c͙h͙ 🍱｡*✧",
        "꧁༺🍲 H͙o͙p͙e͙ y͙o͙u͙r͙ l͙u͙n͙c͙h͙ i͙s͙ t͙a͙s͙t͙y͙ 🍲༻꧂",
        "☆*:.｡.o(🥙 G͙o͙o͙d͙ )o.｡.:*☆",
        "꧁༺🍣 H͙a͙v͙e͙ a͙ g͙r͙e͙a͙t͙ l͙u͙n͙c͙h͙ 🍣༻꧂",
        "(🍜🍚 N͙o͙o͙n͙ ) d͙e͙l͙i͙g͙h͙t͙s͙ 🍚🍜",
        "✧*。🍛 E͙n͙j͙o͙y͙ y͙o͙u͙r͙ l͙u͙n͙c͙h͙ 🍛｡*✧",
        "꧁༺🥗 H͙a͙v͙e͙ a͙ d͙e͙l͙i͙c͙i͙o͙u͙s͙ n͙o͙o͙n͙ 🥗༻꧂",
        "☆*:.｡.o(🍱 G͙o͙o͙d͙ )o.｡.:*☆",
        "꧁༺🍣 H͙a͙v͙e͙ a͙ g͙r͙e͙a͙t͙ n͙o͙o͙n͙ 🍣༻꧂",
        "(🍜🍚 N͙o͙o͙n͙ ) d͙e͙l͙i͙g͙h͙t͙s͙ 🍚🍜",
        "✧*。🍛 E͙n͙j͙o͙y͙ y͙o͙u͙r͙ l͙u͙n͙c͙h͙ 🍛｡*✧",
        "꧁༺🍲 H͙a͙v͙e͙ a͙ d͙e͙l͙i͙c͙i͙o͙u͙s͙ n͙o͙o͙n͙ 🍲༻꧂",
        "☆*:.｡.o(🥙 G͙o͙o͙d͙ )o.｡.:*☆",
        "꧁༺🍣 H͙a͙v͙e͙ a͙ g͙r͙e͙a͙t͙ n͙o͙o͙n͙ 🍣༻꧂",
        "(🍜🍚 N͙o͙o͙n͙ ) d͙e͙l͙i͙g͙h͙t͙s͙ 🍚🍜",
        "✧*。🍛 E͙n͙j͙o͙y͙ y͙o͙u͙r͙ l͙u͙n͙c͙h͙ 🍛｡*✧",
        "꧁༺🥗 H͙a͙v͙e͙ a͙ d͙e͙l͙i͙c͙i͙o͙u͙s͙ n͙o͙o͙n͙ 🥗༻꧂",
        "☆*:.｡.o(🍱 G͙o͙o͙d͙ )o.｡.:*☆",
        "꧁༺🍣 H͙a͙v͙e͙ a͙ g͙r͙e͙a͙t͙ n͙o͙o͙n͙ 🍣༻꧂",
        "(🍜🍚 N͙o͙o͙n͙ ) d͙e͙l͙i͙g͙h͙t͙s͙ 🍚🍜",
        "✧*。🍛 E͙n͙j͙o͙y͙ y͙o͙u͙r͙ l͙u͙n͙c͙h͙ 🍛｡*✧",
        "꧁༺🍲 H͙a͙v͙e͙ a͙ d͙e͙l͙i͙c͙i͙o͙u͙s͙ n͙o͙o͙n͙ 🍲༻꧂",
        "☆*:.｡.o(🥙 G͙o͙o͙d͙ )o.｡.:*☆",
        "꧁༺🍣 H͙a͙v͙e͙ a͙ g͙r͙e͙a͙t͙ n͙o͙o͙n͙ 🍣༻꧂",
        "(🍜🍚 N͙o͙o͙n͙ ) d͙e͙l͙i͙g͙h͙t͙s͙ 🍚🍜",
        "✧*。🍛 E͙n͙j͙o͙y͙ y͙o͙u͙r͙ l͙u͙n͙c͙h͙ 🍛｡*✧",
    ]

    evening_greetings_icons = [
        "꧁༺🌙 G͙o͙o͙d͙ e͙v͙e͙n͙i͙n͙g͙ 🌙༻꧂",
        "(🌠🌆 E͙v͙e͙n͙i͙n͙g͙ ) d͙e͙l͙i͙g͙h͙t͙s͙ 🌆🌠",
        "✧*。🌌 H͙a͙v͙e͙ a͙ p͙e͙a͙c͙e͙f͙u͙l͙ e͙v͙e͙n͙i͙n͙g͙ 🌌｡*✧",
        "꧁༺🌃 G͙o͙o͙d͙ n͙i͙g͙h͙t͙ 🌃༻꧂",
        "☆*:.｡.o(🌌 E͙v͙e͙n͙i͙n͙g͙ )o.｡.:*☆",
        "꧁༺🌙 H͙a͙v͙e͙ a͙ r͙e͙s͙t͙f͙u͙l͙ e͙v͙e͙n͙i͙n͙g͙ 🌙༻꧂",
        "(🌆🌠 E͙v͙e͙n͙i͙n͙g͙ ) t͙r͙a͙n͙q͙u͙i͙l͙i͙t͙y͙ 🌠🌆",
        "✧*。🌄 G͙o͙o͙d͙ e͙v͙e͙n͙i͙n͙g͙ 🌄｡*✧",
        "꧁༺🌙 H͙a͙v͙e͙ a͙ r͙e͙l͙a͙x͙i͙n͙g͙ e͙v͙e͙n͙i͙n͙g͙ 🌙༻꧂",
        "☆*:.｡.o(🌃 E͙v͙e͙n͙i͙n͙g͙ )o.｡.:*☆",
        "꧁༺🌌 H͙a͙v͙e͙ a͙ c͙a͙l͙m͙ e͙v͙e͙n͙i͙n͙g͙ 🌌༻꧂",
        "(🌄🌠 E͙v͙e͙n͙i͙n͙g͙ ) s͙e͙r͙e͙n͙i͙t͙y͙ 🌠🌄",
        "✧*。🌙 G͙o͙o͙d͙ e͙v͙e͙n͙i͙n͙g͙ 🌙｡*✧",
        "꧁༺🌃 H͙a͙v͙e͙ a͙ p͙e͙a͙c͙e͙f͙u͙l͙ e͙v͙e͙n͙i͙n͙g͙ 🌃༻꧂",
        "☆*:.｡.o(🌌 E͙v͙e͙n͙i͙n͙g͙ )o.｡.:*☆",
        "꧁༺🌄 H͙a͙v͙e͙ a͙ r͙e͙l͙a͙x͙i͙n͙g͙ e͙v͙e͙n͙i͙n͙g͙ 🌄༻꧂",
        "(🌆🌠 E͙v͙e͙n͙i͙n͙g͙ ) s͙e͙r͙e͙n͙i͙t͙y͙ 🌠🌆",
        "✧*。🌙 G͙o͙o͙d͙ e͙v͙e͙n͙i͙n͙g͙ 🌙｡*✧",
        "꧁༺🌃 H͙a͙v͙e͙ a͙ c͙a͙l͙m͙ e͙v͙e͙n͙i͙n͙g͙ 🌃༻꧂",
        "☆*:.｡.o(🌌 E͙v͙e͙n͙i͙n͙g͙ )o.｡.:*☆",
        "꧁༺🌄 H͙a͙v͙e͙ a͙ r͙e͙l͙a͙x͙i͙n͙g͙ e͙v͙e͙n͙i͙n͙g͙ 🌄༻꧂",
        "(🌆🌠 E͙v͙e͙n͙i͙n͙g͙ ) s͙e͙r͙e͙n͙i͙t͙y͙ 🌠🌆",
        "✧*。🌙 G͙o͙o͙d͙ e͙v͙e͙n͙i͙n͙g͙ 🌙｡*✧",
        "꧁༺🌃 H͙a͙v͙e͙ a͙ c͙a͙l͙m͙ e͙v͙e͙n͙i͙n͙g͙ 🌃༻꧂",
        "☆*:.｡.o(🌌 E͙v͙e͙n͙i͙n͙g͙ )o.｡.:*☆",
        "꧁༺🌄 H͙a͙v͙e͙ a͙ r͙e͙l͙a͙x͙i͙n͙g͙ e͙v͙e͙n͙i͙n͙g͙ 🌄༻꧂",
    ]
    # --------------------------------------------------------
    # Chọn ngẫu nhiên một phần từ morning_greetings_icons
    now = datetime.datetime.now()
    current_hour = now.hour
    your_tweet_content = random.choice(noon_greetings_icons) + "\n" + random.choice(
        noon_icons) + random.choice(noon_greetings) + random.choice(noon_icons)

    if 5 <= current_hour < 12:
        your_tweet_content  = random.choice(morning_greetings_icons) + "\n" +  random.choice(morning_icons)  +  random.choice(morning_greetings) +random.choice(morning_icons)

    elif 12 <= current_hour < 18:
        your_tweet_content  = random.choice(noon_greetings_icons) + "\n" + random.choice(
            noon_icons) + random.choice(noon_greetings) + random.choice(noon_icons)

    elif 18 <= current_hour < 24:
        your_tweet_content = random.choice(evening_greetings_icons) + "\n" + random.choice(
            evening_icons) + random.choice(evening_greetings) + random.choice(evening_icons)

    tweet_url = f"https://twitter.com/intent/tweet?text={your_tweet_content}"

    driver.get(tweet_url)
    time.sleep(2)
    try:
        # Xác định XPath của thẻ span có văn bản là "Post"
        post_button_xpath = "//span[contains(text(), 'Post')]"

        # Sử dụng WebDriverWait để đợi cho đến khi thẻ span xuất hiện trong vòng 30 giây
        post_button = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, post_button_xpath))
        )

        post_button.click()
        print("thanh cong")
    except Exception as e:
        print("post ko thanh cong")
        # Xử lý trường hợp khi nút Submit không được tìm thấy hoặc không xuất hiện (ví dụ: thử lại hoặc ném một ngoại lệ)
    return