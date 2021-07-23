from datetime import datetime


def getBitFromByte(byte, position):
    i = int(byte, 16)
    return i >> position & 1


def strftimestamp(t: datetime) -> str:
    return t.strftime('%Y-%m-%d %H:%M:%S')
