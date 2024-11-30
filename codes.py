import math
from collections import defaultdict
from decimal import Decimal, getcontext

getcontext().prec = 256

def save_table(table) -> None:
    with open(input("please insert table name(with extension):\n"), "w+") as file:
        for key, value in table.items():
            file.write(f"{key} {value}\n")
        

def freq(msg: str):
    total_count = len(msg)
    freq = {}
    for ch in msg:
        freq[ch] = freq.get(ch, 0) + 1

    cumulative_prob = Decimal(0)
    freq_table = {}

    print("\nfrequency table\n")
    for ch, count in sorted(freq.items()):
        probability = Decimal(count) / Decimal(total_count)
        freq_table[ch] = (probability, (cumulative_prob, cumulative_prob + probability))
        print(f"{ch} - {probability:.8f}") 
        cumulative_prob += probability
    print("\n")

    return freq_table

def char_size(size: int) -> int:
    return math.ceil(math.log2(size))

def encode_from_table(msg: str) -> None:
    result: str = ""
    table = {}
    if(input("create from file? [y or n]\n") == "y"):
        with open(input("write file name:\n"), "r+") as file:
            table = {}
            for i, st in enumerate(file.readlines()):
                parsed = st.split(" ")
                if(len(parsed) != 2):
                    raise BaseException(f"not pair in line: {i}")
                
                if(len(parsed[0]) != 1):
                    raise BaseException(f"not a char in line: {i}")

                table[parsed[0]] = parsed[1][:len(parsed[1]) - 1]
            
    else:
        buf: str = ""
        table = {}
        while(True):
            buf = input("insert character: \n")

            if(buf == "exit"):
                break
            if(len(buf) > 1):
                print("incorrect type of char")
            else:
                table[buf] = input("insert code: \n")

        
    for ch in msg:
        if ch not in table.keys():
            raise BaseException(f"key not in table: {ch}")
        
        result = result + " " + table[ch]

    return result
    
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
        msg = msg + " " + table[ch]

    if(input("do you want to save encoding table? [y or n]\n") == "y"):
        save_table(table)

    return msg


def arithmetic_encode(string: str):
    freq_table = freq(string)

    left = Decimal(0)
    right = Decimal(1)
    
    for ch in string:
        frequency, (low, high) = freq_table[ch]
        range_ = right - left
        right = left + range_ * high
        left = left + range_ * low
        print(f"{ch}: {left:.30f} - {right:.30f}")

    if right - left == 0:
        raise ValueError("Range is zero, indicating an error in encoding.")

    size = round(math.log2(1 / (right - left)))
    result = bin(int(right * Decimal(2) ** size))[2:]
    result = (size - len(result)) * "0" + result

    return result

def haming_encode(data_bits: str):
    data_bits = [int(bit) for bit in data_bits]
    m = len(data_bits) 

    r = 0
    while (2**r < m + r + 1):
        r += 1
    
    total_bits = m + r
    encoded_bits = [0] * total_bits

    j = 0
    for i in range(1, total_bits + 1):
        if (i & (i - 1)) != 0:
            encoded_bits[i - 1] = data_bits[j]
            j += 1

    for i in range(r):
        parity_index = (2**i) - 1 
        parity_value = 0
        for j in range(parity_index, total_bits, 2**(i+1)):
            parity_value ^= sum(encoded_bits[j:j + 2**i])
        
        encoded_bits[parity_index] = parity_value % 2  
    
    return ''.join(map(str, encoded_bits))
