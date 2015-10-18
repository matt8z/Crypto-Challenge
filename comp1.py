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


#message for wint: '2vy9xq7vg0g6upfgtamtw2ilhgwwtau0s9uptvfvu0tcegtazg3 tmog8hflgptgnmrvvm3xhr.jxehtav wp3rehmbpfsds2pn0w6dcaguw103 s9gq7gg03  .fq7ifs2v dbkaa1gu  wp3ryvmbpetfzrdl0uslc.28ayduu riq.a2m6vsq.qrflb3ue9uwruonepir.28a6ncpsm.78wfv95t9gq7ffnc  uiiaap0aribag7q10byar.78wfrctk9b2revc35g9cmvc2ryptfb2.ahm86ygoo'