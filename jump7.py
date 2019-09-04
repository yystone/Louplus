# 跳7程序作业
num = 1
while num <= 100:
	numstr = str(num)
	if '7' in numstr:
		contn7 = True
	else:
		contn7 = False		
	if (num + 7)%7 != 0 and contn7 == False:
		print(num)
	num += 1 
