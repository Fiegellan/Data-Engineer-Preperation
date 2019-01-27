class Staff601():
    # class attributes, always have same attributes
    room = '34-501'
    def __init__(self, greeting = 'hi'): #always have self and what other object you want to be created
        self.greeting = greeting

    def sayHi(self):
        # self say i am talking about myself
        # when kpugh calls sayHi it - reference to what calls it
        # IE self substitutes what ever instance called the method for it
        print self.greeting

print type(Staff601)
kpugh = Staff601('hello') # treats it like a call and instantiates
print kpugh.room
kpugh.sayHi()
fiegelc = Staff601()
fiegelc.sayHi()