class Node:
    def __init__(self, data, parent):
        # Khởi tạo một Node với giá trị data, con trái và con phải là None, và con trỏ parent
        self.data = data  
        self.leftChild = None  
        self.rightChild = None  
        self.parent = parent  

class BinarySearchTree:
    def __init__(self):
        # Khởi tạo một cây tìm kiếm nhị phân rỗng với root là None
        self.root = None  
        
    def insert(self, data):
        # Chèn một node mới với giá trị data vào cây
        if self.root is None:  
            # Nếu cây là trống, tạo một node mới làm root
            self.root = Node(data, None)  
        else:  
            # Nếu cây không trống, gọi phương thức insert_node để tìm vị trí phù hợp cho node mới
            self.insert_node(data, self.root)
    
    def insert_node(self, data, node):
        # Phương thức hỗ trợ để đệ quy tìm vị trí phù hợp để chèn node mới
        if data < node.data:  
            # Nếu data nhỏ hơn giá trị hiện tại của node, điều hướng sang cây con bên trái
            if node.leftChild:  
                # Nếu có con trái, gọi đệ quy insert_node
                self.insert_node(data, node.leftChild)  
            else:  
                # Nếu không có con trái, tạo một node mới làm con trái
                node.leftChild = Node(data, node)  
        else:  
            # Nếu data lớn hơn, điều hướng sang cây con bên phải
            if node.rightChild:  
                # Nếu có con phải, gọi đệ quy insert_node
                self.insert_node(data, node.rightChild)  
            else:  
                # Nếu không có con phải, tạo một node mới làm con phải
                node.rightChild = Node(data, node)


    def remove_node(self, data, node):
        # Phương thức hỗ trợ để loại bỏ một node với giá trị data khỏi cây
        if node is None:
            return 
        
        if data < node.data:
            # Nếu data nhỏ hơn giá trị hiện tại của node, điều hướng sang cây con bên trái
            self.remove_node(data, node.leftChild)
        elif data > node.data:
            # Nếu data lớn hơn, điều hướng sang cây con bên phải
            self.remove_node(data, node.rightChild)
        else:
            # Node với giá trị data cần loại bỏ được tìm thấy

            if node.leftChild is None and node.rightChild is None:
                # Trường hợp 1: Loại bỏ một leaf node
                print("Đang loại bỏ một leaf node...%d" % node.data)

                parent = node.parent 

                if parent is not None and parent.leftChild == node:
                    parent.leftChild = None
                if parent is not None and parent.rightChild == node:
                    parent.rightChild = None

                if parent is None:
                    # Nếu node bị loại bỏ là root, đặt root là None
                    self.root = None

                del node 

            elif node.leftChild is None and node.rightChild is not None:
                # Trường hợp 2: Loại bỏ một node có một con phải
                print("Đang loại bỏ một node có một con phải..")

                parent = node.parent 

                if parent is not None:
                    if parent.leftChild == node:
                        parent.leftChild == node.rightChild
                    if parent.rightChild == node:
                        parent.rightChild = node.rightChild
                else:
                    self.root = node.rightChild
                
                node.rightChild.parent = parent
                del node 
            
            elif node.rightChild is None and node.leftChild is not None:
                # Trường hợp 3: Loại bỏ một node có một con trái
                print("Đang loại bỏ một node có một con trái..")

                parent = node.parent 

                if parent is not None:
                    if parent.leftChild == node:
                        parent.leftChild == node.leftChild
                    if parent.rightChild == node:
                        parent.rightChild = node.leftChild
                else:
                    self.root = node.rightChild
                
                node.rightChild.parent = parent
                del node 
            
            else:
                # Trường hợp 4: Loại bỏ một node có cả hai con
                print('Đang loại bỏ node có cả hai con...')

                predecessor = self.get_predecessor(node.leftChild)

                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                # Gọi đệ quy loại bỏ predecessor node
                self.remove_node(data, predecessor)

    def get_predecessor(self, node):
        # Phương thức hỗ trợ để tìm predecessor node (giá trị lớn nhất trong cây con bên trái)
        if node.rightChild:
            return self.get_predecessor(node.rightChild)
        
        return node 
    
    def remove(self, data):
        # Phương thức công cộng để bắt đầu quá trình loại bỏ
        if self.root is not None:
            self.remove_node(data, self.root)

    def traverse(self):  
        # Phương thức công cộng để bắt đầu duyệt cây theo thứ tự
        if self.root is not None: 
            self.traverse_in_order(self.root)  

    def get_max_value(self):  
        # Phương thức công cộng để lấy giá trị lớn nhất trong cây
        if self.root is not None: 
            return self.get_max(self.root)  

    def get_max(self, node):  
        # Phương thức hỗ trợ để tìm giá trị lớn nhất bắt đầu từ một node cho trước
        if node.rightChild:  
            return self.get_max(node.rightChild) 
        return node.data
    
    def get_min_value(self):  
        # Phương thức công cộng để lấy giá trị nhỏ nhất trong cây
        if self.root is not None:  
            return self.get_min(self.root)   

    def get_min(self, node):  
        # Phương thức hỗ trợ để tìm giá trị nhỏ nhất bắt đầu từ một node cho trước
        if node.leftChild:  
            return self.get_min(node.leftChild)  
        return node.data  

    def traverse_in_order(self, node):  
        # Phương thức hỗ trợ để thực hiện duyệt cây theo thứ tự (trái, node hiện tại, phải)
        if node.leftChild:  
            self.traverse_in_order(node.leftChild)  
        print('%s' % node.data)  
        if node.rightChild:  
            self.traverse_in_order(node.rightChild)

# Ví dụ sử dụng:
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(66)
bst.insert(-5)
bst.insert(1)
bst.insert(99)
bst.insert(34)
bst.insert(1000)
bst.remove(1000)
bst.traverse()

