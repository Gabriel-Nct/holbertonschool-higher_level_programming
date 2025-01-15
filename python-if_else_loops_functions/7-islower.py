#!/usr/bin/env python3
def islower(c):

    if ord(c) > 96 and ord(c) < 123:
        return True
    elif ord(c) == c:
        return True
    else:
        return False
