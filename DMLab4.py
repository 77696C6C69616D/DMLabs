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
def A_to_I(inmatrix = [], edge = 0, outmatrix = [], tmp = []):
    if inmatrix == []: return []    
    test = I_to_A(0, inmatrix)
    outmatrix = InheritCells('A', test, edge)
    for test_inner in range (0, len(test)):   
        for test_inner_inner in range (0, len(test)):
            if test[test_inner][test_inner_inner] == 1:
                tmp.append([test_inner, test_inner_inner])    
    for a_index in range (0, edge):
        outmatrix[tmp[a_index][0]][a_index] = 1
        outmatrix[tmp[a_index][1]][a_index] = 1
    return outmatrix
# Функція перекладу матриці інцидентності в матрицю суміжності
def I_to_A(mode = 1, inmatrix = [], outmatrix = []):
    if inmatrix == []: return None
    outmatrix = InheritCells('I', inmatrix)
    for inner in range (0, len(inmatrix[0])):
        tmp = []
        for inner_inner in range (0, len(inmatrix)):    
            if inmatrix[inner_inner][inner] == 1:
                tmp.append(inner_inner)
        outmatrix[tmp[0]][tmp[1]] = 1
        if mode == 1:
            outmatrix[tmp[1]][tmp[0]] = 1   
    return outmatrix
# Функція спадкування матриці без зв'язків
def InheritCells(mode = ' ', inmatrix= [], edge = 0):
    if mode.upper() == 'I':
        return  [[0 for i in range(len(inmatrix))] for j in range(len(inmatrix))]
    if mode.upper() == 'A':
        return  [[0 for i in range(edge)] for j in range(len(inmatrix))]
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
# Перевірка за замовчуванням
def IDCAMatrixInit(inmatrix = [], edge = 0):
    if not IsValid1(inmatrix, edge):
        print('! Сума вершин != кількості ребер')
        quit()
    None
    
matrix = [ 
[1, 1, 0, 0, 0, 0, 0, 1],
[1, 0, 1, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 0, 0, 0, 0],
[0, 0, 0, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 1, 1, 0],
[0, 0, 0, 0, 1, 0, 1, 1],
]

edge = int(input('> Введіть кільість ребер графа \n$ '))
# Створення та заповнення загальної матриці (НЕ ВИКОНУЄТЬСЯ ЗА ЗАМОВЧЕННЯМ)
# matrix = MatrixInit(edge)
# Перевірка умов існування матриці за замовчуванням
IDCAMatrixInit(matrix, edge)
# Вивід матриці суміжності, перекладеної з матриці інцидентності
print('\n> Переклад інцидентної в суміжну:\n')
[print('    ',index) for index in I_to_A(1, matrix)]
# Вивід матриці інцедентності, перекладеної з матриці суміжності
print('\n> Переклад суміжної в інцидентну: \n!(Порядок стовпців може відрізнятися):\n')
[print('    ',index) for index in A_to_I(matrix, edge)]
print()
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