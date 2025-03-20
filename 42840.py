# 모의고사

def solution(answers):
    res = []
    num1 = [1, 2, 3, 4, 5]
    num2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]

    for idx, answer in enumerate(answers):
        if answer == num1[idx % len(num1)]:
            score[0] += 1
        if answer == num2[idx % len(num2)]:
            score[1] += 1
        if answer == num3[idx % len(num3)]:
            score[2] += 1
    for idx, s in enumerate(score):
        if s == max(score):
            res.append(idx + 1)

    return res
