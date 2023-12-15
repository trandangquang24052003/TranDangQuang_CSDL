CAPACITY = 10

class Heap:
    def __init__(self):
        # Khởi tạo một heap rỗng với kích thước ban đầu là 0 và một mảng để lưu trữ các phần tử của heap.
        self.heap_size = 0
        self.heap = [0] * CAPACITY

    def insert(self, item):
        # Chèn một phần tử vào heap và duy trì tính chất heap bằng cách gọi phương thức fix_up.
        if self.heap_size == CAPACITY:
            return
        self.heap[self.heap_size] = item
        self.heap_size = self.heap_size + 1
        self.fix_up(self.heap_size - 1)

    def fix_up(self, index):
        # Duy trì tính chất heap từ vị trí chỉ định bằng cách đổi chỗ các phần tử với phần tử cha cho đến khi tính chất heap được phục hồi.
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.fix_up(parent_index)

    def get_max(self):
        # Trả về phần tử lớn nhất trong heap, là phần tử ở đỉnh heap.
        return self.heap[0]

    def poll(self):
        # Lấy và trả về phần tử lớn nhất từ heap (phần tử ở đỉnh), sau đó sắp xếp lại heap bằng cách sử dụng phương thức fix_down.
        max_item = self.get_max()
        self.heap[0], self.heap[self.heap_size - 1] = self.heap[self.heap_size - 1], self.heap[0]
        self.heap_size = self.heap_size - 1
        self.fix_down(0)
        return max_item

    def fix_down(self, index):
        # Duy trì tính chất heap từ vị trí chỉ định bằng cách đổi chỗ các phần tử với phần tử con lớn nhất cho đến khi tính chất heap được phục hồi.
        index_left = 2 * index + 1
        index_right = 2 * index + 2
        largest_index = index

        if index_left < self.heap_size and self.heap[index_left] > self.heap[index]:
            largest_index = index_left

        if index_right < self.heap_size and self.heap[index_right] > self.heap[largest_index]:
            largest_index = index_right

        if index != largest_index:
            self.heap[index], self.heap[largest_index] = self.heap[largest_index], self.heap[index]
            self.fix_down(largest_index)

    def heap_sort(self):
        # Thực hiện sắp xếp heap bằng cách lặp lại việc gọi phương thức poll và in các phần tử đã được loại bỏ cho đến khi heap trống.
        for _ in range(self.heap_size):
            max_item = self.poll()
            print(max_item)

if __name__ == '__main__':
    # Tạo một thể hiện của lớp Heap.
    heap = Heap()
    heap.insert(13)
    heap.insert(-2)
    heap.insert(0)
    heap.insert(20)
    heap.insert(1)
    heap.insert(-5)
    heap.insert(99)

    # Thực hiện sắp xếp heap và in kết quả.
    heap.heap_sort()

