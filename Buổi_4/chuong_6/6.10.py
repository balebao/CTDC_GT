from collections import deque

# Hàm kiểm tra xem một ô (x, y) có hợp lệ không
def is_valid(x, y, R, C):
    return 0 <= x < R and 0 <= y < C

# Hàm BFS để tìm thời gian ngắn nhất để tất cả các hạt đều nảy mầm
def bfs(R, C, grid):
    # Tạo queue và các mảng hỗ trợ
    queue = deque()
    days = [[-1] * C for _ in range(R)]  # -1 nghĩa là chưa được xử lý
    
    # Thêm tất cả các cây non vào queue và đánh dấu là ngày 0
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 2:  # Cây non
                queue.append((i, j))
                days[i][j] = 0
    
    # Các hướng di chuyển (trái, phải, trên, dưới)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # BFS
    max_days = 0
    while queue:
        x, y = queue.popleft()
        
        # Duyệt các ô xung quanh (trái, phải, trên, dưới)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, R, C) and grid[nx][ny] == 1 and days[nx][ny] == -1:
                # Nếu ô (nx, ny) là hạt chưa nảy mầm và chưa được xử lý
                days[nx][ny] = days[x][y] + 1
                queue.append((nx, ny))
                max_days = max(max_days, days[nx][ny])
    
    # Kiểm tra xem còn hạt nào chưa nảy mầm không
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 1 and days[i][j] == -1:
                return -1  # Có ít nhất một hạt chưa nảy mầm
    
    return max_days

# Phần nhập và xử lý dữ liệu
T = int(input("số bộ test : "))  # Số bộ test
for _ in range(T):
    R, C = map(int, input("Kích thước bảng R x C: ").split())  # Kích thước bảng R x C
    grid = [list(map(int, input().split())) for _ in range(R)]  # Đọc bảng
    print(bfs(R, C, grid))  # In kết quả
