class MyClass:
    
    
    @staticmethod
    def my_staticmethod():
        print('Это статический метод')


    def method(self):
        print(self.__class__)

MyClass.my_staticmethod()

cat = MyClass()

cat.my_staticmethod()

cat.method()
MyClass.method(cat)