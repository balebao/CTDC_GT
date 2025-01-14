
function partition!(arr, low, high)
    pivot = arr[high]  # Chọn pivot là phần tử cuối
    i = low - 1  # Chỉ số nhỏ hơn pivot

    for j in low:high-1
        if arr[j] <= pivot
            i += 1
            # Hoán đổi arr[i] và arr[j]
            arr[i], arr[j] = arr[j], arr[i]
        end
    end

    # Hoán đổi pivot với arr[i+1] để đưa pivot vào vị trí đúng
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1  # Vị trí của pivot
end

function randomized_partition!(arr, low, high)
    pivot_index = rand(low:high)  # Chọn chỉ số ngẫu nhiên cho pivot
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Hoán đổi pivot với phần tử cuối
    return partition!(arr, low, high)
end

function quick_sort_randomized!(arr, low, high)
    if low < high
        p = randomized_partition!(arr, low, high)  # Phân vùng ngẫu nhiên
        quick_sort_randomized!(arr, low, p - 1)  # Gọi đệ quy cho mảng bên trái của pivot
        quick_sort_randomized!(arr, p + 1, high)  # Gọi đệ quy cho mảng bên phải của pivot
    end
end

# Test
arr = [5, 2, 9, 1, 5, 6]
quick_sort_randomized!(arr, 1, length(arr))

println("Kết quả Quick Sort Randomized:", arr)
