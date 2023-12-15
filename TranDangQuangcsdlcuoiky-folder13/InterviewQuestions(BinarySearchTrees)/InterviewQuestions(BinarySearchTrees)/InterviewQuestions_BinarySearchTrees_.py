class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_same_tree(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    elif tree1 is None or tree2 is None:
        return False

    # So sánh giá trị của nút hiện tại
    if tree1.value != tree2.value:
        return False

    # So sánh các cây con bên trái và bên phải
    return (is_same_tree(tree1.left, tree2.left) and
            is_same_tree(tree1.right, tree2.right))

# Ví dụ sử dụng
# Xây dựng cây 1
tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)

# Xây dựng cây 2
tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.right = TreeNode(3)

result = is_same_tree(tree1, tree2)
print(result)  # Kết quả: True

