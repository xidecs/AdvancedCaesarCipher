def encode(stringGw, key):
    direction = 1
    encoded = ""
    for i in stringGw:
        encoded = encoded + chr(((ord(i) - 96) + (key*direction) )%26 + 96)
        direction = direction * -1
    return encoded
