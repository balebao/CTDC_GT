def calculate_stock_heartbeat(N, prices):
    # Mảng để lưu kết quả nhịp chứng khoán
    heartbeat = [0] * N
    stack = []

    for i in range(N):
        # Đảm bảo giá chứng khoán trong stack luôn nhỏ hơn hoặc bằng giá chứng khoán của ngày hiện tại
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()
        
        if stack:
            # Nếu stack không rỗng, thì nhịp chứng khoán của ngày hiện tại là i - stack[-1]
            heartbeat[i] = i - stack[-1]
        else:
            # Nếu stack rỗng, thì nhịp chứng khoán của ngày hiện tại là i + 1 (từ ngày đầu tiên)
            heartbeat[i] = i + 1
        
        # Thêm chỉ số của ngày hiện tại vào stack
        stack.append(i)

    return heartbeat

# Nhập dữ liệu từ bàn phím
T = int(input("Nhập số lượng bộ test: "))  # Số lượng bộ test
for _ in range(T):
    N = int(input("số ngày: "))  # Số ngày
    prices = list(map(int, input("gia trứng khoán các ngày: ").split()))  # Giá chứng khoán của các ngày
    result = calculate_stock_heartbeat(N, prices)
    print(*result)
