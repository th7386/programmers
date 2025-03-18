# 나누어 떨어지는 숫자 배열

def solution(arr, divisor):
    answer = []

    for i in arr:
        if i % divisor == 0:
            answer.append(i)

    if len(answer) == 0:
        answer.append(-1)

    return sorted(answer)


# 다른 풀이
#
# def solution(arr, divisor):
#     arr = [x for x in arr if x % divisor == 0];
#     arr.sort();
#     return arr if len(arr) != 0 else [-1];

# def solution(arr, divisor):
#     return sorted([n for n in arr if n%divisor == 0]) or [-1]
