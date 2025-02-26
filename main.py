
def getList(filename):
    lst = []
    with open(filename) as f:
        for line in f:
            lst.append(line.strip())
    return lst

print(getList("src/WordLists/SuperMarioBros.txt"))