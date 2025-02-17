def decode_string(s):
    stack = []  # Ngăn xếp để lưu trữ các phần tử tạm thời
    num = 0  # Biến để lưu số lặp lại
    result = ""  # Xâu kết quả sau khi giải mã

    for char in s:
        if char.isdigit():  # Nếu là một chữ số, ta xây dựng số lặp lại
            num = num * 10 + int(char)
        elif char == '[':  # Khi gặp '[', đẩy số lặp lại và xâu kết quả tạm vào ngăn xếp
            stack.append((result, num))
            result = ""  # Xóa xâu tạm thời để chứa các ký tự mới
            num = 0  # Reset số lặp lại
        elif char == ']':  # Khi gặp ']', lấy phần tử từ ngăn xếp và giải mã xong
            prev_result, repeat_count = stack.pop()
            result = prev_result + result * repeat_count  # Nhân xâu hiện tại với số lần lặp lại
        else:
            result += char  # Thêm ký tự vào xâu kết quả tạm thời

    return result

# Nhập dữ liệu từ bàn phím
T = int(input("Nhập số lượng bộ test: "))  # Số lượng bộ test
for _ in range(T):
    encoded_str = input("Xâu mã hóa: ").strip()  # Xâu mã hóa
    decoded_str = decode_string(encoded_str)
    print(decoded_str)
