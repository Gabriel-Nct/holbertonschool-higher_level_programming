#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) < 1:
        return (0, None)
    length = len(sentence)
    firstletter = sentence[0]
    return (length, firstletter)
