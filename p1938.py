# 아주 간단한 계산기
# 입력 받기 (두 개의 숫자가 공백을 띄고 주어짐)


number  = list(map(int,input().split()))
# input() : 주어진 입력 문자열 "8 3" 입력받기
# input().split() : 문자열을 공백 단위로 쪼갬 ["8", "3"]
# map, int : 각각의 문자열을 숫자로 바꿈
# list로 모으기 : [8, 3]

a, b = number # 리스트의 각 원소를 꺼내서 a, b에 저장

print(a+b)
print(a-b)
print(a*b)
print(a//b)