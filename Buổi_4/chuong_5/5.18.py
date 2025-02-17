def find_right_greater_frequency(n, A):
    # Đếm số lần xuất hiện của mỗi phần tử
    freq = {}
    for num in A:
        freq[num] = freq.get(num, 0) + 1

    # Mảng kết quả
    result = [-1] * n
    stack = []

    # Duyệt từ phải qua trái
    for i in range(n - 1, -1, -1):
        while stack and freq[A[stack[-1]]] <= freq[A[i]]:
            stack.pop()

        if stack:
            result[i] = A[stack[-1]]

        stack.append(i)

    return result

# Nhập dữ liệu từ bàn phím
T = int(input("Nhập số lượng bộ test: "))  # Số lượng bộ test
for _ in range(T):
    n = int(input())  # Số phần tử của mảng A[]
    A = list(map(int, input("Nhập các phần tử của mảng A[]: ").split()))  # Mảng A[]
    result = find_right_greater_frequency(n, A)
    print(*result)
