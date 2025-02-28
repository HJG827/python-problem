'''
5
5 1 4
3 5 5 4 5
6 2 6
5 3 3 5 5 1
7 1 6
3 3 5 2 5 1 2
8 1 7
3 1 1 2 2 5 3 5
10 1 6
4 4 2 4 5 2 5 3 5 5

#1 2
#2 -1
#3 1
#4 2
#5 1
'''

'''
    result = 0
    classroom = []  
    now_student = 0
    for i in range(K+2):
        if students[i] > max_class:
            result = -1
            break
        if now_student < min_class:
            now_student += students[i]
            if now_student > max_class:
                result = -1
                break
        else:
            if now_student:
                classroom.append(now_student)
                now_student = students[i]
    # print(classroom)
    
    if len(classroom) < 3:
        result = -1
    elif len(classroom) == 3:
        result = max(classroom)-min(classroom)
    else:
        for i in range(len(classroom) - 2):
            if classroom[i] + classroom[i+1] <= max_class:
                classroom[i] += classroom[i+1]
                classroom.pop(i+1)
            if len(classroom) == 3 and result != -1:
                result = max(classroom) - min(classroom)
                break
            else:
                result = -1

                '''

T = int(input())

for tc in range(1, T+1):
    N, min_class, max_class = map(int, input().split())
    score = list(map(int, input().split()))
    K = max(score)

    students = [0] * (K + 2)

    for a in range(N):
        students[score[a]] += 1
        pass

    
    result = -1
    
    for score1 in range(K+1):
        for score2 in range(score1+1, K+1):
            class1 = sum(students[i] for i in range(score1))
            class2 = sum(students[j] for j in range(score1, score2))
            class3 = sum(students[k] for k in range(score2, K+1))
            if (min_class <= class1 <= max_class
                and min_class <= class2 <= max_class
                and min_class <= class3 <= max_class):
                result = max(class1, class2, class3) - min(class1, class2, class3)
                break
            continue


    print(f'#{tc} {result}')
