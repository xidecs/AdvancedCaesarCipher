def decode(stringGw, key):
    direction = -1
    decoded = ""
    for i in stringGw:
        x = (ord(i) - 96) + (key*direction)
        decoded = decoded + chr(((ord(i) - 96) + (key*direction) )%26 + 96)
        direction = direction * -1
    return decoded