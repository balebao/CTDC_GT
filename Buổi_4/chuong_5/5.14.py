def solve(S):
    stack = []
    result = []
    n = len(S)
    
    # Duyệt qua từng ký tự trong S
    for i in range(n + 1):
        # Thêm số i vào ngăn xếp (số bắt đầu từ 1 đến n+1)
        stack.append(i + 1)
        
        # Nếu gặp 'I' hoặc là cuối chuỗi, giải phóng ngăn xếp
        if i == n or S[i] == 'I':
            while stack:
                result.append(stack.pop())
    
    # Chuyển danh sách result thành số
    return ''.join(map(str, result))

# Phần nhập dữ liệu từ bàn phím
T = int(input("Nhập số lượng bộ test: "))  # Số lượng bộ test
for _ in range(T):
    S = input("Nhập chuỗi S: ").strip()  # Chuỗi S
    print(solve(S))
