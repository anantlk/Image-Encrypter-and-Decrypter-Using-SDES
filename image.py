import numpy as np
import cv2
import sdes
import dec_to_bin
import bin_to_dec

def encrypt_image(path):
	c=0
	img_matrix=cv2.imread(path)
	for i in range(0,len(img_matrix)):
		for j in range(0,len(img_matrix[i])):
			for k in range(len(img_matrix[i][j])):
				c=c+1
				print(c)
				original_bin=dec_to_bin.binary(img_matrix[i][j][k])
				encrypted_bin=sdes.encrypt(original_bin)
				img_matrix[i][j][k]=bin_to_dec.decimal(encrypted_bin)	

	print(c)
	cv2.imshow("image",img_matrix)
	cv2.imwrite("encrypted.png",img_matrix)
	cv2.waitKey()
	
def decrypt_image(path):
	c=0
	img_matrix=cv2.imread(path)
	for i in range(0,len(img_matrix)):
		for j in range(0,len(img_matrix[i])):
			for k in range(len(img_matrix[i][j])):
				c=c+1
				print(c)
				original_bin=dec_to_bin.binary(img_matrix[i][j][k])
				decrypted_bin=sdes.decrypt(original_bin)
				img_matrix[i][j][k]=bin_to_dec.decimal(decrypted_bin)
				
	cv2.imshow("image",img_matrix)
	cv2.waitKey()


