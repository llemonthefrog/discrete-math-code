import math
import table

def char_size(size: int) -> int:
    return math.ceil(math.log2(size))

def freq(msg: str):
    table = {}

    st = set(msg)
    lst = [[char, round((msg.count(char) / len(msg)), 5)] for char in st]

    for i in range(1, len(lst)):
        elem = lst[i]
        j = i - 1
        while j >= 0 and elem[1] > lst[j][1]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = elem

    cnt = 0
    
    for i in range(len(lst)):
        char, frequency = lst[i]
        table[char] = (frequency, (round(cnt, 5), round(cnt + frequency, 4)))
        print(char, frequency)
        cnt += frequency

    return table
    
def uniform_code(string: str) -> int:
    table = {}
    chars = list(set(string))
    chars.sort()

    size = char_size(len(chars))
    for cnt, ch in enumerate(chars):
        binary_code = format(cnt, f'0{size}b')
        table[ch] = binary_code

    for key, value in table:
        print(f"{key} - {value}")

    msg: str = ""
    for ch in string:
        msg += table[ch]

    return msg


def ariph_code(string: str) -> str:
    freq_table = freq(string)

    left, right = 0, 1
    for ch in string:
        frequency, (l, r) = freq_table[ch]
        low, high = (l, r)
        right = left + (right - left) * high
        left = left + (right - left) * low

        print(f"{ch}: {left} - {right}") # comment if you dont need table of codes

    size: int = 0
    if(right - left == 0):
        raise BaseException("error")
    else:
        size = round(math.log2(1 / (right - left)))

    result: str = bin(int(right * 2 ** size))[2:]
    result = (size - len(result)) * "0" + result
    
    return result
