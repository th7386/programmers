# 3진법 뒤집기

def solution(n):
    answer = ''

    while n != 0:
        rem = n % 3
        n = n // 3  # answer = [0, 0, 2, 1]
        answer += str(rem)

    return int(answer, 3)
