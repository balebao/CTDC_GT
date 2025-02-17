# Hàm thực hiện tính toán giá trị biểu thức hậu tố
def evaluate_postfix(exp):
    stack = []
    
    # Duyệt biểu thức từ trái sang phải
    for char in exp:
        if char.isdigit():  # Khi gặp số
            stack.append(int(char))  # Đẩy số vào ngăn xếp
        else:  # Khi gặp toán tử
            operand2 = stack.pop()  # Lấy toán hạng thứ 2
            operand1 = stack.pop()  # Lấy toán hạng thứ 1
            
            # Thực hiện phép toán và đẩy kết quả vào ngăn xếp
            if char == '+':
                stack.append(operand1 + operand2)
            elif char == '-':
                stack.append(operand1 - operand2)
            elif char == '*':
                stack.append(operand1 * operand2)
            elif char == '/':
                stack.append(operand1 // operand2)  # Chia nguyên
                
    return stack[-1]  # Kết quả cuối cùng là phần tử duy nhất trong ngăn xếp

# Hàm chính giải quyết bài toán
def process_tests(T, tests):
    results = []
    for exp in tests:
        # Tính toán giá trị của biểu thức hậu tố
        results.append(evaluate_postfix(exp))
    return results

# Phần nhập dữ liệu từ bàn phím
T = int(input("Nhập số lượng bộ test: "))  # Số lượng bộ test
tests = []

for _ in range(T):
    exp = input("Nhập biểu thức hậu tố: ").strip()  # Biểu thức hậu tố
    tests.append(exp)

# Gọi hàm tính toán và in kết quả
results = process_tests(T, tests)
for result in results:
    print(result)
