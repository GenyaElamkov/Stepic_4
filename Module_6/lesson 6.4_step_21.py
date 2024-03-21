def is_context_manager(obj) -> bool:
    return all((hasattr(obj, "__enter__"), hasattr(obj, "__exit__")))


print(is_context_manager(1992))
print(is_context_manager("beegeek"))
print(is_context_manager([1, 2, 3]))
print(is_context_manager({"one": 1, "two": 2}))
print(is_context_manager(None))

print(is_context_manager(open("output.txt", mode="w")))
