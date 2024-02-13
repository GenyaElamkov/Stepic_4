from typing import Self


class Config:
    _instance = None

    def __new__(cls, *args, **kwargs) -> Self:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        self.program_name = "GenerationPy"
        self.environment = "release"
        self.loglevel = "verbose"
        self.version = "1.0.0"


config = Config()

print(config.program_name)
print(config.environment)
print(config.loglevel)
print(config.version)


config1 = Config()
config2 = Config()
config3 = Config()

print(config1 is config2)
print(config1 is config3)
