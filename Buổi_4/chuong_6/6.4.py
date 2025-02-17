def is_bdn(number):
    # Kiểm tra xem số có phải là số BDN không
    return all(digit in '01' for digit in str(number))

def find_bdn_number(N):
    M = 1
    while True:
        P = M * N
        if is_bdn(P):
            return P
        M += 1

# Phần nhập dữ liệu từ bàn phím
T = int(input("Số lượng bộ test: "))  # Số lượng bộ test
for _ in range(T):
    N = int(input("Nhập số N cho mỗi test: "))  # Nhập số N cho mỗi test
    result = find_bdn_number(N)
    print(result)
