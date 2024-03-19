def log_for(logfile: str, date_str: str):
    filename = f"log_for_{date_str}.txt"
    with (
        open(logfile, "r", encoding="utf-8") as file_read,
        open(filename, "w", encoding="utf-8") as file_write,
    ):
        for context in file_read:
            if date_str in context:
                file_write.write(context.split(maxsplit=1)[1])


with open("log.txt", "w", encoding="utf-8") as file:
    print("2022-01-01 INFO: User logged in", file=file)
    print("2022-01-01 ERROR: Invalid input data", file=file)
    print("2022-01-02 INFO: User logged out", file=file)
    print("2022-01-03 INFO: User registered", file=file)

log_for("log.txt", "2022-01-01")

with open("log_for_2022-01-01.txt", encoding="utf-8") as file:
    print(file.read())
