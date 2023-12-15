class Node:

    def __init__(self, name):
        # Khởi tạo một đối tượng Node với tên, danh sách kề rỗng và trạng thái chưa ghé thăm.
        self.name = name
        self.adjacency_list = []
        self.visited = False


def depth_first_search(node):
    # Hàm thực hiện duyệt đồ thị theo chiều sâu (DFS) từ một đỉnh (node) cho trước.

    # Đánh dấu đỉnh hiện tại là đã ghé thăm và in tên của đỉnh đó.
    node.visited = True
    print(node.name)

    # Duyệt qua tất cả các đỉnh kề của đỉnh hiện tại.
    for n in node.adjacency_list:
        # Nếu đỉnh kề chưa được ghé thăm, gọi đệ quy hàm depth_first_search với đỉnh kề đó.
        if not n.visited:
            depth_first_search(n)

if __name__ == '__main__':
    # Tạo các đối tượng Node đại diện cho các đỉnh của đồ thị.
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")

    # Xây dựng mối quan hệ kề giữa các đỉnh.
    node1.adjacency_list.append(node2)
    node1.adjacency_list.append(node3)
    node2.adjacency_list.append(node4)
    node4.adjacency_list.append(node5)

    # Gọi hàm depth_first_search để bắt đầu duyệt đồ thị từ một đỉnh bất kỳ (ở đây là node1).
    depth_first_search(node1)

