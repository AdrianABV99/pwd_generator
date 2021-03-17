from hashlib import sha256
import random


def get_hexdigest(salt,plaintext):
	return sha256((salt+plaintext).encode('utf-8')).hexdigest()

def password(name, app_name, plaintext):
	salt = get_hexdigest(name, app_name)
	hex = get_hexdigest(salt, plaintext)[:50]
	ALPHABET = ('abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTYVWXYZ', '0123456789', '(,._-*~"<>/|!@#$%^&)+=')
	
	dec = int(hex, 16)
	length = random.randint(8,16)
	pwd = []

	while len(pwd) < length:
		n = random.randint(0, len(ALPHABET)-1)
		a = ALPHABET[n]
		n = random.randint(0, len(a)-1)
		pwd.append(a[n])

	return ''.join(pwd)



		



