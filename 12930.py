# 이상한 문자 만들기

def solution(s):
    answer = []
    list_s = s.split(' ')

    for word in list_s:
        s = ""
        for i in range(0, len(word)):
            s += word[i].upper() if i % 2 == 0 else word[i].lower()

        answer.append(s)

    return ' '.join(answer)
