def printCodeTable(type: str):
    def wrapper(func):
        def wrapped(*arg, **kwargs):
            table = func(*arg, **kwargs)
            print(f"table of {type}")
            for key, value in table.items():
                print(f"{key} - {value}")
            return table
        return wrapped
    return wrapper