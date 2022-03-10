def read_file(filename):
	data = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			data.append(line.strip())
	return data

def convert(data):
	new = []
	person = None
	for line in data: 
		if line == '蔡妙涵' or '女少氵函' in line:
			person = '蔡妙涵'
			continue
		elif line == '你傳送了':
			person = '朱鴻埕'
			continue
		elif '週' in line:
			continue
		if person:
			new.append(person + ': ' + line)
	return new

def write_file(filename, data):
	with open(filename, 'w', encoding = 'utf-8-sig') as f:
		for line in data:
			f.write(line + '\n')



def main():
	data = read_file('input.txt')
	data = convert(data)
	print(data)
	write_file('output.txt',data)
main()
