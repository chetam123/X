import random

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

# Đọc nội dung từ các file
ho_list = read_file('Name/Ho/Ho.txt')
dem_list = read_file('Name/Dem/Dem.txt')
ten_list = read_file('Name/Ten/Ten.txt')

# Tạo và in kết quả cuối cùng
full_name = generate_full_name(ho_list, dem_list, ten_list)
print(full_name)