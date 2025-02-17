def count_bdn_less_than_n(N):
    # Hàm đệ quy sinh số BDN
    def generate_bdn(current):
        if current > N:
            return 0
        count = 1 if current > 0 else 0
        # Tiếp tục tạo các số BDN bằng cách thêm 0 hoặc 1 vào
        count += generate_bdn(current * 10)  # Thêm 0 vào
        count += generate_bdn(current * 10 + 1)  # Thêm 1 vào
        return count

    return generate_bdn(1)

# Phần nhập dữ liệu từ bàn phím
T = int(input("Số lượng bộ test: "))  # Số lượng bộ test
for _ in range(T):
    N = int(input("Nhập số N cho mỗi test: "))  # Nhập số N cho mỗi test
    result = count_bdn_less_than_n(N)
    print(result)
