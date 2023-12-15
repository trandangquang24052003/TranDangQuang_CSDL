class HashTable:
    def __init__(self):
        # Khởi tạo bảng băm với sức chứa mặc định là 10
        self.capacity = 10
        # Mảng lưu trữ các khóa
        self.keys = [None] * self.capacity
        # Mảng lưu trữ các giá trị
        self.values = [None] * self.capacity

    def insert(self, key, data):
        # Tính chỉ số sử dụng hàm băm
        index = self.hash_function(key)

        # Xử lý va chạm: Duyệt tìm vị trí trống để chèn
        while self.keys[index] is not None:
            # Nếu khóa đã tồn tại, cập nhật giá trị
            if self.keys[index] == key:
                self.values[index] = data
                return

            # Duyệt tới vị trí tiếp theo theo phương pháp linear probing
            index = (index + 1) % self.capacity

        # Chèn khóa và giá trị tại vị trí đã tìm được
        self.keys[index] = key
        self.values[index] = data

    def get(self, key):
        # Tính chỉ số sử dụng hàm băm
        index = self.hash_function(key)

        # Duyệt để tìm giá trị tương ứng với khóa
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]

            # Duyệt tới vị trí tiếp theo theo phương pháp linear probing
            index = (index + 1) % self.capacity

        # Trả về None nếu không tìm thấy khóa
        return None

    def hash_function(self, key):
        # Tính tổng ASCII của các ký tự trong khóa và lấy phần dư cho sức chứa
        hash_sum = 0
        for letter in key:
            hash_sum = hash_sum + ord(letter)
        return hash_sum % self.capacity

if __name__ == '__main__':
    # Tạo một đối tượng HashTable
    table = HashTable()
    
    # Chèn ba cặp khóa-giá trị vào bảng băm
    table.insert('Adam', 23)
    table.insert('Kevin', 45)
    table.insert('Daniel', 34)

    # In ra giá trị băm của khóa 'adam'
    print(table.hash_function('adam'))

    # Lấy và in ra giá trị tương ứng với khóa 'Adam'
    print(table.get('Adam'))

