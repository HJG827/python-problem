
# 3. 카운팅 정렬

def CountingSort(arr, k):

    count_lst = [0] * (k+1)
    sort_lst = [0] * len(arr)

    for i in range(len(arr)):
        count_lst[arr[i]] += 1

    for j in range(1, k+1):
        count_lst[j] += count_lst[j-1]

    for m in range(len(arr)-1, -1, -1):
        count_lst[arr[m]] -= 1
        sort_lst[count_lst[arr[m]]] = arr[m]

    return sort_lst


arrs = [2, 3, 1, 8, 45]

print(CountingSort(arrs, max(arrs)))