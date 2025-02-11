T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A, B = [list(map(int, input().split())) for _ in range(N)]

    P = int(input())

    bus_stop = []
    for _ in range(P):
        bus_stop.append(int(input()))

    for i in range(N):
        for j in range(A[0], A[1]+1):
            count +=


    print(f'#{tc} {A}')