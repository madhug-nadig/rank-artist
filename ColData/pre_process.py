import subprocess
import optparse

def pre_process_sum(mode):
	query = list(open('query.txt', 'r'))[0]

	lines = list(open(query + '.txt', 'r'))

	doc_no = -1

	f = open('formatted_file', 'w')
	for line in lines:
		if(len(line) < 10):
			continue
		if(line[:10] == "Data from:"):
			doc_no+=1
			print
			continue
			
		line = line.strip()
		line = line + ' @' + format(doc_no, '03d') + '$'
		
		print (line, file = f)
		
	# print(doc_no)

	print(len(lines), file = f)

	if(mode == 0):
		subprocess.call("./gen_luhn.sh")
	if(mode == 1):
		subprocess.call("./text_sum.sh")

	return doc_no
	f.close() 

if __name__ == "__main__":
	parser = optparse.OptionParser()

	parser.add_option('-l', '--luhn',
		action="store_const", const=0, dest="verbose",
		help="Generates Luhn Summary")
	parser.add_option('-t', '--text',
		action="store_const", const=1, dest="verbose",
		help="Generates Text-Sum Summary")
	
	options, args = parser.parse_args()

	pre_process_sum(options.verbose)