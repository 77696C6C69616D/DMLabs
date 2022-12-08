class logical_functions: # а) реалізовувати логічні функції двох змінних;     
    
    def tautology(self, x1 : int, x2 : int):
        return int(1)
    
    def contradiction(self, x1 : int, x2 : int):
        return int(0)

    def disjunction(self, x1 : int, x2: int): # x1 ∨ x2 
        # x1 + x2
        return int(x1 or x2)

    def conjunction(self, x1 : int, x2: int): # x1 ∧ x2
        # x1 * x2   
        return int(x1 and x2)
    
    def implication_right(self, x1 : int, x2: int ): # x1 → x2
        # x1 → x2 = !x1 + x2         
        return int(not(x1) or x2)

    def logical_conjunction(self, x1 : int, x2: int ): # x1 / x2
        # x1 / x2 = !x1 + !x2
        return int(not(x1) or not(x2))
    
    def exclusive_disjunction(self, x1 : int, x2: int ): # x1 ⊕ x2
        # x1 ⊕ x2 = x1 * !x2 + !x1 * x2            
        return int(x1 and not(x2) or not(x1) and x2)
    
    def implication_left(self, x1 : int, x2: int ): # x1 ← x2
        # x1 ← x2 = x1 * !x2    
        return int(x1 and not(x2))
    
    def sided_limit(self, x1 : int, x2: int ): # x1 ↓ x2
        # x1 ↓ x2 = !x1 * !x2 
        return int(not(x1) and not(x2))
    
    def negation(self, x1 : int, x2: int ): # x1 ~ x2
        # x1 ~ x2 = x1 * x2 + !x1 * !x2
        return int(x1 and x2 or not(x1) and not(x2))
    
    def equivalence(self, x1 : int, x2: int ): # x1 ↔ x2
        # (x1 ∧ x2) ∨ (¬x1 ∧ ¬x2)        
        return int(int(x1 and x2) or int(not(x1) and not(x2)))
              
    values = [ [0, 0], 
               [0, 1], 
               [1, 0], 
               [1, 1] ]
    
    print('''а) реалізовувати логічні функції двох змінних; 
    +---+---+ +---+---+---+---+---+---+---+---+---+---+''')    
    for i in range (0, len(values)):
        x1 = values[i][0]
        x2 = values[i][1]                                
        print(f'    | {x1} | {x2} | | {contradiction(None, x1, x2)} | {conjunction(None, x1, x2)} | {implication_left(None, x1, x2)} | {exclusive_disjunction(None, x1, x2)} | {disjunction(None, x1, x2)} | {sided_limit(None, x1, x2)} | {negation(None, x1, x2)} | {implication_right(None, x1, x2)} | {logical_conjunction(None, x1, x2)} | {tautology(None, x1, x2)} |')        
    print('''    +---+---+ +---+---+---+---+---+---+---+---+---+---+
    | x1| x2| | 0 | * | ← | ⊕ | + | ↓ | ~ | → | / | 1 |
    +---+---+ +---+---+---+---+---+---+---+---+---+---+''')

class table_of_truth: # б) побудувати таблицю істинності для заданої функції (довільної); 
    dm = logical_functions()
    
    values = [ [1, 1, 1], 
               [1, 1, 0], 
               [1, 0, 1], 
               [1, 0, 0], 
               [0, 1, 1], 
               [0, 1, 0], 
               [0, 0, 1], 
               [0, 0, 0] ]
    
    print(f'''\nб) побудувати таблицю істинності для заданої функції (довільної)
    +---+---+---+ +-----------------------------+---------+
    | P | Q | R | | P → (P ∧ ¬Q ↔ (¬P ∨ R)) ∨ Q |Результат|
    +---+---+---+ +-----------------------------+---------+''')
    for i in range (0, len(values)):        
        P = values[i][0]
        Q = values[i][1]
        R = values[i][2]
        tmp_1 = dm.disjunction(not(P), R) 
        tmp_2 = dm.conjunction(P, not(Q))
        tmp_3 = dm.equivalence(tmp_2, tmp_1)
        tmp_4 = dm.disjunction(tmp_3, Q)
        tmp_5 = dm.implication_right(P, tmp_4)
        print(f'    | {P} | {Q} | {R} | |   {tmp_5}    {tmp_2} {int(not(Q))}  {tmp_3}  {int(not(P))}  {tmp_1}     {tmp_4}   |   = {tmp_5}   |')
    print('    +---+---+---+ +-----------------------------+---------+')   

class function_forms: # в) побудувати ДДНФ і ДКНФ для заданої у індивідуальних завданнях функції
    dm = logical_functions()    
    values = [ [1, 1, 1, 1],
               [1, 1, 1, 0],
               [1, 1, 0, 1],
               [1, 1, 0, 0],
               [1, 0, 1, 1],
               [1, 0, 1, 0],
               [1, 0, 0, 1],
               [1, 0, 0, 0],
               [0, 1, 1, 1],
               [0, 1, 1, 0],
               [0, 1, 0, 1],
               [0, 1, 0, 0],
               [0, 0, 1, 1],
               [0, 0, 1, 0],
               [0, 0, 0, 1],
               [0, 0, 0, 0] ] 
    results = [ ]
    print(f'''\nв) побудувати ДДНФ і ДКНФ для заданої у індивідуальних завданнях функції
    1. Таблиця істиності
    +---+---+---+---+ +-------------------------------------------------------+---------+  
    | x1| x2| x3| x4| |¬(((x1∧ ¬x2)↓(¬x3∧x2))⊕ (¬(x2∧x4)∨ ¬(x1∧x3))→ ¬(x1∧x2))|Результат|
    +---+---+---+---+ +-------------------------------------------------------+---------+''')
    for i in range (0, len(values)):        
        x1 = values[i][0]
        x2 = values[i][1]
        x3 = values[i][2]  
        x4 = values[i][3]
        tmp_1 = dm.conjunction(x1, not(x2))
        tmp_2 = dm.conjunction(not(x3), x2)
        tmp_3 = dm.sided_limit(tmp_1, tmp_2)
        tmp_4 = dm.conjunction(x2, x4)
        tmp_5 = dm.conjunction(x1, x3)
        tmp_6 = dm.disjunction(not(tmp_4), not(tmp_5))
        tmp_7 = dm.exclusive_disjunction(tmp_3, tmp_6)
        tmp_8 = dm.conjunction(x1, x2)
        tmp_9 = dm.implication_right(tmp_7, not(tmp_8))
        results.append(int(not(tmp_9)))
        print(f'    | {x1} | {x2} | {x3} | {x4} | |{int(not(tmp_9))}     {tmp_1} {int(not(x2))}   {tmp_3} {int(not(x3))}  {tmp_2}     {tmp_7} {int(not(tmp_4))}   {tmp_4}   {tmp_6} {int(not(tmp_5))}   {tmp_5}    {tmp_9} {int(not(tmp_8))}   {tmp_8}    |   = {int(not(tmp_9))}   |')
    print('    +---+---+---+---+ +-------------------------------------------------------+---------+')
    DDNF = []; DKNF = []
    
    for i in range (0, len(values)):        
        x = values[i]; tmp = '('                      
        if results[i] == 1:                                
            for j in range (0, len(x)): 
                tmp += '¬' + 'x' + str(j+1) if x[j] == 0 else 'x' + str(j+1)                                            
                if j  != len(x)- 1: tmp += ' * '
            tmp += ')'
            DDNF.append(tmp)
        if results[i] == 0:                                
            for j in range (0, len(x)): 
                tmp += '¬' + 'x' + str(j+1) if x[j] == 1 else 'x' + str(j+1)                                            
                if j  != len(x)- 1: tmp += ' + '
            tmp += ')'
            DKNF.append(tmp)
            
    print('    \n    2. ДДНФ'); tmp = ''
    for i in range (0,len(DDNF)): 
        tmp += (DDNF[i])
        if i != len(DDNF)-1: tmp += ' + '
    print('    f(x1, x2, x3 ,x4) =', tmp)
            
    print('    \n    3. ДКНФ');
    print('    f(x1, x2, x3 ,x4) =')    
    for i in range (0,len(DKNF)):       
        tmp = ''
        tmp += (DKNF[i])
        if i != len(DKNF)-1: tmp += ' * '
        print('    ',tmp)