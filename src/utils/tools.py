def getBitFromByte(byte, position):
    i = int(byte, 16)
    return i >> position & 1
