class DevelopmentTeam:
    __junior = []
    __senior = []

    def add_junior(self, *args):
        [self.__junior.append((elem, "junior")) for elem in args]

    def add_senior(self, *args):
        [self.__senior.append((elem, "senior")) for elem in args]

    def __iter__(self):
        yield from self.__junior
        yield from self.__senior


# beegeek = DevelopmentTeam()

# beegeek.add_junior('Timur')
# beegeek.add_junior('Arthur', 'Valery')
# beegeek.add_senior('Gvido')
# print(*beegeek, sep='\n')

beegeek = DevelopmentTeam()

beegeek.add_junior("Timur")
beegeek.add_junior("Arthur", "Valery")
print(*beegeek, sep="\n")
