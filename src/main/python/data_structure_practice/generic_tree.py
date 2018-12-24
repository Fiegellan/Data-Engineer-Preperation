class Tree(object):
    # "Generic tree node."
    def __init__(self, name='root', children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)

    def __repr__(self):
        return self.name

    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)

    def sum_tree(Tree):
        sum = {}
        sum[0] = int(str(Tree))
        a = 0
        level = 1
        for i in Tree.children:
            a = a + int(str(i))
        sum[level] = a
        return sum

    @staticmethod
    def traverse_tree(Tree, Level = 0, sum=None):
        if sum == None:
            sum = {}
        if Level in sum.keys():
            sum[Level] += int(str(Tree))
        else:
            sum[Level] = int(str(Tree))

        Level = Level + 1
        for i in Tree.children:
            if i is not None:
                Tree.traverse_tree(i, Level, sum)
            else:
                pass
        return sum


t = Tree('1', [Tree('3',[Tree('4',[Tree('7')])]),
               Tree('2',[Tree('7'),Tree('10',[Tree('15')])]),
               Tree('10', [Tree('2')]),
               Tree('15', [Tree('5',[Tree('3')]),Tree('10'),Tree('6',[Tree('3'),Tree('2')])]),
               Tree('18',[Tree('6')])])


a = Tree.traverse_tree(t)

print type(a)

for key, value in a.iteritems():
    print "for level: " + str(key) + " the summation is: " + str(value)
