for numbers in range(1,1001):
	if numbers % 3 == 0 :
		print("burrito")
	elif numbers % 5 == 0 :
		print("cheeto")
	elif numbers % 7 == 0 :
		print("veto")
	elif numbers % 3 == 0 and numbers % 5 == 0 :
		print("burritoCheeto")
	elif numbers % 5 == 0 and numbers % 7 == 0 :
		print("burritoVeto")
	elif numbers % 3 == 0 and numbers % 5 == 0  and numbers % 7 == 0 :
		print("BurritoCheetoVeto")
