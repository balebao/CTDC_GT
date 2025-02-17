from collections import deque

# Kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Sinh danh sách số nguyên tố 4 chữ số
def generate_primes():
    return {str(i) for i in range(1000, 10000) if is_prime(i)}

# BFS tìm số bước ngắn nhất từ S đến T
def bfs(start, target, primes):
    if start == target:
        return 0
    queue = deque([(start, 0)])
    visited = {start}
    
    while queue:
        current, steps = queue.popleft()
        
        # Thử thay đổi từng chữ số
        for i in range(4):
            for digit in '0123456789':
                if current[i] != digit:
                    new_number = current[:i] + digit + current[i+1:]
                    if new_number in primes and new_number not in visited:
                        if new_number == target:
                            return steps + 1
                        visited.add(new_number)
                        queue.append((new_number, steps + 1))
    return -1

# Xử lý các test
def solve():
    primes = generate_primes()
    T = int(input("Đọc số lượng test: "))  # Đọc số lượng test
    for _ in range(T):
        S, T = input("S T: ").split()
        print(bfs(S, T, primes))

# Chạy chương trình
solve()
