from collections import deque

class MazeSolver:

    def __init__(self, matrix):
        # Khởi tạo MazeSolver với ma trận đại diện cho mê cung, các hướng di chuyển, mảng visited và khoảng cách ngắn nhất.
        self.matrix = matrix
        self.move_x = [1, 0, 0, -1]  # Di chuyển sang phải, không di chuyển theo chiều ngược lại, di chuyển lên, không di chuyển theo chiều ngược lại
        self.move_y = [0, -1, 1, 0]
        self.visited = [[False for _ in range(len(matrix))] for _ in range(len(matrix))]
        self.min_distance = float('inf')

    def is_valid(self, row, col):
        # Kiểm tra xem ô có hợp lệ để di chuyển không.
        if row < 0 or row >= len(self.matrix):
            return False

        if col < 0 or col >= len(self.matrix[0]):
            return False

        if self.matrix[row][col] == 0:  # 0 đại diện cho tường
            return False

        if self.visited[row][col]:
            return False

        return True

    def search(self, i, j, destination_x, destination_y):
        # Tìm kiếm đường đi ngắn nhất từ điểm xuất phát đến điểm đích bằng thuật toán BFS.

        # Đánh dấu điểm xuất phát đã được ghé thăm và thêm nó vào hàng đợi.
        self.visited[i][j] = True
        queue = deque()
        queue.append((i, j, 0))

        while queue:
            # Lấy thông tin từ đỉnh hàng đợi.
            (i, j, dist) = queue.popleft()

            # Nếu đến điểm đích, cập nhật khoảng cách ngắn nhất và kết thúc.
            if i == destination_x and j == destination_y:
                self.min_distance = dist
                break

            # Duyệt qua tất cả các hướng di chuyển.
            for move in range(len(self.move_x)):
                next_x = i + self.move_x[move]
                next_y = j + self.move_y[move]

                # Nếu ô tiếp theo là hợp lệ, đánh dấu đã ghé thăm và thêm vào hàng đợi.
                if self.is_valid(next_x, next_y):
                    self.visited[next_x][next_y] = True
                    queue.append((next_x, next_y, dist + 1))

    def show_result(self):
        # Hiển thị kết quả: khoảng cách ngắn nhất hoặc thông báo nếu không có đường đi khả dụng.
        if self.min_distance != float('inf'):
            print("Đường đi ngắn nhất từ điểm xuất phát đến điểm đích:", self.min_distance)
        else:
            print("Không có đường đi khả dụng - Điểm đích không thể đạt được!")

if __name__ == '__main__':
    # Tạo một mê cung dưới dạng ma trận.
    m = [
        [1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [0, 0, 0, 1, 1]
    ]

    # Tạo một đối tượng MazeSolver và thực hiện tìm kiếm từ điểm xuất phát (0,0) đến điểm đích (4,4).
    maze_solver = MazeSolver(m)
    maze_solver.search(0, 0, 4, 4)

    # Hiển thị kết quả.
    maze_solver.show_result()

