import re


class CaseHelper:
    @staticmethod
    def is_snake(string: str) -> bool:
        match = re.search(r"^([a-z]*)_([a-z]*)$|^[a-z]*$", string)
        if match:
            return True
        return False

    @staticmethod
    def is_upper_camel(string: str) -> bool:
        match = re.search(r"^(?:[A-Z][a-z]+)+", string)
        if match:
            return True
        return False

    @staticmethod
    def to_snake(string: str) -> str:
        return re.sub(r"(?<!^)(?=[A-Z])", "_", string).lower()

    @staticmethod
    def to_upper_camel(string: str) -> str:
        return string[0].upper() + string.title()[1:].replace("_", "")


# print(CaseHelper.is_snake("beegeek"))
# print(CaseHelper.is_snake("bee_geek"))
# print(CaseHelper.is_snake("Beegeek"))
# print(CaseHelper.is_snake("BeeGeek"))

print(CaseHelper.is_upper_camel("beegeek"))
print(CaseHelper.is_upper_camel("bee_geek"))
print(CaseHelper.is_upper_camel("Beegeek"))
print(CaseHelper.is_upper_camel("BeeGeek"))

# print(CaseHelper.to_snake("Beegeek"))
# print(CaseHelper.to_snake("BeeGeek"))

# print(CaseHelper.to_upper_camel("beegeek"))
# print(CaseHelper.to_upper_camel("bee_geek_dfsf"))

# cases = [
#     "assert_equal",
#     "tear_down",
#     "__init__",
#     "assertEqual",
#     "setUp",
#     "tearDown",
#     "run",
#     "exit",
#     "setup",
# ]

# for case in cases:
#     print(CaseHelper.is_snake(case))

# cases = [
#     "assert_equal",
#     "tear_down",
#     "__init__",
#     "assertEqual",
#     "setUp",
#     "tearDown",
#     "run",
#     "exit",
#     "setup",
#     "AssertEqual",
#     "SetUp",
# ]

# for case in cases:
#     print(CaseHelper.is_upper_camel(case))
