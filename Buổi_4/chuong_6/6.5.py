def min_operations(S, T):
    steps = 0
    while T > S:
        if T % 2 == 0:
            T //= 2  # Nếu T là chẵn, thực hiện thao tác (b) ngược lại
        else:
            T += 1  # Nếu T là lẻ, thực hiện thao tác (a) ngược lại
        steps += 1
    # Nếu T nhỏ hơn S, chỉ có thể thực hiện thao tác (a) để giảm T về S
    steps += S - T
    return steps

# Phần nhập dữ liệu từ bàn phím
T = int(input("Số lượng bộ test: "))  # Số lượng bộ test
for _ in range(T):
    S, T = map(int, input("Nhập S và T cho mỗi bộ test: ").split())  # Nhập S và T cho mỗi bộ test
    result = min_operations(S, T)
    print(result)
