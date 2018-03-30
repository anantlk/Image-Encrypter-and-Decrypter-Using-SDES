import math
def decimal(binary):
	num=0
	pos=7
	for val in binary:
		num=num+int(val)*math.pow(2,pos)
		pos=pos-1
	return int(num)

