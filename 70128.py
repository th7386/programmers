# 내적

def solution(a, b):
    answer = 0
    for i, j in zip(a, b):
        answer += i * j
    return answer


# 다른 풀이
#
# def solution(a, b):
#
#     return sum([x*y for x, y in zip(a,b)])