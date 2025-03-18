# 콜라츠 추측

def solution(num):
    answer = 0
    for i in range(500):
        if num == 1:
            return answer
        if num % 2 == 0:
            num = num / 2
            answer += 1
        elif num % 2 != 0:
            num = 3 * num + 1
            answer += 1
    return -1


# 다른 풀이
#
# def collatz(num):
#     for i in range(500):
#         num = num / 2 if num % 2 == 0 else num * 3 + 1
#         if num == 1:
#             return i + 1
#     return -1
