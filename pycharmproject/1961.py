'''
1961. 숫자 배열 회전 D2

N x N 행렬이 주어질 때,
시계 방향으로 90도, 180도, 270도 회전한 모양을 출력하라.

[제약 사항]
N은 3 이상 7 이하이다.

[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에 N이 주어지고,
다음 N 줄에는 N x N 행렬이 주어진다.

[출력]
출력의 첫 줄은 '#t'로 시작하고,
다음 N줄에 걸쳐서 90도, 180도, 270도 회전한 모양을 출력한다.
입력과는 달리 출력에서는 회전한 모양 사이에만 공백이 존재함에 유의하라.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

입력
10
3
1 2 3
4 5 6
7 8 9
6
6 9 4 7 0 5
8 9 9 2 6 5
6 8 5 4 9 8
2 2 7 7 8 4
7 5 1 9 7 9
8 9 3 9 7 6
…

출력
#1
741 987 369
852 654 258
963 321 147
#2
872686 679398 558496
952899 979157 069877
317594 487722 724799
997427 894586 495713
778960 562998 998259
694855 507496 686278
…

'''

def rotate_90(N, arr):

    result = []
    for c in range(N):
        number = []
        for r in range(N-1, -1, -1):
            number.append(arr[r][c])
        result.append(number)

    return result

def rotate_180(N,arr):
    return rotate_90(N,rotate_90(N,arr))

def rotate_270(N,arr):
    return rotate_180(N,rotate_90(N,arr))

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    print(f'#{tc}')
    for i in range(n):
        result_90 = ''.join(map(str, rotate_90(n,a)[i]))
        result_180 = ''.join(map(str, rotate_180(n, a)[i]))
        result_270 = ''.join(map(str, rotate_270(n, a)[i]))
        print(result_90, result_180, result_270)
