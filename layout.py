HEIGHT = 8 
WIDTH = 6

def validList(lst):
    i = 0
    for word in lst:
        i += len(word)
    return True if i==HEIGHT*WIDTH else False

def btl():
    t = 0

def buildLayout(lst):
    if(not validList(lst)):
       print("INVALID WORD LIST")
    else:
        return btl()