data = []
with open('line.txt', 'r', encoding = 'utf-8-sig') as f:
	for line in f:
		data.append(line.strip())

new = []
for line in data:
	s = line.split(' ')
	time = s[0][:5]
	name = s[0][5:]
	print(name)
