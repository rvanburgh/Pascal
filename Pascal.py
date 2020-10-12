

def Pascals_Row(rowIndex):
        
    out = []
    
    hashmap = {}
    
    def getSquare(i, j):
        
        if (i,j) in hashmap:
            return hashmap[(i, j)]
        
        elif j==1 or j==i:
            return 1
        
        else:
            res = getSquare(i-1, j-1) + getSquare(i-1, j)
            hashmap[(i,j)] = res
            return res
    
    print([getSquare(rowIndex, z) for z in range(1, rowIndex+1)])
        
if __name__ == '__main__':
    try:
        Pascals_Row(int(input()))
    except ValueError:
        print('Error: Please input an integer')