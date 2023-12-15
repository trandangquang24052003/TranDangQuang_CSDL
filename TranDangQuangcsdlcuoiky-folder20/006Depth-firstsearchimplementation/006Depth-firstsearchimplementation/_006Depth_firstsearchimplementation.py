class Node:

    def __init__(self, name):
        # Hàm khởi tạo của lớp Node. Được gọi khi một đối tượng Node mới được tạo. Nhận vào một tham số name để xác định tên của đỉnh.
        self.name = name 
        # Gán giá trị của tham số name cho thuộc tính name của đối tượng Node.
        self.adjacency_list = []
        # Khởi tạo một danh sách kề để lưu trữ các đỉnh kề với đỉnh hiện tại.
        self.visited = False
        # Một thuộc tính visited để theo dõi trạng thái của đỉnh trong quá trình duyệt đồ thị. Ban đầu, đặt giá trị là False.

def depth_first_search(start_node):

    #  Định nghĩa hàm depth_first_search nhận vào một đỉnh start_node làm đỉnh xuất phát cho DFS.
    stack = [start_node]
    # Khởi tạo một stack với đỉnh xuất phát.
    start_node.visited = True

    # Đánh dấu đỉnh xuất phát là đã thăm.
    while stack:

        #  Bắt đầu vòng lặp DFS, lặp cho đến khi stack trở thành rỗng.
        actual_node = stack.pop()
        # Lấy ra đỉnh hiện tại từ stack để xử lý.
        print(actual_node.name)

        for n in actual_node.adjacency_list:
            # Duyệt qua tất cả các đỉnh kề của đỉnh hiện tại.
            if not n.visited:
                #  Nếu đỉnh kề chưa được thăm, đánh dấu nó là đã thăm và thêm vào stack để duyệt tiếp.
                n.visited = True
                stack.append(n)

if __name__ == '__main__':
    
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")

    node1.adjacency_list.append(node2)
    node1.adjacency_list.append(node3)
    node2.adjacency_list.append(node4)
    node4.adjacency_list.append(node5)

    depth_first_search(node1)
    
    
