def print_binary_numbers(n):
    for i in range(1, n + 1):
        print(bin(i)[2:], end=" ")  # bin(i) sẽ trả về chuỗi "0b" + biểu diễn nhị phân, ta lấy phần sau "0b"

# Phần nhập dữ liệu từ bàn phím
T = int(input("Nhập số lượng bộ test: "))  # Số lượng bộ test
for _ in range(T):
    n = int(input("Nhập số tự nhiên n cho mỗi test: "))  # Nhập số tự nhiên n cho mỗi test
    print_binary_numbers(n)
    print("Dòng trống sau mỗi test: ")  # Dòng trống sau mỗi test
