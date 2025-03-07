import random as rand
import time as time
HEIGHT = 8
WIDTH = 6

def validList(lst):
    i = 0
    for word in lst:
        i += len(word)
    return True if i==HEIGHT*WIDTH else False

def btl_nonrandom(word,index, lst, layout, final, i, j):
    if(len(lst)==0 and len(word)==index):
        for row in layout:
            print(" ".join(row))
        print("-----------")
        final.append(layout)
        return
    
    if (len(word)==index):
        word = lst.pop()
        for newi in range(HEIGHT):
            for newj in range(WIDTH):
                if(layout[newi][newj]==""):
                    layout[newi][newj] = word[0]
                    btl(word, 1, lst, layout, final, newi, newj)
                    layout[newi][newj]=""
        lst.append(word)
                
    else:
        for di in range(-1, 2):
            for dj in range (-1,2):
                if (i+di >= 0 and i+di < HEIGHT and j+dj>=0 and j+dj < WIDTH and layout[i+di][j+dj]=="" ):
                    layout[i+di][j+dj] = word[index]
                    btl(word, index+1, lst, layout, final, i+di, j+dj)
                    layout[i+di][j+dj]=""

def btl(word,index, lst, layout, final, i, j):
    if(len(lst)==0 and len(word)==index):
        for row in layout:
            print(" ".join(row))
        print("-----------")
        final.append(layout)
        return
    
    if (len(word)==index):
        word = lst.pop()
        positions = [(i,j) for i in range(HEIGHT) for j in range (WIDTH)]
        rand.shuffle(positions)
        for (newi, newj) in positions:
            if(layout[newi][newj]==""):
                layout[newi][newj] = word[0]
                btl(word, 1, lst, layout, final, newi, newj)
                layout[newi][newj]=""
        lst.append(word)
    else:
        for di in range(-1, 2):
            for dj in range (-1,2):
                if (i+di >= 0 and i+di < HEIGHT and j+dj>=0 and j+dj < WIDTH and layout[i+di][j+dj]=="" ):
                    layout[i+di][j+dj] = word[index]
                    btl(word, index+1, lst, layout, final, i+di, j+dj)
                    layout[i+di][j+dj]=""

def btl_one(word,index, lst, layout, final, i, j):
    if(len(lst)==0 and len(word)==index):
        for row in layout:
            print(" ".join(row))
        print("-----------")
        final.append(layout)
        return True
    
    if (len(word)==index):
        word = lst.pop()
        positions = [(i,j) for i in range(HEIGHT) for j in range (WIDTH)]
        rand.shuffle(positions)
        for (newi, newj) in positions:
            if(layout[newi][newj]==""):
                layout[newi][newj] = word[0]
                if (btl_one(word, 1, lst, layout, final, newi, newj)):
                    layout[newi][newj]=""
                    lst.append(word)
                    return True
                layout[newi][newj]=""
        lst.append(word)
    else:
        for di in range(-1, 2):
            for dj in range (-1,2):
                if (i+di >= 0 and i+di < HEIGHT and j+dj>=0 and j+dj < WIDTH and layout[i+di][j+dj]=="" ):
                    layout[i+di][j+dj] = word[index]
                    if(btl_one(word, index+1, lst, layout, final, i+di, j+dj)):
                        layout[i+di][j+dj]=""
                        return True
                    layout[i+di][j+dj]=""


def buildLayout(lst):
    if(not validList(lst)):
       print("INVALID WORD LIST")
    else:
        layout = [["" for _ in range(WIDTH)] for _ in range(HEIGHT)]
        final =[]
        for i in range(5):
            btl_one("",0, lst, layout, final, rand.randint(0, HEIGHT-1), rand.randint(0, WIDTH-1))
        return final
    

def transformlist(lst):
    # create list of word lengths, order it and then create a new list of its marker

wordlist = ["SUPERMARIOBROS", "TOAD", "BOWSER", "LUIGI", "PEACH", "MUSHROOM", "GOOMBA"]
baselist = transformlist(wordlist)
res = buildLayout(wordlist)
