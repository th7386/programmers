# 하샤드 수

def solution(x):
    arr = list(str(x))
    sum = 0

    for i in range(len(arr)):
        sum += int(arr[i])
        if x % sum == 0:
            answer = True
        else:
            answer = False

    return answer


# 간결한 풀이
# def solution(n):
#     return n % sum([int(c) for c in str(n)]) == 0
