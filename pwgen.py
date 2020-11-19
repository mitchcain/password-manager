
# logic to generate new passwords of user-specified length

from random import randint

def pwgen(num_char):
	chars = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
			'0', '-', '=', 'q', 'w', 'e', 'r', 't', 'y', 'u', 
			'i', 'o', 'p', '[', ']', '\\', 'a', 's', 'd', 'f', 
			'g', 'h', 'j', 'k', 'l', ';', '\'', 'z', 'x', 'c', 
			'v', 'b', 'n', 'm', ',', '.', '/', '~', '!', '@', 
			'#', '$', '%', '^', '&', '*', '(', ')', '_', '+', 
			'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 
			'{', '}', '|', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 
			'K', 'L', ':', '"', 'Z', 'X', 'C', 'V', 'B', 'N', 
			'M', '<', '>', '?']
	pw = []


	for i in range(num_char):
		ran = randint(0, 93)
		char = chars[ran]
		pw.append(char)
		i += 1

	word = ''.join(pw)
	return word

