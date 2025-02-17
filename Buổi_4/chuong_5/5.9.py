# Hàm kiểm tra nếu ký tự là toán hạng
def is_operand(c):
    return c.isalnum()

# Hàm chuyển đổi từ hậu tố sang tiền tố
def postfix_to_prefix(exp):
    stack = []
    # Đọc biểu thức từ trái sang phải
    for char in exp:
        if is_operand(char):
            stack.append(char)
        else:
            # Khi gặp toán tử, lấy hai toán hạng từ ngăn xếp
            operand2 = stack.pop()
            operand1 = stack.pop()
            # Tạo biểu thức tiền tố và đẩy lại vào ngăn xếp
            stack.append(char + operand1 + operand2)
    return stack[-1]  # Kết quả cuối cùng là biểu thức tiền tố

# Hàm chính giải quyết bài toán
def process_tests(T, tests):
    results = []
    for exp in tests:
        # Chuyển đổi biểu thức hậu tố thành tiền tố
        results.append(postfix_to_prefix(exp))
    return results

# Phần nhập dữ liệu từ bàn phím
T = int(input("Nhập số lượng bộ test: "))  # Số lượng bộ test
tests = []

for _ in range(T):
    exp = input("Nhập biểu thức hậu tố: ").strip()  # Biểu thức hậu tố
    tests.append(exp)

# Gọi hàm chuyển đổi và in kết quả
results = process_tests(T, tests)
for result in results:
    print(result)
