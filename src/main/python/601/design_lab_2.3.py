# Take aways
# Always return the type of the class, don't return the a different type
# If you change the type you can't layer functions on each other
# __str__ creates the string version of the class, while __add__ is the default add and __mul__ is the default multiplier
class V2():
    def __init__(self, a, b):
        self.vect = [a, b]

    def __str__(self):
        return str(self.vect)

    def __add__(self, v):
        return self.add(v)

    def __mul__(self,v):
        return self.mul(v)

    def getX(self):
        return self.vect[0]

    def getY(self):
        return self.vect[1]

    def mul(self,z):
        return V2(self.getX()*z, self.getY()*z)

    def add(self,a):
        return V2(self.getX() + a.getX(), self.getY() + a.getY())

v = V2(1.0,2.0)
print v
g = V2(2.2,3.3)
print v.getX()
print v.getY()
print v + g
print v*2
print v.mul(-1)
print v.add(g).mul(-1)
print v.add(g).mul(-1).add(v).add(g)*6
