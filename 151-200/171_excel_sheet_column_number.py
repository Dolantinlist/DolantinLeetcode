def titleToNumber(s):
    rlt = 0
    bench = ord('A')
    for ch in s:
        tmp = ord(ch) - bench + 1
        rlt = rlt*26 + tmp
    return rlt
print(titleToNumber('AB'))