'''
4
5 3
35 39
93 70
569 138

#1 10
#2 20
#3 123
#4 1175

'''

T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())

    arr = [[1] * n for _ in range(4)]
    for time in range(2, k+1):
        for i in range(4):
            for j in range(n):
                if (i+j+1) % time == 0:
                    arr[i][j] = (arr[i][j] + 1) % 2 

    result = 0

    for r in range(4):
        for c in range(n):
            if arr[r][c] == 1:
                result += 1

    print(f'#{tc} {result}')