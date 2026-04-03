def add_binary(a, b):
    '''
    Given two strings perform binary addition and return the result as a string
    '''
    result = ""
    carry = 0
    i = len(a) - 1
    j = len(b) - 1

    while i >= 0 or j >= 0 or carry:
        if i >= 0:
            carry += int(a[i])
            i -= 1
        if j >= 0:
            carry += int(b[j])
            j -= 1

        result = str(carry % 2) + result
        carry = carry // 2

    return result
