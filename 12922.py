# 수박수박수박수박수박수?

def solution(n):
    if n % 2 == 0:
        return '수박' * int(n / 2)
    return '수박' * int(n/2) + '수'


# 다른 풀이
#
# def water_melon(n):
#     str = "수박"*n
#     return str[:n]