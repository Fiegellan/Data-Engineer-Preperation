def isSubstring(a,b):
    if a in b: return True
    else: return False

# print isSubstring('foo','barfoobar')
def extractTags(a):
    b = []
    start = 0
    for i,g in enumerate(a):
        if g =='[':
            start = i+1
        if g ==']':
            b.append(a[start:i])
            start = 0
    return b

print extractTags('[fizz] thing [/fizz] fuzz [zip]')