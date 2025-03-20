# 콜라 문제

def solution(a, b, n):
    answer = lambda a, b, n: max(n - b, 0) // (a - b) * b
    return answer(a, b, n)


# 다른 풀이
#
# def solution(a, b, n):
#     answer = 0
#     while n >= a:
#         answer += (n // a) * b
#         n = (n // a) * b + (n % a)
#     return answer