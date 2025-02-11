# def seq_search(arr, n, key):
#     for i in range(n):
#         if arr[i] == key:
#             return i
#     return -1
#
#
arr = [4, 9, 11, 23, 2, 19, 7]
#
# print(seq_search(a, len(a), 19))

# def selectionSort(a, N):
#     for i in range(N-1):
#         min_idx = i
#         for j in range(i+1, N):
#             if a[min_idx] > a[j]:
#                 min_idx = j
#         a[i], a[min_idx] = a[min_idx], a[i]
#

# def select(arr, k):
#     for i in range(0, k):
#         min_idx = i
#         for j in range(i+1, len(arr)):
#             if arr[min_idx] > arr[j]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#     return arr[k-1]

def binarySearch(a, N, key):
    start = 0
    end = N-1
    while start <= end:
        middle = (start + end) // 2
        if a[middle] == key:  # 검색 성공
            return middle
        elif a[middle] > key:  # 찾는 값보다 크면
            end = middle - 1   # 왼쪽 구간 선택
        else:                  # 찾는 값보다 작으면
            start = middle + 1  # 오른쪽 구간 선택
    return -1                   # 검색 실패

print(binarySearch(arr, len(arr), 1))