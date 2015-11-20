from instruments import SAMPLES as samp

for i in samp:
	print(i + ":")
	instrument = samp[i]
	for c in instrument:
		print("    " + c + ":")
		cat = instrument[c]
		names = []
		for d in cat:
			names.append(d)
		l = len(cat[names[0]])
		for i in range(1, len(names)):
			assert len(cat[names[i]]) == l
			print("    " * 2 + names[0] + ' -=-> ' + names[i])

print("passed")