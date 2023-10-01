""" interview 1
def reverse(nums):

    start_index=0

    end_index=len(nums)-1

    while end_index > start_index:

        nums[start_index],nums[end_index]=nums[end_index],nums[start_index]
        start_index=start_index + 1
        end_index = end_index - 1


if _name_ =='_main_':

    n=[1,2,3,4]
    reverse(n)
    print(n)
"""
""" interview 2
def is_palindrome(s):
    # Loại bỏ các khoảng trắng và chuyển thành chữ thường
    s = s.replace(" ", "").lower()
    
    # Đặt con trỏ ở đầu và cuối chuỗi
    left = 0
    right = len(s) - 1
    
    while left < right:
        # So sánh ký tự tại vị trí left và right
        if s[left] != s[right]:
            return False
        # Di chuyển con trỏ
        left += 1
        right -= 1
    
    return True

# Kiểm tra chuỗi đối xứng
print(is_palindrome("abcba"))  # True
print(is_palindrome("anhna"))  # True
print(is_palindrome("anhthao"))  # False
"""
"""interview 3
def are_lists_equivalent(list1, list2):
    return sorted(list1) == sorted(list2)

# Kiểm tra hàm với ví dụ
list1 = [1, 2, 3]
list2 = [3, 2, 1]

if are_lists_equivalent(list1, list2):
    print("Hai danh sách tương đương.")
else:
    print("Hai danh sách không tương đương.")
"""
""" interview 4
def are_anagrams(word1, word2):
    # Sắp xếp các ký tự trong word1 và word2
    sorted_word1 = sorted(word1)
    sorted_word2 = sorted(word2)
    
    # So sánh các từ đã sắp xếp
    return sorted_word1 == sorted_word2

# Kiểm tra hàm
print(are_anagrams('listen', 'silent'))   
print(are_anagrams('triangle', 'integral')) 
print(are_anagrams('hello', 'world'))
"""
""" interview 5
def find_duplicates(arr):
    # Tạo một danh sách để lưu trữ các giá trị đã kiểm tra
    checked_values = []
    
    # Tạo một danh sách để lưu trữ các giá trị trùng lặp
    duplicates = []
    
    # Lặp qua từng phần tử trong mảng
    for num in arr:
        # Kiểm tra xem phần tử đã tồn tại trong danh sách đã kiểm tra hay chưa
        if num in checked_values:
            # Nếu đã tồn tại, thêm nó vào danh sách các giá trị trùng lặp
            if num not in duplicates:
                duplicates.append(num)
        else:
            # Nếu chưa tồn tại, thêm nó vào danh sách để kiểm tra tiếp
            checked_values.append(num)
    
    return duplicates

# Kiểm tra hàm với một ví dụ
arr = [1, 3, 3, 5]
result = find_duplicates(arr)
print(result)
"""