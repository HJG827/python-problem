# 2058. 자릿수 더하기

# 하나의 자연수를 입력 받아 각 자릿수의 합을 계산하는 프로그램을 작성하라.
# [제약 사항]
# 자연수 N은 1부터 9999까지의 자연수이다. (1 ≤ N ≤ 9999)

# [입력]
# 입력으로 자연수 N이 주어진다.
# 6789

# [출력]
# 각 자릿수의 합을 출력한다.
# 30

number = int(input())
digits = [int(digit) for digit in str(number)]

# digit_sum = sum(int(digits))
print(sum(digits))