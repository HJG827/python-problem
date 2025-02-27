# 진기의 최고급 붕어빵
'''
4
2 2 2
3 4
2 2 2
1 2
2 2 1
4 2
2 2 1
3 2


#1 Possible
#2 Impossible
#3 Possible
#4 Impossible
# '''

def sell_taiyaki(N, M, K):
    taiyaki = 0
    for i in range(N):
        taiyaki = time[i] // M * K
        if taiyaki < i + 1:
            return 'Impossible'
    return 'Possible'


T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    time = list(map(int, input().split()))
    time.sort()
    result = sell_taiyaki(N, M, K)
    print(f'#{tc} {result}')