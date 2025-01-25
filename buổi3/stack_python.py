class Stack:
    def __init__(self):
        # Sử dụng danh sách để lưu trữ các phần tử
        self.elements = []

    def push(self, item):
        # Thêm phần tử vào cuối danh sách
        self.elements.append(item)
        print(f"Đã thêm '{item}' vào ngăn xếp.")

    def pop(self):
        # Loại bỏ phần tử cuối cùng
        if not self.is_empty():
            item = self.elements.pop()
            print(f"Đã lấy '{item}' ra khỏi ngăn xếp.")
            return item
        else:
            print("Ngăn xếp trống!")
            return None

    def peek(self):
        # Truy cập phần tử cuối cùng
        if not self.is_empty():
            return self.elements[-1]
        else:
            print("Ngăn xếp trống!")
            return None

    def is_empty(self):
        # Kiểm tra xem danh sách có trống không
        return len(self.elements) == 0

    def size(self):
        # Trả về kích thước ngăn xếp
        return len(self.elements)

    def display(self):
        # In ngăn xếp từ đỉnh đến đáy
        print("Ngăn xếp (đỉnh đến đáy):", self.elements[::-1])


# Minh họa sử dụng ngăn xếp
if __name__ == "__main__":
    stack = Stack()
    stack.push("Sách A")
    stack.push("Sách B")
    stack.push("Sách C")

    stack.display()  # Output: Ngăn xếp (đỉnh đến đáy): ['Sách C', 'Sách B', 'Sách A']

    top_item = stack.peek()
    print("Phần tử ở đỉnh ngăn xếp:", top_item)  # Output: Sách C

    stack.pop()
    stack.display()  # Output: Ngăn xếp (đỉnh đến đáy): ['Sách B', 'Sách A']

    print("Ngăn xếp có trống không?", stack.is_empty())  # Output: False

    