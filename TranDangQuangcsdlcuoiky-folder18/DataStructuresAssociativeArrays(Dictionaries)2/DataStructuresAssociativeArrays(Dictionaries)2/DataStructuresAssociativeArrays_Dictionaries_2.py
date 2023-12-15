def is_min_heap(heap):
    # Tính số lượng nút không phải lá trong cây
    nums_item = (len(heap) - 2) // 2

    # Duyệt qua từng nút không phải lá để kiểm tra tính chất của min heap
    for i in range(nums_item):
        # Kiểm tra nút con bên trái
        if 2 * i + 1 < len(heap) and heap[i] > heap[2 * i + 1]:
            return False

        # Kiểm tra nút con bên phải
        if 2 * i + 2 < len(heap) and heap[i] > heap[2 * i + 2]:
            return False

    # Nếu không có trường hợp nào vi phạm tính chất, trả về True
    return True

if __name__ == '__main__':
    # Kiểm tra với một dãy số cụ thể
    n = [4, 6, 3, 2, -2]
    print(is_min_heap(n))

