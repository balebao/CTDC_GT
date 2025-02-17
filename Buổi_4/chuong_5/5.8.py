# Hàm kiểm tra nếu ký tự là toán hạng
def is_operand(c):
    return c.isalnum()

# Hàm chuyển đổi từ tiền tố sang hậu tố
def prefix_to_postfix(exp):
    stack = []
    # Đọc biểu thức từ phải sang trái
    for char in reversed(exp):
        if is_operand(char):
            stack.append(char)
        else:
            # Khi gặp toán tử, lấy các toán hạng từ ngăn xếp
            operand1 = stack.pop()
            operand2 = stack.pop()
            # Tạo biểu thức hậu tố và đẩy lại vào ngăn xếp
            stack.append(operand1 + operand2 + char)
    return stack[-1]  # Kết quả cuối cùng là biểu thức hậu tố

# Hàm chính giải quyết bài toán
def process_tests(T, tests):
    results = []
    for exp in tests:
        # Chuyển đổi biểu thức tiền tố thành hậu tố
        results.append(prefix_to_postfix(exp))
    return results

# Phần nhập dữ liệu từ bàn phím
T = int(input("Nhập số lượng bộ test: "))  # Số lượng bộ test
tests = []

for _ in range(T):
    exp = input("Nhập biểu thức tiền tố: ").strip()  # Biểu thức tiền tố
    tests.append(exp)

# Gọi hàm chuyển đổi và in kết quả
results = process_tests(T, tests)
for result in results:
    print(result)
