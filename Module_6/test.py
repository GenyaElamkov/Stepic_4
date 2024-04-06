from contextlib import contextmanager

@contextmanager
def writable_text_file(path):
    file = open(path, mode='w', encoding='utf-8')
    yield file
    file.close()


with writable_text_file('output.txt') as file:
    file.write('Python generation!')