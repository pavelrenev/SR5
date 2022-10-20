print("Данная программа переводит целое неотрицательное число из десятичной системы в двоичную или восмеричную")

c=input("Введите целое число: ")
s=input("Введите систему в которую будет переведено число: ")

def per(c, s):
	c_k1=""
	while c>0:
		c_k1=str(c%s)+c_k1
		c=c//s
	
	return c_k1

def prov_c(c):

	k=0
	s="1234567890"
	for i in c:
		if i not in s:
			k+=1
			print("Неверно введено число")
			break
	return k

def prov_s(s):	
	k=0
	c="28"
	for i in s:
		if i not in c or len(s)!=1:
			k+=1
			print("Неверно введена система перевода")
			break
	return k

if (prov_c(c)+prov_s(s))==0:
	c,s=int(c),int(s)
	c_k=per(c, s)

	print("Результат:", c, "=>", c_k)