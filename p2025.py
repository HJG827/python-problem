# 2025. N줄덧셈
# 1부터 주어진 숫자만큼 모두 더한 값을 출력하시오.
# 단, 주어질 숫자는 10000을 넘지 않는다.

N = int(input())
# for i in range(N):
#     i+=1
#     result = sum(i)
# print(result)

result=0
for i in range(1,N+1):
    result += i
print(result)