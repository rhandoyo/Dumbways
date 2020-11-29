 
putar = 4
def putarAray(prm):
    for i in range(putar+1):
        if i != 0:
            print('Putaran', i,':',(prm[i::] + prm[:i]))


param = ['a','b','c','d','e']
putarAray(param)