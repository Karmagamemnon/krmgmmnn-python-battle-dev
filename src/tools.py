def getBitFromByte(byte, position):
    i = int(byte, 16)
    return i >> position & 1


def extractKBits(num, k, p):

    # convert number into binary first
    binary = bin(num)

    # remove first two characters
    binary = binary[2:]

    end = len(binary) - p
    start = end - k + 1

    # extract k  bit sub-string
    kBitSubStr = binary[start: end+1]

    # convert extracted sub-string into decimal again
    print(int(kBitSubStr, 2))
