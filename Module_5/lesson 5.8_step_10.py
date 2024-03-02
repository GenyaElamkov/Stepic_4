class Ord:
    def __getattribute__(self, __name):
        return ord(__name)
        # return object.__getattribute__(self, __name)
    
    # def __getattr__(self, __name):
    #     return ord(__name)




obj = Ord()

print(obj.a)
print(obj.b)

obj = Ord()

print(obj.в)
print(obj.г)