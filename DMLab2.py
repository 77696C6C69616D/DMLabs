# C U B- ∩ (A U C-) ∩ B 

def fun_1 (a = [], b = []): # A U B
	d = list(a)
	d.extend(i for i in b if i not in a)		
	return 'Ø' if d == [] else d

def fun_2 (a = [], b = []): # A ∩ B
	d = []
	d.extend(i for i in a if i in b and i in a)	
	return 'Ø' if d == [] else d

def fun_3 (a = [], b = []): # A \ B
	d = []
	d.extend(i for i in a if i not in b)
	return 'Ø' if d == [] else d

def fun_4 (a = [], b = [], c = []): # U (умова: елементи не входять до A)
	d = []
	d.extend(i for i in fun_1(a, fun_1(b, c)) if i not in a)	
	return 'Ø' if d == [] else d

# a = ['q', 'n', 'x', 't', 'b', 'j', 'l', 'c', 'w', 'r']
# b = ['x', 'w', 'y', 'k', 'a', 'b', 'c', 'd', 'i', 's']
# c = ['n', 'u', 'z', 't', 'm', 'd', 'p', 'w', 'y', 'i']

# a = [10,1,9,4,8]
# b = [5,1,8,7,3]
# c = [7,8,4,3,10]

# C U B- 
tmp_1 = fun_1(c, fun_3(fun_4(a, b, c), b))

# A U C-
tmp_2 = fun_1(a, fun_3(fun_4(a, b, c), c))

# (C U B-) ∩ (A U C-)
tmp_3 = fun_2(tmp_1, tmp_2)

# (C U B- ∩ (A U C-)) ∩ B 
tmp_4 = fun_2(tmp_3, b)

print(f'>> A: {a}')
print(f'>> B: {b}')
print(f'>> C: {c}')
print('\n>> C U B- ')
print(f'>> {tmp_1}')
print('\n>> A U C-')
print(f'>> {tmp_2}')
print('\n>> (C U B-) ∩ (A U C-)')
print(f'>> {tmp_3}')
print('\n>> (C U B- ∩ (A U C-)) ∩ B ')
print(f'>> {tmp_4}')
