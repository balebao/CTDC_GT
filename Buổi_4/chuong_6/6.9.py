from collections import deque

# Hàm kiểm tra xem một ô có hợp lệ không
def is_valid(x, y, N, grid, visited):
    return 0 <= x < N and 0 <= y < N and grid[x][y] != 'X' and not visited[x][y]

# Hàm BFS để tìm số bước di chuyển ít nhất
def bfs(N, grid, start, goal):
    # Tạo queue và mảng visited
    queue = deque([(start[0], start[1], 0)])  # (x, y, bước di chuyển)
    visited = [[False] * N for _ in range(N)]
    visited[start[0]][start[1]] = True

    while queue:
        x, y, dist = queue.popleft()

        # Nếu đã tới đích, trả về số bước
        if (x, y) == goal:
            return dist

        # Duyệt tất cả các ô có thể di chuyển đến từ (x, y)
        # Di chuyển theo hàng
        for i in range(x + 1, N):  # Duyệt xuống dưới
            if is_valid(i, y, N, grid, visited):
                visited[i][y] = True
                queue.append((i, y, dist + 1))
            else:
                break  # Dừng nếu có vật cản

        for i in range(x - 1, -1, -1):  # Duyệt lên trên
            if is_valid(i, y, N, grid, visited):
                visited[i][y] = True
                queue.append((i, y, dist + 1))
            else:
                break

        # Di chuyển theo cột
        for j in range(y + 1, N):  # Duyệt sang phải
            if is_valid(x, j, N, grid, visited):
                visited[x][j] = True
                queue.append((x, j, dist + 1))
            else:
                break  # Dừng nếu có vật cản

        for j in range(y - 1, -1, -1):  # Duyệt sang trái
            if is_valid(x, j, N, grid, visited):
                visited[x][j] = True
                queue.append((x, j, dist + 1))
            else:
                break

    return -1  # Không tìm được đường đi

# Phần nhập và xử lý dữ liệu
T = int(input("số bộ test : "))  # Số bộ test
for _ in range(T):
    N = int(input("Kích thước bảng N x N: "))  # Kích thước bảng N x N
    grid = [input().strip() for _ in range(N)]  # Đọc bảng
    a, b, c, d = map(int, input("Tọa độ điểm xuất phát và đích; ").split())  # Tọa độ điểm xuất phát và đích

    # Gọi hàm BFS để tính số bước di chuyển ít nhất
    result = bfs(N, grid, (a, b), (c, d))
    print(result)
