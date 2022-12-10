"""
    Скласти алгоритм програми, що реалізує переклад 
    із заданого способу матричного подання графа в інший.

    Створити програму, що реалізує переклад із заданого 
    способу матричного подання графа в іншій. Передбачити 
    консольне введення вхідних даних і висновок 
    результатів роботи програми на екран.
"""
"""
A - матриця суміжності
I - матриця інцидентності
"""
# Функція перекладу матриці суміжності в матрицю інцидентності
def A_to_I(inmatrix = []):
    if inmatrix == []: return []
    outmatrix = inmatrix
    
    
    return outmatrix
# Функція перекладу матриці інцидентності в матрицю суміжності
def I_to_A(inmatrix = [], outmatrix = []):
    if inmatrix == []: return None
    outmatrix = InheritCells(inmatrix)
    
    
    
    for inner in inmatrix: 
        for a in inner:  
            for inner_inner in range (0, len(inmatrix)):
                
            
                if inmatrix[inner_inner][a] == 1: 
                    outmatrix[a][inner_inner] = 1
                    
                    
                    
                    None
                    
    return outmatrix
# Функція спадкування матриці із скиданням значень
def InheritCells(inmatrix= [], outmatrix = []):
    for row in range(len(inmatrix)):
        tmp = []
        for j in range(0, len(matrix)):
            tmp.append(0)
        outmatrix.append(tmp)
    return outmatrix
# Функція введення матриці
def MatrixInit(edge, outmatrix = []):
    row_len = int(input('$ Введіть кількість [рядків]: '))
    for i in range (0, row_len):
        while True:
            inp = input(f'   $ Введіть {i + 1}-й рядок ["0101"]\n   $ ')  
            if outmatrix != []:
                if len(inp) != len(outmatrix[0]):
                    print('    ! Невірна кількість стовпців\n')
            if not IsValid1(outmatrix, edge):
                print('    ! Сума вершин != кількості ребер')
            if not IsValid2(outmatrix):
                print('    ! Парна кількість вершин із степенем 0')
            outmatrix.extend([[*inp]]); break; 
    return outmatrix
# Перевірка 1
def IsValid1(outmatrix = [], edge = 0, tmp = 0): 
    for i in outmatrix: 
        tmp += sum(i)
    if tmp != edge * 2: # Сума степенів усіх вершин графа дорівнює подвоєній кількості ребер
        return False
    return True
# Перевірка 2
def IsValid2(outmatrix = [], tmp = 0):
    for j in outmatrix:
        for i in j: 
            tmp += 1 if i == 0 else 0 
    return True if tmp % 2 == 0 else False

matrix = [ 
[1, 1, 0, 0, 0, 0, 0, 1],
[1, 0, 1, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 0, 0, 0, 0],
[0, 0, 0, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 1, 1, 0],
[0, 0, 0, 0, 1, 0, 1, 1],
]

edge = 0
# edge = int(input('> Введіть кільість ребер графа \n$ '))
# Створення та заповнення загальної матриці
# matrix = MatrixInit(edge)

# Вивід матриці суміжності, перекладеної з матриці інцидентності
print('\n> Переклад інцидентної в суміжну:\n')
[print(i) for i in I_to_A(matrix)]

"""
# Вивід матриці інцедентності, перекладеної з матриці суміжності
print('\n> Переклад суміжної в інцидентну:\n')
[print(i) for i in A_to_I(matrix)]
"""

"""
# Тест
print('> Граф:'
'\n              x2       '
'\n         a1  /  \ a3   '
'\n            /    \     '
'\n          x1 ____ x3   '
'\n           |  a2  |    '
'\n          x6 ____ x4   '
'\n            \ a5 /     '
'\n         a7  \  / a6   '
'\n              x5       ' 
)
"""
