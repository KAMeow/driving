country = input('please enter your country:')
age = input('please enter your age:')
age = int(age)
if country == 'Taiwan':
	if age >= 18:
		print('you are able to take driver license')
	else:
		print('you are unable to take driver license')
elif country == 'American':
	if age >= 16:
		print('you are able to take driver license')
	else:
		print('you are unable to take driver license')
else:
	print('sorry, this is only for Taiwan / American')