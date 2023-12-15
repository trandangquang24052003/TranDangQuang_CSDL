class Node:
    def __init__(self, data, parent):
        # Khởi tạo nút với giá trị data, cha là parent
        self.data = data
        self.left_node = None
        self.right_node = None
        self.parent = parent
        self.height = 0


class AVLTree:
    def __init__(self):
        # Khởi tạo cây AVL với root là None
        self.root = None

    def remove(self, data):
        if self.root:
            # Nếu cây không rỗng, gọi hàm remove_node để xóa giá trị data
            self.remove_node(data, self.root)

    def insert(self, data):
        if self.root is None:
            # Nếu cây rỗng, tạo một nút mới với giá trị data làm root
            self.root = Node(data, None)
        else:
            # Ngược lại, gọi hàm insert_node để thêm giá trị data vào cây
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        # Thêm giá trị data vào cây bắt đầu từ nút node
        if data < node.data:
            # Nếu giá trị data nhỏ hơn giá trị của nút, thêm vào cây con bên trái
            if node.left_node:
                self.insert_node(data, node.left_node)
            else:
                node.left_node = Node(data, node)
                # Cập nhật chiều cao của nút và kiểm tra và cân bằng cây
                node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node)) + 1
        else:
            # Ngược lại, thêm vào cây con bên phải
            if node.right_node:
                self.insert_node(data, node.right_node)
            else:
                node.right_node = Node(data, node)
                # Cập nhật chiều cao của nút và kiểm tra và cân bằng cây
                node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node)) + 1

        # Kiểm tra và cân bằng cây từ nút vừa thêm vào
        self.handle_violation(node)

    def remove_node(self, data, node):
        # Xóa giá trị data khỏi cây bắt đầu từ nút node
        if node is None:
            return

        if data < node.data:
            self.remove_node(data, node.left_node)
        elif data > node.data:
            self.remove_node(data, node.right_node)
        else:
            if node.left_node is None and node.right_node is None:
                # Nút là lá, xóa nút và cân bằng cây từ nút cha
                print("Xóa một nút lá...%d" % node.data)
                parent = node.parent
                if parent is not None and parent.left_node == node:
                    parent.left_node = None
                if parent is not None and parent.right_node == node:
                    parent.right_node = None
                if parent is None:
                    self.root = None
                del node
                self.handle_violation(parent)
            elif node.left_node is None and node.right_node is not None:
                # Nút có một con phải, xóa nút và cân bằng cây từ nút cha
                print("Xóa một nút có một con phải...")
                parent = node.parent
                if parent is None:
                    self.root = node.right_node
                else:
                    if parent.left_node == node:
                        parent.left_node = node.right_node
                    else:
                        parent.right_node = node.right_node
                    node.right_node.parent = parent
                del node
                self.handle_violation(parent)
            elif node.right_node is None and node.left_node is not None:
                # Nút có một con trái, xóa nút và cân bằng cây từ nút cha
                print("Xóa một nút có một con trái...")
                parent = node.parent
                if parent is None:
                    self.root = node.left_node
                else:
                    if parent.left_node == node:
                        parent.left_node = node.left_node
                    else:
                        parent.right_node = node.left_node
                    node.left_node.parent = parent
                del node
                self.handle_violation(parent)
            else:
                # Nút có hai con, đổi giá trị với tiền nhiệm và xóa tiền nhiệm
                print('Xóa nút có hai con...')
                predecessor = self.get_predecessor(node.left_node)
                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp
                self.remove_node(data, predecessor)

    def get_predecessor(self, node):
        # Tìm tiền nhiệm của nút (nút có giá trị lớn nhất trong cây con trái)
        if node.right_node:
            return self.get_predecessor(node.right_node)
        return node

    def handle_violation(self, node):
        # Kiểm tra và cân bằng cây từ nút đưa vào
        while node is not None:
            # Cập nhật chiều cao của nút và kiểm tra và cân bằng cây
            node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node)) + 1
            self.violation_helper(node)
            node = node.parent

    def violation_helper(self, node):
        # Kiểm tra cân bằng của nút và thực hiện các phép xoay cần thiết
        balance = self.calculate_balance(node)
        if balance > 1:
            if self.calculate_balance(node.left_node) < 0:
                # Thực hiện xoay phải cho cây con trái
                self.rotate_left(node.left_node)
            # Thực hiện xoay trái cho nút hiện tại
            self.rotate_right(node)
        if balance < -1:
            if self.calculate_balance(node.right_node) < 0:
                # Thực hiện xoay phải cho cây con phải
                self.rotate_right(node.right_node)
            # Thực hiện xoay trái cho nút hiện tại
            self.rotate_left(node)

    def calc_height(self, node):
        # Trả về chiều cao của một nút. Nếu nút là None, trả về -1.
        if node is None:
            return -1
        return node.height

    def calculate_balance(self, node):
        # Trả về giá trị cân bằng của một nút, là sự chênh lệch giữa chiều cao của cây con bên trái và cây con bên phải
        if node is None:
            return 0
        return self.calc_height(node.left_node) - self.calc_height(node.right_node)

    def traverse(self):
        # Duyệt cây theo thứ tự trung tâm và in thông tin về từng nút
        if self.root is not None:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        # Duyệt cây theo thứ tự trung tâm và in thông tin về từng nút
        if node.left_node:
            self.traverse_in_order(node.left_node)

        l = '' if node.left_node is not None else 'NULL'
        r = '' if node.right_node is not None else 'NULL'
        p = '' if node.parent is not None else 'NULL'

        print("%s trái: %s phải: %s cha: %s chiều cao: %s" % (node.data, l, r, p, node.height))

        if node.right_node:
            self.traverse_in_order(node.right_node)

    def rotate_right(self, node):
        # Thực hiện phép xoay cây về bên phải tại một nút
        print("Xoay về bên phải tại nút", node.data)

        temp_left_node = node.left_node
        t = temp_left_node.right_node

        temp_left_node.right_node = node
        node.left_node = t

        if t is not None:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_left_node
        temp_left_node.parent = temp_parent

        if temp_left_node.parent is not None and temp_left_node.parent.left_node == node:
            temp_left_node.parent.left_node = temp_left_node

        if temp_left_node.parent is not None and temp_left_node.parent.right_node == node:
            temp_left_node.parent.right_node = temp_left_node

        if node == self.root:
            self.root = temp_left_node

        node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node))
        temp_left_node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node)) + 1

    def rotate_left(self, node):
        # Thực hiện phép xoay cây về bên trái tại một nút
        print("Xoay về bên trái tại nút", node.data)

        temp_right_node = node.right_node
        t = temp_right_node.left_node

        temp_right_node.left_node = node
        node.right_node = t

        if t is not None:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_right_node
        temp_right_node.parent = temp_parent

        if temp_right_node.parent is not None and temp_right_node.parent.left_node == node:
            temp_right_node.parent.left_node = temp_right_node

        if temp_right_node.parent is not None and temp_right_node.parent.right_node == node:
            temp_right_node.parent.right_node = temp_right_node

        if node == self.root:
            self.root = temp_right_node

        node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node))
        temp_right_node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node)) + 1


if __name__ == '__main__':
    # Tạo đối tượng AVLTree
    avl = AVLTree()
    # Thêm các giá trị vào cây
    avl.insert(32)
    avl.insert(16)
    avl.insert(48)
    avl.insert(8)
    avl.insert(24)
    avl.insert(40)
    avl.insert(56)
    avl.insert(36)
    avl.insert(44)
    avl.insert(52)
    avl.insert(60)
    avl.insert(4)
    avl.insert(58)
    avl.insert(62)
    # Xóa một giá trị khỏi cây
    avl.remove(4)
    # In thông tin về cây sau mỗi thay đổi
    avl.traverse()

