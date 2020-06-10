country = input('please enter your country:')
age = input('please enter your age:')
if country == 'Taiwan':
	if age >= 18:
		print('you are able to take driver license')
	else:
		print('you are unable to take driver license')
else:
	print('sorry, we cannot serve you.')