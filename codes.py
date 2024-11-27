import math
import table
from collections import defaultdict
from decimal import Decimal, getcontext

def freq(msg: str):
    table = defaultdict(float)

    # Подсчет частоты символов
    for char in msg:
        table[char] += 1
    
    # Преобразование в список и расчет относительных частот
    total_chars = len(msg)
    freq_list = [[char, Decimal(count) / Decimal(total_chars)] for char, count in table.items()]
    
    # Сортировка по частоте (по убыванию)
    freq_list.sort(key=lambda x: x[1], reverse=True)

    cnt = Decimal(0)
    freq_table = {}

    for char, frequency in freq_list:
        freq_table[char] = (frequency, (cnt, cnt + frequency))
        cnt += frequency

    return freq_table

def char_size(size: int) -> int:
    return math.ceil(math.log2(size))
    
def uniform_code(string: str) -> int:
    table = {}
    chars = list(set(string))
    chars.sort()

    size = char_size(len(chars))
    for cnt, ch in enumerate(chars):
        binary_code = format(cnt, f'0{size}b')
        table[ch] = binary_code

    for key, value in table.items():
        print(f"{key} - {value}")

    msg: str = ""
    for ch in string:
        msg += table[ch]

    return msg


def ariph_code(string: str) -> str:
    freq_table = freq(string)

    left = Decimal(0)
    right = Decimal(1)
    
    for ch in string:
        frequency, (l, r) = freq_table[ch]
        low, high = (l, r)
        right = left + (right - left) * high
        left = left + (right - left) * low

        print(f"{ch}: {left} - {right}")  # delete if you dont need debug

    size: int = 0
    if right - left == 0:
        raise BaseException("error")
    else:
        size = round(math.log2(1 / (right - left)))

    result: str = bin(int(right * Decimal(2) ** size))[2:]
    result = (size - len(result)) * "0" + result
    
    return result
