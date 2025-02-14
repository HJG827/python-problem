# def fibo(n):
#     if n < 2:
#         return n
#     else:
#         return fibo(n-1) + fibo(n-2)
#
#
# def fibo1(n):
#     global memo
#     if n >= 2 and memo[n] == 0:
#         memo[n] = fibo1(n-1) + fibo1(n-2)
#     return memo(n)
#
# memo = [0] * (n+1)
# memo[0] = 0
# memo[1] = 1
#
# def fibo2(n):
#     f = [0] * (n + 1)
#     f[0] = 0
#     f[1] = 1
#     for i in range(2, n + 1):
#         f[i] = f[i-1] + f[i-2]
#
#     return f[n]


'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''



def dfs(v, N):
    visited = [0] * (N + 1)
    stack = []

    while True:
        if visited[v] == 0:
            visited[v] = 1
            stack.append(v)
            print(v)

        for w in adj_list[v]:
            if visited[w] == 0:
                stack.append(v)
                v = w
                break

        else:
            if stack:
                v = stack.pop()
            else:
                break

V, E = map(int, input(). split())
graph = list(map(int, input(). split()))
adj_list = [[] for _ in range(V + 1)]

for i in range(E):
    v, w = graph[i*2], graph[i*2 + 1]

    adj_list[v].append(w)
    adj_list[w].append(v)

dfs(1, V)