def solution(s):
    alpha = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    answer = 0
    stack = []
    result = ''
    for i in s:
        if i.isalpha():
            stack.append(i)
            if ''.join(map(str,stack)) in alpha:
                result += str(alpha.index(str(''.join(map(str,stack)))))
                stack = []
            else:
                continue
        else:
            result += i
    answer = int(result)
    return answer