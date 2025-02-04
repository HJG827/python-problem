# 알파벳을 숫자로 변환
# 입력
# ABCDEFGHIJKLMNOPQRSTUVWXYZ

# 출력
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26

text = input()
number_lst = []

for char in text:
    number = ord(char)-64
    number_lst.append(number)
print(*number_lst)