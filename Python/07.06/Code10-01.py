from typing import Counter


def openBox() :
    global count 
    print('BOX OPEN')
    count -= 1
    if count == 0 :
        print('INPUT RING')
        return
    openBox()
    print('BOX CLOSE')

count = 10
openBox()