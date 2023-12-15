class Node:
    def __init__(self, name):
        self.name = name 
        #  Gán giá trị của tham số name cho thuộc tính name của đối tượng Node.
        self.adjacency_list = []  
        # Khởi tạo một danh sách kề để lưu trữ các đỉnh kề với đỉnh hiện tại.      
        self.visited = False 
        #  Một thuộc tính visited để theo dõi trạng thái của đỉnh trong quá trình duyệt đồ thị. Ban đầu, đặt giá trị là False.

def breadth_first_search(star_node) : # Định nghĩa hàm
    # Hàm khởi tạo của lớp Node. Được gọi khi một đối tượng Node mới được tạo. Nhận vào một tham số name để xác định tên của đỉnh.
    queue = [star_node] 
    # Tạo một hàng đợi (queue) ban đầu chứa đỉnh xuất phát.

    while queue:
       # Thực hiện vòng lặp trong khi hàng đợi không rỗng.

        actual_node = queue.pop(0) 
        #  Lấy ra đỉnh đầu tiên từ hàng đợi để xử lý và loại bỏ nó khỏi hàng đợi.
        actual_node.visited = True
        # Đánh dấu đỉnh hiện tại là đã thăm.
        print(actual_node.name)
        # In tên của đỉnh hiện tại.

        for n in actual_node.adjacency_list:
            # Duyệt qua tất cả các đỉnh kề của đỉnh hiện tại.
            if not n.visited:
                # Nếu đỉnh kề chưa được thăm, thêm nó vào hàng đợi để duyệt tiếp.
                queue.append(n)

if __name__ == '__main__' :
    
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")

    node1.adjacency_list.append(node2)
    node1.adjacency_list.append(node3)
    node2.adjacency_list.append(node4)
    node4.adjacency_list.append(node5)

    breadth_first_search(node1)
