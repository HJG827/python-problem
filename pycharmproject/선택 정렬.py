# 2. 선택 정렬

def SelectionSort(arr):
    N = len(arr)
    for i in range(N):
        min_idx = i
        for j in range(i, N):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]


arrs = [5, 1, 7, 54, 17]
SelectionSort(arrs)
print(arrs)