# 푸드 파이트 대회

def solution(food):
    answer = ''
    for i in range(1, len(food)):
        answer += str(i) * (food[i] // 2)

    return answer + '0' + answer[::-1]

# [1, 3, 4, 6] 물 1개 1번음식 2개 2번음식 4개 3번음식 6개 122333 + 0 + 333221
