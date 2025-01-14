#include <iostream>
#include <vector>
#include <cstdlib>  // Thư viện cho rand()

using namespace std;

// Hàm Partition: Đưa pivot về vị trí đúng và sắp xếp các phần tử
int partition(vector<int>& arr, int low, int high) {
    int pivot = arr[high];  // Chọn pivot là phần tử cuối
    int i = low - 1;  // Chỉ số nhỏ hơn pivot

    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            // Hoán đổi arr[i] và arr[j]
            swap(arr[i], arr[j]);
        }
    }

    // Hoán đổi pivot với arr[i+1] để đưa pivot vào vị trí đúng
    swap(arr[i + 1], arr[high]);

    return i + 1;  // Vị trí của pivot
}

// Hàm Randomized Partition: Chọn pivot ngẫu nhiên
int randomized_partition(vector<int>& arr, int low, int high) {
    int pivot_index = rand() % (high - low + 1) + low;  // Chọn chỉ số ngẫu nhiên cho pivot
    swap(arr[pivot_index], arr[high]);  // Hoán đổi pivot với phần tử cuối
    return partition(arr, low, high);
}

// Hàm Quick Sort ngẫu nhiên
void quick_sort_randomized(vector<int>& arr, int low, int high) {
    if (low < high) {
        int p = randomized_partition(arr, low, high);  // Phân vùng ngẫu nhiên
        quick_sort_randomized(arr, low, p - 1);  // Gọi đệ quy cho mảng bên trái của pivot
        quick_sort_randomized(arr, p + 1, high);  // Gọi đệ quy cho mảng bên phải của pivot
    }
}

int main() {
    vector<int> arr = {5, 2, 9, 1, 5, 6};

    quick_sort_randomized(arr, 0, arr.size() - 1);

    cout << "Kết quả Quick Sort Randomized: ";
    for (int x : arr) {
        cout << x << " ";
    }
    cout << endl;

    return 0;
}
