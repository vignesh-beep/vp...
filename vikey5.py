num1=int(input())
c=0
for i in range(1,num1+1):
	if(num1%i==0):
		c+=1
if(c==2):
	print('yes')
else:
	print('no')
