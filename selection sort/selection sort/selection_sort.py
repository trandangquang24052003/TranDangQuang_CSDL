"""
# Bài 4
def seclectionsort(A):               # cố định danh sách a 
    n= len(A)                        # n gán bằng độ dài danh sách của A
    for i in range(n-1):             # vòng lặp xét từ i đến gần cuối (áp chót)
        position = i                 # gán biến này bằng biến kia 
        for j in range(i+1, n):      # gán j = i+1 và chạy trong khoảng i+1 đến n
            if A[j] < A[position]:   # nếu giá trị j bé hơn position 
                position =j          # gán position bằng j
        temp = A[i]                  # đổi vị trí và tiếp tục xét tiếp 
        A[i] = A[position]
        A[position] = temp

A = [3,5,8,9,6,2]
print('Original Array:', A)
seclectionsort(A)
print('Sorted Array:', A)
"""
""" 
# Bài 8
def bubblesort(A): # Hàm bubblesort chính, sắp xếp mảng A
    n = len(A) # Lấy độ dài của mảng
    for passes in range (n-1,0,-1):  # Vòng lặp ngoài chạy từ n-1 đến 0, giảm dần mỗi lần. Đại diện cho số lần đi qua danh sách.
        for i in range (passes):    # Vòng lặp trong chạy từ 0 đến passes. Đối với mỗi lần đi qua, nó kiểm tra từng cặp phần tử liền kề trong danh sách.
            if A[i] > A[i+1]: # Nếu phần tử hiện tại A[i] lớn hơn phần tử tiếp theo A[i+1], nó sẽ hoán đổi chúng.
                temp =A[i]
                A[i] = A[i+1]
                A[i+1] = temp

A = [3,5,8,9,6,2]
print ('Original Array:' ,A)
bubblesort(A)
print ('Sort Array:' ,A)
"""
"""# Bài 6
def insertionsort(A):  # Định nghĩa hàm sắp xếp chèn với đầu vào là một danh sách A
    n= len(A)  # Lấy độ dài của danh sách A
    for i in range(1,n):  # Duyệt qua từng phần tử của danh sách, bắt đầu từ phần tử thứ hai
        cvalue = A[i]  # Lưu giá trị hiện tại cần được chèn vào phần đã sắp xếp của danh sách
        position = i  # Lưu vị trí hiện tại của giá trị cvalue trong danh sách
        while position > 0 and A[ position -1 ] > cvalue:  # Nếu vị trí hiện tại lớn hơn 0 và giá trị tại vị trí trước đó lớn hơn giá trị cvalue
            A[position] = A[ position -1 ]  # Di chuyển giá trị lớn hơn về sau một vị trí
            position = position - 1  # Giảm vị trí hiện tại đi 1
        A[position] = cvalue  # Chèn giá trị cvalue vào vị trí phù hợp

A = [3,5,8,9,6,2]  # Khởi tạo danh sách A cần sắp xếp
print('Original Array:', A)  # In ra danh sách ban đầu
insertionsort(A)  # Gọi hàm sắp xếp chèn với đầu vào là danh sách A
print('Sorted Array:', A)  # In ra danh sách sau khi đã sắp xếp
"""
""" # Bài 23
def radixsort(A):                           #định nghĩa một hàm có tên là radixsort(), nhận vào một mảng A.
    n = len(A)                              #tính độ dài của mảng A.
    maxelement = max(A)                     #tìm phần tử lớn nhất trong mảng A
    digits = len (str(maxelement))          #tính số chữ số của phần tử lớn nhất trong mảng A.
    l = []                                  #khởi tạo một danh sách l trống.
    bins = [l] * 10                         #khởi tạo một danh sách bins chứa 10 danh sách trống.
    for i in range (digits):                #bắt đầu một vòng lặp for lặp digits lần.
        for j in range (n):                 #bắt đầu một vòng lặp for lặp n lần.
            e = int((A[j]) / pow(10,i)) % 10    #Dòng này tính chữ số thứ i của phần tử thứ j trong mảng A.
            if len(bins[e]) > 0:
                bins[e].append(A[j])
            else:
                bins[e] = [A[j]]
                #kiểm tra xem danh sách bins[e] có trống hay không.
                #Nếu danh sách bins[e] không trống, thì phần tử thứ j của mảng A sẽ được thêm vào danh sách bins[e].
                #Nếu danh sách bins[e] trống, thì một danh sách mới sẽ được tạo ra và thêm phần tử thứ j của mảng A vào danh sách mới đó.
        k = 0
        for x in range(10):
                #khởi tạo một biến k bằng 0 và bắt đầu một vòng lặp for lặp 10 lần.
            if len(bins[x]) > 0:
                for y in range(len(bins[x])):
                    A[k] = bins[x].pop(0)
                    k = k+1
                    #kiểm tra xem danh sách bins[x] có trống hay không.
                    #Nếu danh sách bins[x] không trống, thì tất cả các phần tử trong danh sách bins[x] sẽ được thêm vào mảng A theo thứ tự, bắt đầu từ vị trí k.
                    #Biến k sẽ được tăng lên 1 sau mỗi lần thêm một phần tử vào mảng A.
A = [28,115,435,650,760,54]
print('Original Array:', A)
radixsort(A)
print('Sorted Array:' ,A)
"""
""" # Bài 15
def mergesort(A, left, right):
    # Hàm mergesort nhận vào mảng A cùng với chỉ số bắt đầu (left) và chỉ số kết thúc (right) của phạm vi cần sắp xếp.

    if left < right:
        # Kiểm tra xem phạm vi cần sắp xếp có nhiều hơn một phần tử không (tức là left < right).

        mid = (left + right) // 2
        # Tìm giữa của phạm vi để chia mảng thành hai nửa.

        mergesort(A, left, mid)
        # Gọi đệ quy để sắp xếp nửa bên trái của mảng.

        mergesort(A, mid + 1, right)
        # Gọi đệ quy để sắp xếp nửa bên phải của mảng.

        merge(A, left, mid, right)
        # Gộp hai nửa đã sắp xếp lại với nhau.

def merge(A, left, mid, right):
    # Hàm merge nhận vào mảng A và chỉ số bắt đầu (left), chỉ số giữa (mid), và chỉ số kết thúc (right) của phạm vi cần gộp.

    i = left
    j = mid + 1
    k = left
    # Khởi tạo các biến chỉ số.

    B = [0] * (right + 1)
    # Tạo một mảng tạm thời B để lưu kết quả gộp.

    while i <= mid and j <= right:
        # Lặp qua cả hai nửa của mảng và so sánh phần tử.

        if A[i] < A[j]:
            # So sánh phần tử từ nửa bên trái và nửa bên phải, chọn phần tử nhỏ hơn.
            B[k] = A[i]
            # Lưu phần tử nhỏ hơn vào mảng kết quả.
            i = i + 1
            # Di chuyển chỉ số i để xem phần tử tiếp theo trong nửa bên trái.

        else:
            B[k] = A[j]
            j = j + 1
        k = k + 1
        # Tương tự, lưu phần tử nhỏ hơn vào mảng kết quả và di chuyển chỉ số j hoặc k.

    while i <= mid:
        # Sao chép phần còn lại của nửa bên trái (nếu còn).
        B[k] = A[i]
        i = i + 1
        k = k + 1

    while j <= right:
        # Sao chép phần còn lại của nửa bên phải (nếu còn).
        B[k] = A[j]
        j = j + 1
        k = k + 1

    for x in range(left, right + 1):# Sao chép kết quả từ mảng tạm thời B vào mảng ban đầu A.
        A[x] = B[x]

A = [5, 6, 8, 9, 6, 2]
print("Original Array", A)
mergesort(A, 0, len(A) - 1)
print("Sorted Array", A)
"""
""" # bài 19
def quicksort(A, low, high): # Hàm quicksort chính, sắp xếp mảng A từ chỉ số low đến high
    if low < high:
        pi = partition(A, low, high) # Tìm chỉ số pivot sau khi phân chia
        quicksort(A, low, pi-1) # Đệ quy sắp xếp các phần tử trước và sau pivot
        quicksort(A,pi+1,high)

def partition(A, low, high): # Hàm phân chia mảng theo pivot    
    pivot = A[low]  # Chọn phần tử đầu tiên làm pivot
    i = low + 1
    j = high
    while True:
        while i <=j and A[i] <= pivot: # Nếu phần tử hiện tại nhỏ hơn hoặc bằng pivot thì tăng i
            i = i + 1
        while i <= j and A[j] > pivot:  # Nếu phần tử hiện tại lớn hơn pivot thì giảm j
            j = j - 1
        if i <= j:  # Nếu i nhỏ hơn hoặc bằng j thì hoán đổi vị trí của A[i] và A[j]
            A[i], A[j] = A[j], A[i] 
        else:
            break
    A[low], A[j] = A[j], A[low]  # Hoán đổi vị trí của pivot và A[j]
    return j

A = [3,5,8,9,6,2]
print('Original Array:', A)
quicksort(A, 0, len(A)-1)
print('Sorted Array:', A) 
"""
"""# Bài 21
def countsort(A):  # Định nghĩa hàm sắp xếp đếm với đầu vào là một danh sách A
    n = len (A)  # Lấy độ dài của danh sách A
    maxsize = max(A)  # Tìm giá trị lớn nhất trong danh sách A
    carray = [0] * (maxsize + 1)  # Khởi tạo một danh sách carray với kích thước bằng maxsize + 1, tất cả các phần tử đều bằng 0
    for i in range(n):  # Duyệt qua từng phần tử của danh sách A
        carray [A[i]] = carray[A[i]] + 1  # Tăng giá trị tại vị trí tương ứng trong carray lên 1
    i = 0
    j = 0
    while i < maxsize + 1 :  # Duyệt qua từng phần tử của carray
        if carray[i] > 0 :  # Nếu giá trị tại vị trí hiện tại lớn hơn 0
            A[j] = i   # Gán giá trị đó vào danh sách A
            j = j + 1
            carray[i] = carray[i] - 1   # Giảm giá trị tại vị trí hiện tại trong carray đi 1
        else:
            i = i + 1   # Nếu không, tăng i lên 1

A = [3,5,8,9,6,2,3,5,5]  # Khởi tạo danh sách A cần sắp xếp
print('Original Array:', A)  # In ra danh sách ban đầu
countsort(A)  # Gọi hàm sắp xếp đếm với đầu vào là danh sách A
print('Sorted Array:',A)   # In ra danh sách sau khi đã sắp xếp
"""
""" #Bài 10
def shellsort(A):                           #định nghĩa một hàm có tên là shellsort() với tham số đầu vào là một mảng A.
    n = len(A)                              #tính độ dài của mảng A và lưu trữ nó trong biến n.
    gap = n//2                              #tính toán khoảng cách ban đầu giữa các phần tử được so sánh, bằng với nửa độ dài của mảng A.
    while gap > 0:                          #bắt đầu một vòng lặp while lặp chừng nào khoảng cách gap còn lớn hơn 0.
        i = gap                             #khởi tạo một biến i bằng với khoảng cách gap.
        while i < n:                        #bắt đầu một vòng lặp while lặp chừng nào biến i còn nhỏ hơn độ dài của mảng A.
            temp = A[i]                     #lưu trữ giá trị của phần tử tại vị trí i của mảng A trong một biến tạm thời temp.
            j = i - gap                     #khởi tạo một biến j bằng với vị trí i trừ đi khoảng cách gap
            while j >= 0 and A[j] > temp:   # bắt đầu một vòng lặp while lặp chừng nào biến j còn lớn hơn hoặc bằng 0 và phần tử tại vị trí j của mảng A còn lớn hơn biến temp.
                A[j+gap] = A[j]             #di chuyển phần tử tại vị trí j của mảng A sang vị trí j + gap.
                j = j - gap                 #giảm giá trị của biến j đi khoảng cách gap.
            A[j + gap] = temp               #lưu trữ giá trị của biến temp vào vị trí j + gap của mảng A.
            i = i+1                         #tăng giá trị của biến i lên 1.
        gap = gap // 2                      #giảm giá trị của khoảng cách gap đi một nửa.

A = [3,5,8,9,6,2]
print('Original Array:', A)
shellsort(A)
print('sorted array: ' , A)
"""