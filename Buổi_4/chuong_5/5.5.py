# Hàm chuẩn hóa biểu thức
def normalize(expression):
    stack = []
    for char in expression:
        if char == ')':
            temp = ''
            while stack and stack[-1] != '(':
                temp = stack.pop() + temp
            stack.pop()  # Xóa dấu '('
            for ch in temp:
                stack.append(ch)
        else:
            stack.append(char)
    return ''.join(stack)

# Hàm chính để so sánh hai biểu thức
def compare_expressions(T, tests):
    results = []
    for i in range(T):
        P1, P2 = tests[i]
        # Chuẩn hóa hai biểu thức và so sánh
        if normalize(P1) == normalize(P2):
            results.append("YES")
        else:
            results.append("NO")
    return results

# Phần nhập dữ liệu từ bàn phím
T = int(input("Nhập số lượng bộ test: "))  # Số lượng bộ test
tests = []

for _ in range(T):
    P1 = input("Nhập biểu thức P1: ").strip()  # Biểu thức thứ nhất
    P2 = input("Nhập biểu thức P2: ").strip()  # Biểu thức thứ hai
    tests.append((P1, P2))

# Gọi hàm so sánh
results = compare_expressions(T, tests)

# In kết quả
for result in results:
    print(result)
