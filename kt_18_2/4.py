def levenshtein_distance(source, target):
    # Tạo bảng động để lưu trữ các khoảng cách
    m, n = len(source), len(target)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Khởi tạo bảng (dp) với các giá trị ban đầu
    for i in range(m + 1):
        dp[i][0] = i  # Chi phí để biến chuỗi source[0..i] thành chuỗi rỗng
    for j in range(n + 1):
        dp[0][j] = j  # Chi phí để biến chuỗi rỗng thành chuỗi target[0..j]
    
    # Điền vào bảng dp
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if source[i - 1] == target[j - 1]:
                cost = 0  # Không thay đổi khi ký tự giống nhau
            else:
                cost = 1  # Thay thế ký tự nếu khác nhau
            
            dp[i][j] = min(
                dp[i - 1][j] + 1,  # Xoá một ký tự
                dp[i][j - 1] + 1,  # Thêm một ký tự
                dp[i - 1][j - 1] + cost  # Thay thế một ký tự
            )
    
    # Kết quả cuối cùng là dp[m][n], khoảng cách Levenshtein giữa source và target
    return dp[m][n]

# Nhập chuỗi từ bàn phím
source = input("Nhập chuỗi nguồn: ")
target = input("Nhập chuỗi đích: ")

# Tính khoảng cách Levenshtein
distance = levenshtein_distance(source, target)

# In kết quả
print(f"Khoảng cách Levenshtein giữa '{source}' và '{target}' là: {distance}")
