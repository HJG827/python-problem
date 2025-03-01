'''
빙고
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	25698	11808	9520	45.961%
문제
빙고 게임은 다음과 같은 방식으로 이루어진다.

먼저 아래와 같이 25개의 칸으로 이루어진 빙고판에 1부터 25까지 자연수를 한 칸에 하나씩 쓴다
다음은 사회자가 부르는 수를 차례로 지워나간다. 예를 들어 5, 10, 7이 불렸다면 이 세 수를 지운 뒤 빙고판의 모습은 다음과 같다.
차례로 수를 지워가다가 같은 가로줄, 세로줄 또는 대각선 위에 있는 5개의 모든 수가 지워지는 경우 그 줄에 선을 긋는다.

이러한 선이 세 개 이상 그어지는 순간 "빙고"라고 외치는데, 가장 먼저 외치는 사람이 게임의 승자가 된다.
철수는 친구들과 빙고 게임을 하고 있다. 철수가 빙고판에 쓴 수들과 사회자가 부르는 수의 순서가 주어질 때, 사회자가 몇 번째 수를 부른 후 철수가 "빙고"를 외치게 되는지를 출력하는 프로그램을 작성하시오.

입력
첫째 줄부터 다섯째 줄까지 빙고판에 쓰여진 수가 가장 위 가로줄부터 차례대로 한 줄에 다섯 개씩 빈 칸을 사이에 두고 주어진다. 여섯째 줄부터 열째 줄까지 사회자가 부르는 수가 차례대로 한 줄에 다섯 개씩 빈 칸을 사이에 두고 주어진다. 빙고판에 쓰여진 수와 사회자가 부르는 수는 각각 1부터 25까지의 수가 한 번씩 사용된다.

출력
첫째 줄에 사회자가 몇 번째 수를 부른 후 철수가 "빙고"를 외치게 되는지 출력한다.

예제 입력 1 
11 12 2 24 10
16 1 13 3 25
6 20 5 21 17
19 4 8 14 9
22 15 7 23 18
5 10 7 16 2
4 22 8 17 13
3 18 1 6 25
12 19 23 14 21
11 24 9 20 15
예제 출력 1 
15'''


def check_bingo(arr):
    count = 0
    for i in range(5):
        if all(arr[i][j] for j in range(5)):
            count += 1
        if all(arr[j][i] for j in range(5)):
            count += 1
    if all(arr[j][j] for j in range(5)):
        count += 1
    if all(arr[j][4-j] for j in range(5)):
        count += 1
    return count

def my_bingo(bingo, announce):
    mark = [[0]*5 for _ in range(5)]
    for i in range(len(announce)):
        number = announce[i]
        for r in range(5):
            for c in range(5):
                if number == bingo[r][c]:
                    mark[r][c] = 1
                    break

        if check_bingo(mark) >= 3:
            return i

bingo = [list(map(int, input().split())) for _ in range(5)]
announce = [0]
turn = 0

for _ in range(5):
    announce.extend(list(map(int,input().split())))


print(my_bingo(bingo, announce))