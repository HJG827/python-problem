# 1. 버블 정렬

def BubbleSort(arr):
    N = len(arr)

    for i in range(N-1, -1, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arrs = [1, 8, 145, 34, 5]
BubbleSort(arrs)
print(arrs)