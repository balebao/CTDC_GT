# Hàm chuyển đổi biểu thức trung tố thành hậu tố
def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}  # Độ ưu tiên của các toán tử
    output = []
    operators = []
    
    for char in expression:
        if char.isdigit():  # Nếu là số
            output.append(char)
        elif char == '(':  # Nếu là dấu mở ngoặc
            operators.append(char)
        elif char == ')':  # Nếu là dấu đóng ngoặc
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            operators.pop()  # Pop '(' ra
        else:  # Nếu là toán tử
            while (operators and operators[-1] != '(' and
                   precedence[operators[-1]] >= precedence[char]):
                output.append(operators.pop())
            operators.append(char)
    
    # Đẩy tất cả toán tử còn lại vào output
    while operators:
        output.append(operators.pop())
    
    return ''.join(output)

# Hàm tính toán giá trị biểu thức hậu tố
def evaluate_postfix(expression):
    stack = []
    
    for char in expression:
        if char.isdigit():  # Nếu là số
            stack.append(int(char))
        else:  # Nếu là toán tử
            operand2 = stack.pop()
            operand1 = stack.pop()
            if char == '+':
                stack.append(operand1 + operand2)
            elif char == '-':
                stack.append(operand1 - operand2)
            elif char == '*':
                stack.append(operand1 * operand2)
            elif char == '/':
                stack.append(operand1 // operand2)  # Chia lấy phần nguyên
    
    return stack[-1]

# Hàm xử lý nhiều bộ test
def process_tests(T, tests):
    results = []
    for exp in tests:
        # Chuyển biểu thức trung tố sang hậu tố
        postfix_expr = infix_to_postfix(exp)
        # Tính toán giá trị của biểu thức hậu tố
        result = evaluate_postfix(postfix_expr)
        results.append(result)
    return results

# Phần nhập dữ liệu từ bàn phím
T = int(input("Nhập số lượng bộ test: "))  # Số lượng bộ test
tests = []

for _ in range(T):
    exp = input("Nhập biểu thức trung tố: ").strip()  # Biểu thức trung tố
    tests.append(exp)

# Gọi hàm tính toán và in kết quả
results = process_tests(T, tests)
for result in results:
    print(result)
