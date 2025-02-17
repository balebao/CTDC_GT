def has_redundant_parentheses(expression):
    stack = []
    
    for char in expression:
        if char == ')':
            if not stack:
                return "Yes"  # Lỗi nếu gặp ')' mà không có '(' tương ứng
            
            top = stack.pop()
            elements_inside = 0  # Đếm số phần tử trong ngoặc
            
            while stack and top != '(':
                elements_inside += 1
                top = stack.pop()
            
            if elements_inside == 0:  # Nếu không có toán tử nào giữa ( và )
                return "Yes"
        else:
            stack.append(char)
    
    return "No"

# Nhập số lượng test cases
t = int(input("Enter number of test cases: ").strip())
for _ in range(t):
    expr = input("Enter expression: ").strip()
    print(has_redundant_parentheses(expr))
