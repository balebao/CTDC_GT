def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):  # Sửa lỗi (n-11 -> n-1-i)
            if arr[j] > arr[j + 1]:
                # Hoán đổi
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Nếu không có hoán đổi nào, mảng đã được sắp xếp
        if not swapped:
            break


if __name__ == "__main__":
    arr = [5, 2, 9, 1, 5]  # Sửa cú pháp khai báo mảng
    bubble_sort(arr)
    print("Kết quả sau Bubble Sort:", arr)  # Sửa cú pháp in kết quả
