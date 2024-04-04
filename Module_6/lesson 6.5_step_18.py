class TreeBuilder:
    def __init__(self) -> None:
        self.node = {}
        self.level = 0

    def __enter__(self):
        self.node.setdefault(self.level, [])
        self.level += 1
    
    def __exit__(self, *args):
        tmp = self.node[self.level]
        self.node[self.level] = []
        self.level -= 1
        if tmp:
            self.node[self.level].append(tmp)


    def add(self, sheet):
        self.node.setdefault(self.level, []).append(sheet)

    def structure(self):
        if self.node:
            return self.node[0]
        return []

# class TreeBuilder:
#     def __init__(self) -> None:
#         self.node = [[]]

#     def __enter__(self):
#         self.node.append([])

#     def __exit__(self, *args):
#         if self.node[-1]:
#             self.node[-2].append(self.node[-1])
#         self.node.pop()

#     def add(self, sheet):
#         self.node[-1].append(sheet)

#     def structure(self):
#         return self.node[-1]

    # [[1, [2, [3, [4]]]], 5]
# INPUT DATA:

# TEST_1:
tree = TreeBuilder()
print(tree.structure())

tree.add('1st')
print(tree.structure())

with tree:
    tree.add('2nd')
    with tree:
        tree.add('3rd')
    tree.add('4th')
    with tree:
        pass
        
print(tree.structure())

# TEST_2:
tree = TreeBuilder()

tree.add('1st')

with tree:
    tree.add('2nd')
    with tree:
        tree.add('3rd')
        with tree:
            tree.add('4th')
            with tree:
                tree.add('5th')
    with tree:
        pass

tree.add('6th')
print(tree.structure())

# TEST_3:
tree = TreeBuilder()

with tree:
    tree.add(1)
    tree.add(2)
    with tree:
        tree.add(3)
        with tree:
            tree.add(4)
    with tree:
        tree.add(5)

print(tree.structure())

# TEST_4:
tree = TreeBuilder()

with tree:
    tree.add(1)
    with tree:
        tree.add(2)
        tree.add(3)
    with tree:
        pass

print(tree.structure())

# TEST_5:
tree = TreeBuilder()

tree.add(0)
print(tree.structure())

with tree:
    tree.add(1)
    with tree:
        tree.add(2)
        tree.add(3)
        with tree:
            tree.add(4)
    with tree:
        pass

print(tree.structure())

with tree:
    tree.add(5)
    with tree:
        tree.add(6)
    with tree:
        tree.add(7)
        with tree:
            tree.add(8)

print(tree.structure())

# TEST_6:
tree = TreeBuilder()

tree.add('root')
with tree:
    tree.add('first child')
    tree.add('second child')
    with tree:
        tree.add('grandchild')
    tree.add('bastard')
    with tree:
        pass
    tree.add('another bastard')

print(tree.structure())

# TEST_7:
tree = TreeBuilder()

tree.add('1st')

with tree:
    with tree:
        with tree:
            with tree:
                tree.add('5th')

print(tree.structure())

# TEST_8:
tree1 = TreeBuilder()
tree2 = TreeBuilder()

tree1.add('1st')

with tree1:
    tree1.add('2nd')
    with tree1:
        tree1.add('3rd')
    tree1.add('4th')
    with tree1:
        pass

print(tree1.structure())
print(tree2.structure())