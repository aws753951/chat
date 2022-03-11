def read_file(filename):
	data = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			data.append(line.strip())

	return data
	

def convert(data):
	count_zora = 0
	count_sticker_zora = 0
	count_image_zora = 0
	count_marc = 0
	count_sticker_marc = 0
	count_image_marc = 0
	for line in data: 
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == '陳盈臻':
			if s[2] == '貼圖':
				count_sticker_zora += 1
			elif s[2] == '圖片':
				count_image_zora += 1
			else:
				for m in s[2:]:
					count_zora += len(m)		
		elif name == '朱鴻埕':
			if s[2] == '貼圖':
				count_sticker_marc += 1
			elif s[2] == '圖片':
				count_image_marc += 1
			else:
				for m in s[2:]:
					count_marc += len(m)
	print('zora說的話字數有: ', count_zora, '次', '傳了', count_sticker_zora, '個貼圖', count_image_zora, '圖片')
	print('marc說的話字數有: ', count_marc, '次', '傳了', count_sticker_marc, '個貼圖', count_image_marc, '圖片')


def write_file(filename, data):
	with open(filename, 'w', encoding = 'utf-8-sig') as f:
		for line in data:
			f.write(line + '\n')



def main():
	data = read_file('line.txt')
	data = convert(data)
	# print(data)
	# write_file('line.txt',data)
main()
