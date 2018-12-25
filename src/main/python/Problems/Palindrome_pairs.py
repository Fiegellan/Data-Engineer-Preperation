

def palindrome_pairs(list):
    answer = []
    for i,x in enumerate(list):
        print x, x[::-1]
        if x[::-1] in list:
            if i != list.index(x[::-1]):
                # print 'index 1', i, 'index 2', list.index(x[::-1])
                a = (i, list.index(x[::-1]))
                answer.append(a)

    return set((a,b) if a<=b else (b,a) for a,b in answer)



print palindrome_pairs(['ii','12', '21'])