class Closer:
    def __init__(self, obj) -> None:
        self.obj = obj

    def __enter__(self):
        return self.obj

    def __exit__(self, *args, **kwargs)-> None:
        try:
            self.closed()
        except AttributeError:
            print("Незакрываемый объект")

    def closed(self)-> None:
        self.obj.close()