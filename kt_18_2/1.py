from collections import deque

def max_sliding_window(num_list, k):
    if not num_list or k == 0:
        return []
    
    result = []
    dq = deque()
    
    for i in range(len(num_list)):
        # Loại bỏ các phần tử nằm ngoài cửa sổ trượt
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        
        # Loại bỏ các phần tử nhỏ hơn phần tử hiện tại
        while dq and num_list[dq[-1]] < num_list[i]:
            dq.pop()
        
        dq.append(i)
        
        # Lưu kết quả sau khi cửa sổ đạt kích thước k
        if i >= k - 1:
            result.append(num_list[dq[0]])
    
    return result

# Nhập dữ liệu từ người dùng
num_list = list(map(int, input("Nhập danh sách số nguyên, cách nhau bởi dấu cách: ").split()))
k = int(input("Nhập kích thước cửa sổ k: "))

print(max_sliding_window(num_list, k))

