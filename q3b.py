def add_binary(a, b):
    a = a[2:]
    b = b[2:]

    if len(a) < len(b):
        a = '0' * (len(b) - len(a)) + a
    else:
        b = '0' * (len(a) - len(b)) + b

    carry = 0
    result = ""

    for i in range(len(a) - 1, -1, -1):
        bit_sum = int(a[i]) + int(b[i]) + carry
        result = str(bit_sum % 2) + result
        carry = bit_sum // 2

    if carry:
        result = "1" + result

    i = 0
    while i < len(result) and result[i] == "0":
        i += 1

    result = result[i:]
    if result == "":
        result = "0"

    return "0b" + result
