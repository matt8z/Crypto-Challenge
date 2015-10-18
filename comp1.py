def e(p,k):
	alphabet = "abcdefghijklmnopqrstuvwxyz1234567890 ."
	crypters = list(k)
	output = ""
	kletter = 0
	for char in p:
		charnum = alphabet.find(char)
		charnum += alphabet.find(crypters[kletter])
		charnum = charnum % len(alphabet)
		output += alphabet[charnum]
		kletter = (kletter + 1) % len(k)
	return output

def d(c,k):
	alphabet = "abcdefghijklmnopqrstuvwxyz1234567890 ."
	decrypters = list(k)
	output = ""
	kletter = 0
	for char in c:
		charnum = alphabet.find(char)
		charnum -= alphabet.find(decrypters[kletter])
		charnum = charnum % len(alphabet)
		output += alphabet[charnum]
		kletter = (kletter + 1) % len(k)
	return output