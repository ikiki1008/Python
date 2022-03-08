print('hell yeah')

while True :
	a=input('whats first number?')
	if a == '0000':
		break
	b=int(input('OIC, now gimme second numba'))
	a=int(a)
	result=a+b
	print(a,'+',b,'=',result)
	result=a-b
	print(a,'-',b,'=',result)
	result=a/b
	print(a,'/',b,'=',result)
print('end of calculation!!')
