'''
removes all occurrences of a string from another string
'''

def remove(substr,theStr):
    position_substr = theStr.find(substr,0)

    if position_substr != -1:
        return theStr[:position_substr] + '' + theStr[position_substr+len(substr):]
    else:
        return theStr

def remove_all(substr,theStr):
    position_substr = count = 0

    while True:
        position_substr = theStr.find(substr, position_substr) +1
        if position_substr > 0:
            count += 1
        else:
            break
    for i in range(count):
        theStr = remove(substr,theStr)

    return theStr
