def find_longest_valid_parentheses(S):
    stack = [-1]  # Khởi tạo stack với -1 để tính độ dài từ đầu chuỗi
    max_len = 0

    for i in range(len(S)):
        if S[i] == '(':
            stack.append(i)  # Đẩy chỉ số vào stack khi gặp '('
        else:
            stack.pop()  # Pop dấu ngoặc mở ra khi gặp ')'
            if stack:
                max_len = max(max_len, i - stack[-1])  # Tính độ dài dãy ngoặc đúng
            else:
                stack.append(i)  # Nếu stack rỗng, đẩy chỉ số hiện tại vào stack

    return max_len

# Nhập dữ liệu từ bàn phím
T = int(input("Nhập số lượng bộ test: "))  # Số lượng bộ test
for _ in range(T):
    S = input("Nhập chuỗi S: ")  # Xâu S
    print(find_longest_valid_parentheses(S))  # In độ dài dãy ngoặc đúng dài nhất
