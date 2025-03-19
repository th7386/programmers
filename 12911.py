# 다음 큰 숫자

def solution(n):
    answer = n + 1
    while True:
        if str(bin(n)).count('1') == str(bin(answer)).count('1'):
            return answer
        answer += 1
