from re import T


class WriteSpy:
    def __init__(self, file1, file2, to_close=False) -> None:
        self.file1 = file1
        self.file2 = file2
        self.to_close = to_close

    def __enter__(self):
        return self

    def __exit__(self, *args):
        if self.to_close:
            self.file1.close()
            self.file2.close()
        # return False
        # self.to_close = True

    def write(self, text):
        self.file1.write(text)
        self.file2.write(text)

    def close(self):
        self.file1.close()
        self.file2.close()

    def writable(self):
        try:
            if any([self.file1.writable(), self.file2.writable()]):
                return True
        except ValueError:
            return False
        # return self.file1.mode == self.file1.mode == "w"

    def closed(self):
        if self.file1.close() and self.file2.close:
            return False
        return True


# f1 = open('file1.txt', mode='w')
# f2 = open('file2.txt', mode='w')

# with WriteSpy(f1, f2, to_close=True) as combined:
#     combined.write('You shall seal the blinding light that plagues their dreams\n')
#     combined.write('You are the Vessel\n')
#     combined.write('You are the Hollow Knight')

# print(f1.closed, f2.closed)

# with open('file1.txt') as file1, open('file2.txt') as file2:
#     print(file1.read())
#     print(file2.read())


# f1 = open('file1.txt', mode='w')
# f2 = open('file2.txt', mode='w')

# with WriteSpy(f1, f2, to_close=True) as combined:
#     print(combined.writable())

# f1 = open('file1.txt')
# f2 = open('file2.txt')

# with WriteSpy(f1, f2, to_close=True) as combined:
#     print(combined.writable())


f1 = open("file1.txt", mode="w")
f2 = open("file2.txt", mode="w")

with WriteSpy(f1, f2, to_close=True) as combined:
    print(combined.closed())
    f1.close()
    print(combined.closed())
    f2.close()
    print(combined.closed())
