def solution(s):
    if s.lower().count('p') == s.lower().count('y'):
        return True
    elif s.lower().count('p') != s.lower().count('y'):
        return False
    else:
        return True

    