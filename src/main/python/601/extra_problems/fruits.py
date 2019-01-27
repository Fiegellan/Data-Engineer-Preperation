class FruitSalad():
    fruits = ['melons', 'pineapples']
    servings = 4

    def __init__(self,ingredients = ['melons', 'pineapples'], used = 0):
        self.fruits = ingredients
        self.servings = self.servings - used

    def __str__(self):
        return str(self.servings)+' servings of fruit salad with ' + str(self.fruits)

    def add(self,a):
        self.fruits = self.fruits + a

    def serve(self):
        if self.servings>0:
            self.servings = self.servings-1
            return 'enjoy'
        else:
            return 'sorry'

a = FruitSalad(['bananas', 'apples'],2)
print a.fruits
a.add(['melons', 'pineapples'])

print a.serve()
print a.serve()
print a.serve()
print a.serve()
print a.serve()
