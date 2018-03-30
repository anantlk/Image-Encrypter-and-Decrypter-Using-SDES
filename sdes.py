key1='';
key2='';

P10 = (3, 5, 2, 7, 4, 10, 1, 9, 8, 6)
P8 = (6, 3, 7, 4, 8, 5, 10, 9)
P4 = (2, 4, 3, 1)

IP = (2, 6, 3, 1, 4, 8, 5, 7)
IPi = (4, 1, 3, 5, 7, 2, 8, 6)

E = (4, 1, 2, 3, 2, 3, 4, 1)

S0 = [
        [1, 0, 3, 2],
        [3, 2, 1, 0],
        [0, 2, 1, 3],
        [3, 1, 3, 2]
     ]

S1 = [
        [0, 1, 2, 3],
        [2, 0, 1, 3],
        [3, 0, 1, 0],
        [2, 1, 0, 3]
     ]

def permutation(perm, key):
    permutated_key = ""
    for i in perm:
        permutated_key += key[i-1]

    return permutated_key

def generate_first_key(left_key, right_key):
    left_key_rot = left_key[1:] + left_key[:1]
    right_key_rot = right_key[1:] + right_key[:1]
    key_rot = left_key_rot + right_key_rot
    return permutation(P8, key_rot)

def generate_second_key(left_key, right_key):
    left_key_rot = left_key[3:] + left_key[:3]
    right_key_rot = right_key[3:] + right_key[:3]
    key_rot = left_key_rot + right_key_rot
    return permutation(P8, key_rot)

def F(right, subkey):
    expanded_cipher = permutation(E, right)
    xor_cipher = bin( int(expanded_cipher, 2) ^ int(subkey, 2) )[2:].zfill(8)
    left_xor_cipher = xor_cipher[:4]
    right_xor_cipher = xor_cipher[4:]
    left_sbox_cipher = Sbox(left_xor_cipher, S0)
    right_sbox_cipher = Sbox(right_xor_cipher, S1)
    return permutation(P4, left_sbox_cipher + right_sbox_cipher)

def Sbox(input, sbox):
    row = int(input[0] + input[3], 2)
    column = int(input[1] + input[2], 2)
    return bin(sbox[row][column])[2:].zfill(4)

def f(first_half, second_half, key):
     left = int(first_half, 2) ^ int(F(second_half, key), 2)
     #print "Fk: " + bin(left)[2:].zfill(4) + second_half
     return bin(left)[2:].zfill(4), second_half

def encrypt(cipher):
	# parameters
	key = "0111111101"
	p10key = permutation(P10, key)
	left = p10key[:len(p10key)/2]
	right = p10key[len(p10key)/2:]

	first_key = generate_first_key(left, right)
	key1=first_key
	second_key = generate_second_key(left, right)
	key2=second_key
	#print "[*] First key: " + first_key
	#print "[*] Second key: " + second_key

	permutated_cipher = permutation(IP, cipher)
	#print "IP: " + permutated_cipher
	first_half_cipher = permutated_cipher[:len(permutated_cipher)/2]
	second_half_cipher = permutated_cipher[len(permutated_cipher)/2:]

	left, right = f(first_half_cipher, second_half_cipher, key1)
	#print "SW: " + right + left
	left, right = f(right, left, key2) # switch left and right!

	return permutation(IPi, left + right)
	
def decrypt(encrypted):
	key = "0111111101"
	p10key = permutation(P10, key)
	left = p10key[:len(p10key)/2]
	right = p10key[len(p10key)/2:]

	first_key = generate_first_key(left, right)
	key1=first_key
	second_key = generate_second_key(left, right)
	key2=second_key
	#print "[*] First key: " + first_key
	#print "[*] Second key: " + second_key

	permutated_cipher = permutation(IP, encrypted)
	#print "IP: " + permutated_cipher
	first_half_cipher = permutated_cipher[:len(permutated_cipher)/2]
	second_half_cipher = permutated_cipher[len(permutated_cipher)/2:]

	left, right = f(first_half_cipher, second_half_cipher, key2)
	#print "SW: " + right + left
	left, right = f(right, left, key1) # switch left and right!

	return permutation(IPi, left + right)
	
