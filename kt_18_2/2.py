def count_chars(string):
    char_count = {}
    for char in string.replace(" ", ""):  # Loại bỏ khoảng trắng nếu cần
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

# Nhập chuỗi từ bàn phím
string = input("Nhập chuỗi ký tự: ")
print(count_chars(string))
