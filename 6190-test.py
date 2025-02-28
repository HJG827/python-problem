
def number_check(number):
    prev = 10
    while number:
        char = number % 10
        if char > prev:
            return 0
        prev = char
        number //= 10
    return 1

def number_check2(number):
    num_str = str(number)
    for i in range(len(num_str) -1):
        if ord(num_str[i]) > ord(num_str[i+1]):
            return 0
    return 1

print(number_check(2223334))
print(number_check2(2223334))