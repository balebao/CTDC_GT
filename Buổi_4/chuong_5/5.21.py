def max_valid_length(s):
    stack = [-1]  # Ngăn xếp chứa chỉ số của dấu ngoặc mở hoặc chỉ số trước dấu ngoặc hợp lệ
    max_len = 0  # Biến lưu trữ độ dài biểu thức đúng lớn nhất
    
    for i, char in enumerate(s):
        if char == '(':  # Nếu là dấu ngoặc mở, đẩy chỉ số vào ngăn xếp
            stack.append(i)
        else:  # Nếu là dấu ngoặc đóng, tìm dấu ngoặc mở tương ứng
            stack.pop()  # Pop ngoặc mở gần nhất
            if stack:
                # Tính độ dài biểu thức đúng (chỉ số hiện tại trừ đi chỉ số ngoặc mở gần nhất)
                max_len = max(max_len, i - stack[-1])
            else:
                # Nếu không có ngoặc mở tương ứng, đẩy chỉ số hiện tại vào ngăn xếp
                stack.append(i)
    
    return max_len

# Phần nhập dữ liệu từ bàn phím
T = int(input("Nhập số lượng bộ test: "))  # Số lượng bộ test
for _ in range(T):
    P = input("Nhập biểu thức P: ").strip()  # Biểu thức P
    result = max_valid_length(P)
    print("Độ dài biểu thức đúng dài nhất:", result)
