from itertools import product

def generate_lucky_numbers(N):
    lucky_numbers = []
    for length in range(1, N + 1):
        for comb in product([6, 8], repeat=length):
            lucky_numbers.append(int(''.join(map(str, comb))))
    lucky_numbers.sort()  # Sắp xếp theo thứ tự tăng dần
    return lucky_numbers

def solve():
    T = int(input("Đọc số lượng bộ test"))  # Đọc số lượng bộ test
    for _ in range(T):
        N = int(input("Đọc giá trị N cho mỗi test"))  # Đọc giá trị N cho mỗi test
        lucky_numbers = generate_lucky_numbers(N)
        print(len(lucky_numbers))  # In ra số lượng số lộc phát
        print(" ".join(map(str, lucky_numbers)))  # In ra các số lộc phát theo thứ tự tăng dần

# Phần nhập và xử lý dữ liệu
solve()
