password = 'a123456'

i = 3
j = 3

while i > 0:
	password_user = input('請輸入密碼: ')
	if password_user == password:
		print('登入成功')
		break
	else:
		j = j - 1
		if j > 0:
			print('密碼錯誤，還有', j, '次機會')
		else:
			break
	i = i - 1