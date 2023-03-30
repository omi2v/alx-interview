#!/usr/bin/python3
def canUnlockAll(boxes):
    mykey = [0];
    for key in mykey:
        for boxkey in mykey[key]:
            if boxkey not in mykey and boxkey < len(boxes):
                mykey.append(boxkey)
                if len(mykey) == len(boxes):
                    return True
                return False
