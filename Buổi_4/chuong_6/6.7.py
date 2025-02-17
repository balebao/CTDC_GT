def is_valid_number(num):
    """Kiểm tra xem số num có thỏa mãn yêu cầu không."""
    digits = str(num)
    
    # Kiểm tra các chữ số có khác nhau không và đều nhỏ hơn hoặc bằng 5
    seen = set()
    for digit in digits:
        if digit in seen or int(digit) > 5:
            return False
        seen.add(digit)
    
    return True

def count_valid_numbers(L, R):
    """Đếm số lượng số thỏa mãn yêu cầu trong khoảng [L, R]."""
    count = 0
    for num in range(L, R + 1):
        if is_valid_number(num):
            count += 1
    return count

# Phần nhập dữ liệu
T = int(input("Số lượng bộ test: "))  # Số lượng bộ test
for _ in range(T):
    L, R = map(int, input("L R cho mỗi bộ test : ").split())  # L và R cho mỗi test
    result = count_valid_numbers(L, R)
    print(result)
