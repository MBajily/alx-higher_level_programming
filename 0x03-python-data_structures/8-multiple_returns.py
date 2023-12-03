#!/usr/bin/python3
def multiple_returns(sentence):
    result = ()
    if sentence:
        result = len(sentence), sentence[0]
    else:
        result = len(sentence), None
    return result
