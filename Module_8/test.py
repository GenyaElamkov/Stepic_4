import functools

def add_attr_to_instances(cls):
    old_init = cls.__init__             # сохраняем исходный инициализатор
    
    @functools.wraps(old_init)
    def new_init(self, *args, **kwargs):
        old_init(self, *args, **kwargs) # вызываем исходный инициализатор
        self.attr = None                # добавляем экземпляру класса атрибут attr
    
    cls.__init__ = new_init             # заменяем исходный инициализатор новым
    return cls

@add_attr_to_instances
class MyClass:
    pass


obj = MyClass()

print(obj.attr)