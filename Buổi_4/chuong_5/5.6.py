# Hàm kiểm tra ưu tiên của toán tử
def precedence(op):
    if op == '^':
        return 3
    if op == '*' or op == '/':
        return 2
    if op == '+' or op == '-':
        return 1
    return 0

# Hàm chuyển đổi từ trung tố sang hậu tố
def infix_to_postfix(exp):
    stack = []  # Ngăn xếp chứa toán tử
    result = []  # Kết quả cuối cùng (hậu tố)

    for char in exp:
        # Nếu là toán hạng (chữ cái hoặc số), thêm trực tiếp vào kết quả
        if char.isalnum():
            result.append(char)
        # Nếu là dấu ngoặc mở, đẩy vào ngăn xếp
        elif char == '(':
            stack.append(char)
        # Nếu là dấu ngoặc đóng, lấy các toán tử từ ngăn xếp ra cho đến khi gặp dấu ngoặc mở
        elif char == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()  # Bỏ dấu ngoặc mở
        # Nếu là toán tử
        else:
            while stack and precedence(stack[-1]) >= precedence(char):
                result.append(stack.pop())
            stack.append(char)

    # Lấy các toán tử còn lại trong ngăn xếp
    while stack:
        result.append(stack.pop())

    return ''.join(result)

# Hàm chính giải quyết bài toán
def process_tests(T, tests):
    results = []
    for exp in tests:
        # Chuyển đổi biểu thức trung tố thành hậu tố
        results.append(infix_to_postfix(exp))
    return results

# Phần nhập dữ liệu từ bàn phím
T = int(input("Nhập số lượng bộ test: "))  # Số lượng bộ test
tests = []

for _ in range(T):
    exp = input("Nhập biểu thức trung tố: ").strip()  # Biểu thức trung tố
    tests.append(exp)

# Gọi hàm chuyển đổi và in kết quả
results = process_tests(T, tests)
for result in results:
    print(result)
