# 간단한 N의 약수
# 정수 N의 약수를 오름차순으로 출력

# 입력
# 10

# 출력
# 1 2 5 10


N = int(input())

num = []
for i in range(1,N+1):
    
    if N % i ==0:
        num.append(i)
    
print(*num)