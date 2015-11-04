from os import listdir, popen
from os.path import isfile, join

files = [ f for f in listdir('data') if isfile(join('data', f)) ]

for file in files:
	if file[0] is not '.':
		prefix = file[:-4]

		f = open('data/' + file, 'r')
		content = f.readlines()
		f.close()

		for index, line in enumerate(content):
			data = line[13:-2]
			cmd = './thirst 5 ' + data + '> solutions/' + prefix + str(index) + '.txt'
			print(cmd)
			popen(cmd)	