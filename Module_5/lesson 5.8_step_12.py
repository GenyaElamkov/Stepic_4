from typing import Any


class NonNegativeObject:
    def __init__(self, **kwargs) -> None:
        # for k, v in kwargs.items():
        #     if isinstance(v, (int | float)):
        #         self.__dict__[k] = abs(v)
        #     else:
        #         self.__dict__[k] = v

        for k, v in kwargs.items():
            setattr(self, k, v)

    # def __getattribute__(self, __name: str):
    #     return object.__getattribute__(self, __name)

    def __setattr__(self, __name: str, __value: Any) -> None:
        if isinstance(__value, (int, float)):
            __value = abs(__value)
        object.__setattr__(self, __name, __value)



point = NonNegativeObject(x=1, y=-2, z=0, color="black")

print(point.x)
print(point.y)
print(point.z)
print(point.color)


point = NonNegativeObject(x=1.5, y=-2.3, z=0.0, color='yellow')

print(point.x)
print(point.y)
print(point.z)
print(point.color)