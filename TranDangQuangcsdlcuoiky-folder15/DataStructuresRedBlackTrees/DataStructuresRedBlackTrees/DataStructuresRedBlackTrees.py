class Color:
    RED = 1  # Mã màu đỏ
    BLACK = 2  # Mã màu đen

class Node:
    def __init__(self, data, parent=None, color=Color.RED):
        # Khởi tạo một node mới với dữ liệu, node cha (mặc định là None), và màu (mặc định là Đỏ).
        self.data = data
        self.color = color
        self.parent = parent
        self.left = None
        self.right = None

class RedBlackTree:
    def __init__(self):
        # Khởi tạo cây Red-Black với root là None.
        self.root = None

    def insert(self, data):
        # Chèn một node mới vào cây Red-Black và kiểm tra vi phạm các điều kiện của cây.
        if not self.root:
            self.root = Node(data)
            self.violate(self.root)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        # Chèn một node mới vào cây con được xác định bởi node hiện tại.
        if data < node.data:
            if node.left:
                self.insert_node(data, node.left)
            else:
                node.left = Node(data, node)
                self.violate(node.left)
        else:
            if node.right:
                self.insert_node(data, node.right)
            else:
                node.right = Node(data, node)
                self.violate(node.right)

    def violate(self, node):
        # Xử lý vi phạm các điều kiện của cây Red-Black sau khi chèn node mới.
        parent_node = None
        grand_parent_node = None

        while node != self.root and node.parent.color == Color.RED:
            parent_node = node.parent
            grand_parent_node = parent_node.parent

            if grand_parent_node is None:
                return

            if parent_node == grand_parent_node.left:
                uncle = grand_parent_node.right

                if uncle and uncle.color == Color.RED:
                    # case 1 và case 4
                    print("Đổi màu node %s thành Đỏ" % grand_parent_node.data)
                    grand_parent_node.color = Color.RED
                    print("Đổi màu node %s thành Đen" % parent_node.data)
                    parent_node.color = Color.BLACK
                    uncle.color = Color.BLACK
                    node = grand_parent_node
                else:
                    # case 2: node chú là đen và node là con phải
                    if node == parent_node.right:
                        self.rotate_left(parent_node)
                        node = parent_node
                        parent_node = node.parent

                    # case 3
                    parent_node.color = Color.BLACK
                    grand_parent_node.color = Color.RED
                    print("Đổi màu %s thành Đen" % parent_node.data)
                    print("Đổi màu %s thành Đỏ" % grand_parent_node.data)
                    self.rotate_right(grand_parent_node)
            else:
                uncle = grand_parent_node.left

                if uncle and uncle.color == Color.RED:
                    # case 1 và case 4
                    print("Đổi màu node %s thành Đỏ" % grand_parent_node.data)
                    grand_parent_node.color = Color.RED
                    print("Đổi màu node %s thành Đen" % parent_node.data)
                    parent_node.color = Color.BLACK
                    uncle.color = Color.BLACK
                    node = grand_parent_node
                else:
                    # case 2: node chú là đen và node là con trái
                    if node == parent_node.left:
                        self.rotate_right(parent_node)
                        node = parent_node
                        parent_node = node.parent

                    # case 3
                    parent_node.color = Color.BLACK
                    grand_parent_node.color = Color.RED
                    print("Đổi màu %s thành Đen" % parent_node.data)
                    print("Đổi màu %s thành Đỏ" % grand_parent_node.data)
                    self.rotate_left(grand_parent_node)

        if self.root.color == Color.RED:
            print("Đổi màu gốc thành Đen...")  # Recolor gốc thành Đen
            self.root.color = Color.BLACK

    def traverse(self):
        # Thực hiện duyệt cây theo thứ tự trung tố (in-order).
        if self.root is not None:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        # Duyệt cây theo thứ tự trung tố (in-order) bắt đầu từ node được chỉ định.
        if node.left:
            self.traverse_in_order(node.left)

        # (Thêm các công việc khác cần thiết ở đây)

    def rotate_right(self, node):
        # Thực hiện phép quay phải trên node được chỉ định để duy trì tính cân bằng.
        print("Quay phải trên node ", node.data)

        temp_left_node = node.left
        t = temp_left_node.right

        temp_left_node.right = node
        node.left = t

        if t is not None:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_left_node
        temp_left_node.parent = temp_parent

        if temp_left_node.parent is not None and temp_left_node.parent.left == node:
            temp_left_node.parent.left = temp_left_node

        if temp_left_node.parent is not None and temp_left_node.parent.right == node:
            temp_left_node.parent.right = temp_left_node

        if node == self.root:
            self.root = temp_left_node

    def rotate_left(self, node):
        # Thực hiện phép quay trái trên node được chỉ định để duy trì tính cân bằng.
        print("Quay trái trên node ", node.data)

        temp_right_node = node.right
        t = temp_right_node.left

        temp_right_node.left = node
        node.right = t

        if t is not None:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_right_node
        temp_right_node.parent = temp_parent

        if temp_right_node.parent is not None and temp_right_node.parent.left == node:
            temp_right_node.parent.left = temp_right_node

        if temp_right_node.parent is not None and temp_right_node.parent.right == node:
            temp_right_node.parent.right = temp_right_node

        if node == self.root:
            self.root = temp_right_node


# Tạo một đối tượng RedBlackTree
rbt = RedBlackTree()

# Chèn các giá trị vào cây
rbt.insert(32)
rbt.insert(10)
rbt.insert(55)
rbt.insert(1)
rbt.insert(19)
rbt.insert(79)
rbt.insert(16)
rbt.insert(23)
rbt.insert(12)

# Thực hiện duyệt cây
rbt.traverse()

