class heaptransformer:

    def __init__(self, heap):
        # Khởi tạo đối tượng heaptransformer với một mảng (heap) như đầu vào.
        self.heap = heap
        
    def transform(self):
        # Duyệt qua các phần tử từ cuối cùng của mảng đến phần tử đầu tiên.
        # Với mỗi phần tử, gọi phương thức fix_down để duy trì tính chất heap.
        for i in range((len(self.heap) - 2) // 2, -1, -1):
            self.fix_down(i)
            
    def fix_down(self, index):
        # Phương thức để duy trì tính chất heap từ vị trí chỉ định bằng cách đổi chỗ các phần tử với phần tử con có giá trị nhỏ hơn.
        
        index_left = 2 * index + 1
        index_right = 2 * index + 2
        
        index_largest = index
        
        # So sánh giá trị của phần tử con trái với phần tử cha.
        if index_left < len(self.heap) and self.heap[index_left] < self.heap[index]:
            index_largest = index_left
            
        # So sánh giá trị của phần tử con phải với phần tử lớn nhất hiện tại.
        if index_right < len(self.heap) and self.heap[index_right] < self.heap[index_largest]:
            index_largest = index_right
            
        # Nếu phần tử cha không là lớn nhất, đổi chỗ nó với phần tử lớn nhất và tiếp tục đệ quy để đảm bảo tính chất heap.
        if index != index_largest:
            self.heap[index], self.heap[index_largest] = self.heap[index_largest], self.heap[index]
            self.fix_down(index_largest)
    
if __name__ == '__main__':
    # Tạo một mảng đầu vào.
    n = [210, 100, 23, 2, 5]
    
    # Tạo một đối tượng heaptransformer với mảng đầu vào và thực hiện phép biến đổi để chuyển thành heap.
    heap_transform = heaptransformer(n)
    heap_transform.transform()
    
    # In mảng sau khi đã chuyển thành heap.
    print(heap_transform.heap)

