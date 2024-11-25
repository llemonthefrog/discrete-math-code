import math
import table

def char_size(size: int) -> int:
    return math.ceil(math.log2(size))


@table.printCodeTable("uniform code")
def uniform_code(string: str):
    table = {}
    chars = list(set(string))
    chars.sort()

    size = char_size(len(chars))
    for cnt, ch in enumerate(chars):
        binary_code = format(cnt, f'0{size}b')
        table[ch] = binary_code

    return table

