alpmatrix = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'k']
nummatrix = [1, 2, [3, 4], [5, 6], 7, 8]


def matrix_of_len (inmatrix): 
    outmatrix = init_out(inmatrix)
    
    for inner in range (0, len(outmatrix)):
        
        for inner_inner in range (1, len(outmatrix) + 1):
            
            
            None
    
    for i in outmatrix:
        print(i)
    
    return outmatrix

def init_out(input, cout = [], tmp = []): 
    length = len(input)
    for i in input:
        if str(type(i)) == "<class 'list'>":
            length += len(i) - 1
    for inner in range (0, length):    
        tmp.append(0)
    for inner_inner in range (0, length): 
        cout.append(tmp)
    return cout

def GetMaxNode(inp, cout = []): 
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

cin = [
[0, 1, 2, 2, 3, 3, 4, 5],
[1, 0, 1, 1, 2, 2, 3, 4],
[2, 1, 0, 1, 1, 1, 2, 3],
[2, 1, 1, 0, 2, 1, 2, 3],
[3, 2, 1, 2, 0, 1, 2, 3],
[3, 2, 1, 1, 1, 0, 1, 2],
[4, 3, 2, 2, 2, 1, 0, 1],
[5, 4, 3, 3, 3, 2, 1, 0]]

tmp = (GetMaxNode(cin))

print('\n> Граф: '
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
print('> Матриця графа:\n')
matrix_of_len(nummatrix)
print()

print('> Центр графа:', GetCenter(tmp))
print('> Периферійні вершини:', GetPerif(tmp))
print('> Радіус графа R(G):', GetRadius(tmp))
print('> Діаметр графа D(G):', GetDiameter(tmp))
print()
