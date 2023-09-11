password = 'a123456'

i = 3

while i > 0:
	i = i - 1
	pwd_user = input('請輸入密碼: ')
	if pwd_user == password:
		print('登入成功')
		break
	else:
		if i > 0:
			print('密碼錯誤，還有', i, '次機會')
		else:
			print('沒機會嘗試了')