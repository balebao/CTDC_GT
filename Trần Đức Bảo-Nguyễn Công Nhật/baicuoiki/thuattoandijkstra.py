import pygame
import sys
import numpy as np
from collections import deque
import time
import heapq  
# Khai báo các màu dùng trong hiển thị
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
PURPLE = (160, 32, 240)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
INFO_COLOR = (255, 165, 0)

# Kích thước mỗi ô và số hàng/cột trong lưới
CELL_SIZE = 20
ROWS = 30
COLS = 40

# Thuật toán dijkstra trả về đường đi ngắn nhất và các ô đã duyệt

def dijkstra(grid, start, goal):
    rows, cols = grid.shape
    visited = np.full((rows, cols), False)
    dist = np.full((rows, cols), np.inf)
    prev = np.full((rows, cols), None)

    dist[start] = 0
    pq = [(0, start)]
    visited_order = []

    while pq:
        current_dist, current = heapq.heappop(pq)
        if visited[current]:
            continue
        visited[current] = True
        visited_order.append(current)

        if current == goal:
            break

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = current[0] + dx, current[1] + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx, ny] != 1:
                new_dist = current_dist + 1
                if new_dist < dist[nx, ny]:
                    dist[nx, ny] = new_dist
                    prev[nx, ny] = current
                    heapq.heappush(pq, (new_dist, (nx, ny)))

    path = []
    at = goal
    while at is not None:
        path.append(at)
        at = prev[at]
    path.reverse()

    if path[0] == start:
        return path, visited_order
    else:
        return None, visited_order


# Lớp xử lý giao diện và logic trực quan hóa
class PathfindingVisualizer:
    def __init__(self, screen, rows, cols):
        self.screen = screen
        self.rows = rows
        self.cols = cols
        self.grid = np.zeros((rows, cols), dtype=int)  # Lưới: 0 là trống, 1 là chướng ngại
        self.start = (0, 0)     # Điểm bắt đầu (mặc định)
        self.goal = (rows-1, cols-1)  # Điểm kết thúc
        self.path = None
        self.visited = None
        self.visited_animation_idx = 0
        self.path_animation_idx = 0
        self.visited_done = False
        self.algorithm_running = False
        self.start_time = None
        self.end_time = None
        self.no_path = False

    # Tạo mới bản đồ với vật cản ngẫu nhiên
    def reset(self):
        self.grid = np.zeros((self.rows, self.cols), dtype=int)
        num_obstacles = int(self.rows * self.cols * 0.25)  # 25% là vật cản
        for _ in range(num_obstacles):
            row = np.random.randint(0, self.rows)
            col = np.random.randint(0, self.cols)
            if (row, col) != self.start and (row, col) != self.goal:
                self.grid[row][col] = 1

        # Reset các thông tin khác
        self.path = None
        self.visited = None
        self.visited_animation_idx = 0
        self.path_animation_idx = 0
        self.visited_done = False
        self.algorithm_running = False
        self.start_time = None
        self.end_time = None
        self.no_path = False

    # Vẽ lưới và các trạng thái trên màn hình
    def draw_grid(self):
        for row in range(self.rows):
            for col in range(self.cols):
                color = WHITE
                if self.grid[row][col] == 1:
                    color = BLACK
                pygame.draw.rect(self.screen, color, (col*CELL_SIZE, row*CELL_SIZE, CELL_SIZE, CELL_SIZE))
                pygame.draw.rect(self.screen, GRAY, (col*CELL_SIZE, row*CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

        # Vẽ ô đã duyệt (tím)
        if self.visited:
            for i in range(min(self.visited_animation_idx, len(self.visited))):
                r, c = self.visited[i]
                pygame.draw.rect(self.screen, PURPLE , (c*CELL_SIZE, r*CELL_SIZE, CELL_SIZE, CELL_SIZE))

        # Vẽ đường đi tìm được (vàng)
        if self.visited_done and self.path:
            for i in range(min(self.path_animation_idx, len(self.path))):
                r, c = self.path[i]
                pygame.draw.rect(self.screen, YELLOW, (c*CELL_SIZE, r*CELL_SIZE, CELL_SIZE, CELL_SIZE))

        # Vẽ điểm bắt đầu (xanh lá) và kết thúc (đỏ)
        pygame.draw.rect(self.screen, GREEN, (self.start[1]*CELL_SIZE, self.start[0]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(self.screen, RED, (self.goal[1]*CELL_SIZE, self.goal[0]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Hiển thị thông tin: độ dài đường đi, số ô đã khám phá, thời gian thực thi
    def draw_info(self):
        font = pygame.font.SysFont("Times New Roman", 24, bold=True)

        if self.visited_done:
            visited_count = len(self.visited) if self.visited else 0
            path_length = len(self.path) if self.path else 0
            time_taken = self.end_time - self.start_time if self.end_time and self.start_time else 0

            visited_text = font.render(f"Số ô đã khám phá: {visited_count}", True, BLUE)
            path_text = font.render(f"Độ dài đường đi: {path_length}", True, INFO_COLOR)
            time_text = font.render(f"Thời gian: {time_taken:.2f} giây", True, INFO_COLOR )

            self.screen.blit(visited_text, (10, 10))
            self.screen.blit(path_text, (10, 40))
            self.screen.blit(time_text, (10, 70))

        # Hiển thị lỗi nếu không tìm được đường đi
        if self.no_path and self.visited_done:
            error_font = pygame.font.SysFont("Times New Roman", 48, bold=True)
            text = error_font.render("Không tìm thấy đường đi!", True, RED)
            rect = text.get_rect(center=(self.screen.get_width() // 2, 30))
            self.screen.blit(text, rect)

    # Chạy thuật toán dijkstra
    def run_algorithm(self):
        self.path, self.visited = dijkstra(self.grid, self.start, self.goal)
        self.visited_animation_idx = 0
        self.path_animation_idx = 0
        self.visited_done = False
        self.algorithm_running = True
        self.start_time = time.time()
        self.no_path = self.path is None

    # Cập nhật animation khi chạy thuật toán
    def update_animation(self):
        if not self.algorithm_running:
            return

        if not self.visited_done:
            visited_speed = 5
            self.visited_animation_idx += visited_speed
            if self.visited_animation_idx >= len(self.visited):
                self.visited_done = True
                self.path_animation_idx = 0
        else:
            if self.no_path:
                self.algorithm_running = False
                self.end_time = time.time()
            else:
                path_speed = 1
                self.path_animation_idx += path_speed
                if self.path_animation_idx >= len(self.path):
                    self.algorithm_running = False
                    self.end_time = time.time()

    # Xử lý chuột phải đặt start/goal
    def handle_mouse_click(self, pos, is_right_click=False):
        col, row = pos[0] // CELL_SIZE, pos[1] // CELL_SIZE
        if not is_right_click:
            if (row, col) != self.goal:
                self.start = (row, col)
        else:
            if (row, col) != self.start:
                self.goal = (row, col)

    # Thêm hoặc xoá vật cản tại ô được nhấn chuột trái
    def toggle_obstacle(self, pos):
        col, row = pos[0] // CELL_SIZE, pos[1] // CELL_SIZE
        if (row, col) != self.start and (row, col) != self.goal:
            self.grid[row][col] = 1 if self.grid[row][col] == 0 else 0

    # Xoá toàn bộ vật cản
    def remove_obstacles(self):
        self.grid = np.zeros((self.rows, self.cols), dtype=int)

# Hàm main khởi chạy chương trình
def main():
    pygame.init()
    screen = pygame.display.set_mode((COLS*CELL_SIZE, ROWS*CELL_SIZE))
    pygame.display.set_caption("BFS Pathfinding with Random Obstacles")
    clock = pygame.time.Clock()

    visualizer = PathfindingVisualizer(screen, ROWS, COLS)
    visualizer.reset()

    running = True
    while running:
        screen.fill(WHITE)
        visualizer.draw_grid()
        visualizer.draw_info()
        visualizer.update_animation()
        pygame.display.flip()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    visualizer.run_algorithm()
                elif event.key == pygame.K_r:
                    visualizer.reset()
                elif event.key == pygame.K_c:
                    visualizer.remove_obstacles()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if event.button == 1:
                    visualizer.toggle_obstacle(pos)
                elif event.button == 3:
                    visualizer.handle_mouse_click(pos, is_right_click=True)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
