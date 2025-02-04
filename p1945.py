# 간단한 소인수분해

# N=2a x 3b x 5c x 7d x 11e
# 이때 a, b, c, d, e?

# 입력
# 10  
# 6791400
# 1646400
# 1425600
# 8575
# 185625
# 6480
# 1185408
# 6561
# 25
# # 330750
 
# 출력
# #1 3 2 2 3 1
# #2 6 1 2 3 0
# #3 6 4 2 0 1
# #4 0 0 2 3 0
# #5 0 3 4 0 1
# #6 4 4 1 0 0
# #7 7 3 0 3 0
# #8 0 8 0 0 0
# #9 0 0 2 0 0
# #10 1 3 3 2 0


N = int(input())
primes = [2,3,5,7,11]

for i in range(1, N+1):
    number = int(input())
    prime_count = []


    for prime in primes:
        count = 0
        while number%prime==0:
            number = number//prime
            count += 1
        prime_count.append(count)    

    print(f'#{i}', *prime_count)