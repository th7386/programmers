# 가운데 글자 가져오기

def solution(s):
    mid = int(len(s) / 2)
    if len(s) % 2 != 0:
        return s[mid]
    return s[mid - 1:mid + 1]


# 다른 풀이
#
# def string_middle(str):
#     return str[(len(str)-1)//2 : len(str)//2 + 1]
