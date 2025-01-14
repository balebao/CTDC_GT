def merge(arr, left, mid, right):
    # Kích thước của các mảng con
    n1 = mid - left + 1
    n2 = right - mid

    # Tạo các mảng tạm
    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]

    # Trộn hai mảng L và R vào arr[left..right]
    i = 0
    j = 0
    k = left
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Sao chép phần còn lại của L, nếu có
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Sao chép phần còn lại của R, nếu có
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2  # Tìm điểm giữa mảng

        # Sắp xếp đệ quy hai nửa
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        # Trộn hai nửa đã sắp xếp
        merge(arr, left, mid, right)

# Test
arr = [5, 2, 9, 1, 5, 6]
merge_sort(arr, 0, len(arr) - 1)

print("Kết quả Merge Sort:", arr)
