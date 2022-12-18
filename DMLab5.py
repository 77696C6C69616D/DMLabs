alpmatrix = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'k']

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

cin = [
[0, 1, 2, 2, 3, 3, 4, 5],
[1, 0, 1, 1, 2, 2, 3, 4],
[2, 1, 0, 1, 1, 1, 2, 3],
[2, 1, 1, 0, 2, 1, 2, 3],
[3, 2, 1, 2, 0, 1, 2, 3],
[3, 2, 1, 1, 1, 0, 1, 2],
[4, 3, 2, 2, 2, 1, 0, 1],
[5, 4, 3, 3, 3, 2, 1, 0]]

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

print('> Матриця графа:\n')
# matrix_of_len(NodeNumber)
[print(i) for i in cin]
print()


tmp = GetMaxNodesLen(cin)
print('> Центр графа:', GetCenter(tmp))
print('> Периферійні вершини:', GetPerif(tmp))
print('> Радіус графа R(G):', GetRadius(tmp))
print('> Діаметр графа D(G):', GetDiameter(tmp))
print()
