# Вимоги до пз:
	#! 1. Модульна структура програми;
	#! 2. Уведення даних із клавіатури і з зовнішнього файлу;
	#! 3. Перевірка  коректності введених даних;
	#! 4. Меню.

# Результати виконання: 
	#! print(a+b) # [1,2,3,4,5,6,7,8,9,10]
	#! print(a*b) # [6,5,4,7]
	#! print(a-b) # [3,2,1]
	#! print((a+b)-(a*b)) # [1,2,3,8,9,10]
	#! Доповнення множини 
	#! Різниця між множинами 
	#! Симетрична різниця між множинами 

# Аксіома існування:
def fun_1(a = [], b = []): # A != Ø B != Ø
	return False if a == [] and b == [] else True

# Аксіома еквівалентності:
def fun_2(a = [], b = []): # A = B
	return True if a == b else False

# Аксіома об'єднання: 
def fun_3 (a = [], b = []): # A U B
	c = list(a)
	c.extend(i for i in b if i not in a)		
	return 'Ø' if c == [] else c 

# Аксіома перетинання:
def fun_4 (a = [], b = [], c = []): # A ∩ B
	c.extend(i for i in a if i in b and i in a)	
	return 'Ø' if c == [] else c 

# Аксіома про універсальну множину:
def fun_5 (a = [], b = [], c = []): # A- 
	c = []
	c.extend(i for i in fun_3(a, b) if i not in a)
	return 'Ø' if c == [] else c 

# Аксіома про порожню множину:
def fun_6(a = []): # A = Ø 
	return True if a == [] else False

# Доповнення множини:
def fun_7(a = [], b = [], c = []): # A U A-
	c = list(a)
	c.extend(i for i in fun_3(a, b) if i not in a)
	return 'Ø' if c == [] else c 

# Різниця між множинами:
def fun_8 (a = [], b = [], c = []): # A \ B
	c.extend(i for i in a if i not in b)
	return 'Ø' if c == [] else c 

# Симетрична різниця між множинами: 
def fun_9 (a = [], b = [], c = []): # А \ В + В \ А
	c.extend(i for i in a if i in a and i not in b)
	c.extend(i for i in b if i in b and i not in a)
	return 'Ø' if c == [] else c 

# Заповнення множини з консолі
def trm_ (): 
	list = []
	while(True):				
		inp = input('>> ') 
		if inp == '\\ex': break
		try: list.append(int(inp)); continue
		except ValueError: None
		try: list.append(float(inp)); continue
		except ValueError: None	
		if inp.lower() == 'true': list.append(True); continue	
		if inp.lower() == 'false': list.append(False); continue
		list.append(inp)
	return list

#Заповнення множини з файла
def fil_ (file_name = 'input.txt'): 			
	list = []
	file = open(file_name, "r")
	list_tmp = file.read().splitlines()		
	for i in list_tmp: 
		try: list.append(int(i)); continue
		except ValueError: None
		try: list.append(float(i)); continue
		except ValueError: None	
		if i.lower() == 'true': list.append(True); continue	
		if i.lower() == 'false': list.append(False); continue
		list.append(i)	
	file.close()	
	return list

# Стандартні значення множин A і B
a = [1,2,3,4,5,6,7]
b = [4,5,6,7,8,9,10]

# Меню: 
while(True): 
	print('\n>> \\fl → Заповнення множин')
	print('>> \\fn → Операції над множинами (опціонально)')
	print('>> \\ex → Вихід')
	ch = input('\n>> Оберіть дію: ')
	if ch == '\\ex': exit()
	if ch == '\\fl': 
		while True: 
			print(f'\n>> Множина A: {a}')
			print(f'>> Множина B: {b}')
			print('\n>> \\tm → Заповнення з консолі')
			print('>> \\fl → Заповнення з файла')
			print('>> \\df → Залишити стандартні значення')			
			ch = input('\n>> Тип заповнення: ')						
			if ch == '\\df' or ch == '\\ex': break
			if ch == '\\tm': 				
				ch = input('\n>> Заповнити множину: ')										
				if ch == 'a': print('\n>> (\\ex - Вихід)'); a = trm_()
				if ch == 'b': print('\n>> (\\ex - Вихід)'); b = trm_() 
			if ch == '\\fl': 
				ch = input('\n>> Заповнити множину: ')
				if ch == 'a': a = fil_()
				if ch == 'b': b = fil_() 
	if ch == '\\fn':
		print(f'\n>> Множина A: {a}')
		print(f'>> Множина B: {b}')	
		print(f'\n>> Аксіома існування (A != Ø, B != Ø): {fun_1(a, b)}')
		print(f'\n>> Аксіома еквівалентності (A = B): {fun_2(a, b)}')
		print(f"\n>> Аксіома об'єднання (A U B): \n{fun_3(a, b)}")
		print(f'\n>> Аксіома перетинання (A ∩ B): \n{fun_4(a, b)}')
		print(f'\n>> Аксіома про універсальну множину A (A-): \n{fun_5(a, b)}')
		print(f'\n>> Аксіома про універсальну множину B (B-): \n{fun_5(b, a)}')
		print(f'\n>> Аксіома про порожню множину A (A = Ø): {fun_6(a)}')
		print(f'\n>> Аксіома про порожню множину B (B = Ø): {fun_6(b)}')
		print(f'\n>> Доповнення множини A (A U A-): \n{fun_7(a, b)}')
		print(f'\n>> Доповнення множини B (B U B-): \n{fun_7(b, a)}')
		print(f'\n>> Різниця між множинами (A \\ B): \n{fun_8(a, b)}')
		print(f'\n>> Симетрична різниця між множинами (А \\ В + В \\ А): \n{fun_9(a, b)}\n')

# print(fun_1(a, b)) # A != Ø B != Ø 
# print(fun_2(a, b)) # A = B 
# print(fun_3(a, b)) # A U B 
# print(fun_4(a, b)) # A ∩ B 
# print(fun_5(a)) # A- 
# print(fun_6(a)) # A = Ø  
# print(fun_7(a)) # A U A-  
# print(fun_8(a, b)) # A \ B 
# print(fun_9(a, b)) # А \ В + В \ А 