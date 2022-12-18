alpmatrix = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'k']
NodeNumber = 8
branch = [3, 5]

def matrix_of_len (inmatrix, tmp = []): 
    cout = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
    ]
    substractor = len(branch)
    
    for inner in range (0, NodeNumber):
        for inner_inner in range (0, NodeNumber):
            if inner != inner_inner:   
                
                if inner_inner + 1 in branch: 
                    cout[inner][inner_inner] = None
                    continue
                    
                
                
                
                if inner_inner + 1 > NodeNumber/2: 
                    cout[inner][inner_inner] = inner_inner + 1 - inner + 1 - substractor
                    continue
                
                
                
                cout[inner][inner_inner] = inner_inner - 1 - inner - 1
                    
                    

                    
                    
                    
            None
        break
            
            
            
            
    # [0, 1, 2, 2, 3, 3, 4, 5],
    # [1, 0, 1, 1, 2, 2, 3, 4],
    # [2, 1, 0, 1, 1, 1, 2, 3],
    # [2, 1, 1, 0, 2, 1, 2, 3],
    # [3, 2, 1, 2, 0, 1, 2, 3],
    # [3, 2, 1, 1, 1, 0, 1, 2],
    # [4, 3, 2, 2, 2, 1, 0, 1],
    # [5, 4, 3, 3, 3, 2, 1, 0]]
    
    
    for i in cout: 
        print(i)
    
        
    exit()    

def GetMaxNodesLen(inp, cout = []): 
    [cout.append(max(i)) for i in inp]
    return cout

def GetCenter (MaxNodeLen, cout = []):
    [cout.append(alpmatrix[i]) if MaxNodeLen[i] == min(MaxNodeLen) else None for i in range (0, len(MaxNodeLen))]
    return cout

def GetPerif (MaxNodeLen, cout = []):     
    [cout.append(alpmatrix[i]) if MaxNodeLen[i] == max(MaxNodeLen) else None for i in range (0, len(MaxNodeLen))]
    return cout

def GetRadius (MaxNodeLen):     
    return min(MaxNodeLen)

def GetDiameter (MaxNodeLen):     
    return max(MaxNodeLen)

print('\n> Граф: \n'
"""
       c      e
       o------o
     / |      |
o---o  |      |
a   b\ |      | f
       o------o---o g
       d         /
              k o
""")
print("""
o---o---o---o---o---o
a   b   d   f   g   k
        c---e
""")

print('> Матриця графа:\n')
matrix_of_len(NodeNumber)
print()

tmp = GetMaxNodesLen(cin)
print('> Центр графа:', GetCenter(tmp))
print('> Периферійні вершини:', GetPerif(tmp))
print('> Радіус графа R(G):', GetRadius(tmp))
print('> Діаметр графа D(G):', GetDiameter(tmp))
print()
