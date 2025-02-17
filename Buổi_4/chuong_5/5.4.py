def remove_parentheses(expression):
    result = []    # Kết quả cuối cùng
    sign = 1        # 1 nếu dấu là +, -1 nếu dấu là -
    stack = []      # Stack để lưu trạng thái dấu trước ngoặc

    for i, char in enumerate(expression):
        if char == '(':
            # Kiểm tra xem dấu trước ngoặc là gì để điều chỉnh
            if i > 0 and expression[i - 1] == '-':
                # Nếu trước ngoặc có dấu - thì đảo ngược dấu trong ngoặc
                stack.append(-sign)
            else:
                stack.append(sign)
        elif char == ')':
            # Kết thúc một ngoặc, pop trạng thái ra
            stack.pop()
        elif char in '+-':
            # Nếu gặp dấu + hoặc -, phải xét dấu hiện tại
            if stack and stack[-1] == -1:
                # Nếu dấu trong stack là -1, đảo ngược dấu
                if char == '+':
                    result.append('-')
                elif char == '-':
                    result.append('+')
            else:
                # Nếu không đảo ngược dấu
                result.append(char)
        else:
            # Thêm các toán hạng (kí tự khác dấu +, -, ( , ) vào kết quả
            result.append(char)
    
    return ''.join(result)

# Input and Output handling
T = int(input("Nhập số lượng bộ test: "))  # Số lượng bộ test

for _ in range(T):
    expression = input("Nhập biểu thức: ").strip()
    print(remove_parentheses(expression))


