from collections import deque

def smallest_number_divisible_by_n(N):
    # BFS sử dụng hàng đợi
    queue = deque()
    # Dùng modulo để tránh quá tải bộ nhớ
    queue.append('9')
    while queue:
        num_str = queue.popleft()
        # Chuyển đổi số chuỗi thành số nguyên để kiểm tra
        num = int(num_str)
        if num % N == 0:
            return num_str
        # Thêm các số tiếp theo bằng cách thêm '0' và '9' vào cuối chuỗi
        queue.append(num_str + '0')
        queue.append(num_str + '9')

# Phần nhập dữ liệu từ bàn phím
T = int(input("Số lượng bộ test: "))  # Số lượng bộ test
for _ in range(T):
    N = int(input("Nhập số N cho mỗi test: "))  # Nhập số N cho mỗi test
    result = smallest_number_divisible_by_n(N)
    print(result)
