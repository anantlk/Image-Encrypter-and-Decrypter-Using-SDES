def binary(number):
	s=''
	bin_val=''
	while(number>0):
		s=s+str(number%2)
		number=number//2
	#print(s)
	if(len(s)<8):
		s=s+"0"*(8-len(s))
	#print(s)
	for val in s[len(s)-1::-1]:
		bin_val+=val
	return bin_val
	
