def div42by(divideBy):
	try:
		return 42/divideBy
	except ZeroDivisionError:
		print("enter valid value")
	return 
print(div42by(2))
print(div42by(0))

