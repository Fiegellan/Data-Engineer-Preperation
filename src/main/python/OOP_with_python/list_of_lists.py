class list_on_list:

    def __init__(self, list):
        """
        First take the input list and sort it based on the commandsand have it sent to the various correct locations
        """
        self.list = list

    def hasNext(self,k):
        print self.list
        if len(self.list) > k:
            return True
        else:
            return False

    def next(self,k):
        if len(self.list) >k:
            return self.list[k+1]
        else:
            return 'error'


    def remove(self):
        if len(self.list) >k:
            a
            list_on_list
        else:
            return 'error'




def main():
    a = list_on_list([1,2,3])
    print a.hasNext(2)
    print a.next(1)


if __name__ == '__main__':
    main()
