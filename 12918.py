# 문자열 다루기 기본

def solution(s):
    return True if (len(s) == 4 or len(s) == 6) and s.isdigit() == True else False
