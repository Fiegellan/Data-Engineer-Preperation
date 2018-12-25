answer = []
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.nestedList = nestedList

    def next(self,a,b,c):
        """
        :rtype: int
        """
        global answer
        if b > 0 and c is True:
            for i in a:
                answer.append(i)
        elif b == 0 and c is True:
            answer.append(a)
        elif c is False:
            print answer

    def hasNext(self):
        """
        :rtype: bool
        """
        i = 0
        while i in range(0,len(self.nestedList)+1):
            if i < len(self.nestedList) and type(self.nestedList[i]) is list:
                self.next(self.nestedList[i], len(self.nestedList[i]), True)
                i += 1
            elif i < len(self.nestedList) and type(self.nestedList[i]) is int:
                self.next(self.nestedList[i], 0, True)
                i += 1
            else:
                self.next(0, 0, False)
                i+=1

def main():
    a = NestedIterator([[1,1],2,[1,1],[1,2,3,4]])
    print a.hasNext()


if __name__ == '__main__':
    main()
