# Hàm thực hiện tính toán giá trị biểu thức tiền tố
def evaluate_prefix(exp):
    stack = []
    
    # Duyệt biểu thức từ phải sang trái
    for char in reversed(exp):
        if char.isdigit():  # Khi gặp số
            stack.append(int(char))  # Đẩy số vào ngăn xếp
        else:  # Khi gặp toán tử
            operand1 = stack.pop()  # Lấy toán hạng thứ 1
            operand2 = stack.pop()  # Lấy toán hạng thứ 2
            
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
        # Tính toán giá trị của biểu thức tiền tố
        results.append(evaluate_prefix(exp))
    return results

# Phần nhập dữ liệu từ bàn phím
T = int(input("Nhập số lượng bộ test: "))  # Số lượng bộ test
tests = []

for _ in range(T):
    exp = input("Nhập biểu thức tiền tố: ").strip()  # Biểu thức tiền tố
    tests.append(exp)

# Gọi hàm tính toán và in kết quả
results = process_tests(T, tests)
for result in results:
    print(result)
