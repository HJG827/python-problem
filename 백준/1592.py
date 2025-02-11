# """
# 영식이와 친구들

# 영식이와 친구들이 원형으로 모여서 시계방향으로 1부터 N까지 적혀있는 자리에 앉는다. 영식이와 친구들은 공 던지는 게임을 하기로 했다. 게임의 규칙은 다음과 같다.
# 일단 1번 자리에 앉은 사람이 공을 받는다. 그리고 나서 공을 다른 사람에게 던진다. 다시 공을 받은 사람은 다시 공을 던지고, 이를 계속 반복한다. 한 사람이 공을 M번 받았으면 게임은 끝난다. (지금 받은 공도 포함하여 센다.) 공을 M번보다 적게 받은 사람이 공을 던질 때, 현재 공을 받은 횟수가 홀수번이면 자기의 현재 위치에서 시계 방향으로 L번째 있는 사람에게, 짝수번이면 자기의 현재 위치에서 반시계 방향으로 L번째 있는 사람에게 공을 던진다.

# 입력
# 첫째 줄에 N, M, L이 입력으로 들어온다. N은 3보다 크거나 같고, 50보다 작거나 같은 자연수이고, M은 50보다 작거나 같은 자연수이다. L은 N-1보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 공을 몇 번 던지는지 횟수를 출력한다.

# 힌트
# 예제 1의 경우 일단 1번이 공을 잡는다. 1번은 공을 한 번 잡았기 때문에, 공을 3번에게 던진다. 3번은 공을 한 번 잡았기 때문에, 공을 5번에게 던진다. 5번은 2번에게 던지고, 2번은 4번에게 던진다. 4번은 1번에게 던진다. 1번은 이제 공을 두 번 잡았기 때문에, 공을 4번에게 던진다. 4번은 2번에게 던지고, 2번은 5번에게 던지고, 5번은 3번에게 던지고, 마지막으로 3번은 1번에게 던진다. 1번은 이제 공을 세 번 잡았기 때문에, 게임은 끝난다.

# 10 3 5

# 4

# """

N, M, L = map(int, input().split())

arr = [0] * N

arr[0] = 1

cnt = 0
i = 0

while M not in arr:

    if arr[i] % 2 == 1:
        next_i = i - L
        if not 0 <= next_i < N:
            while not 0 <= next_i < N:
                next_i += N
        arr[next_i] += 1

    else:
        next_i = i + L
        if not 0 <= next_i < N:
            while not 0 <= next_i < N:
                next_i -= N
        # print(next_i)
        arr[next_i] += 1

    i = next_i
    cnt += 1

print(cnt)
