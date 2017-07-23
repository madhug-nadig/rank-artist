import subprocess
import language_check
import json

def lang_check():
	error_dict = {'Miscellaneous':1, 'Grammar':2, 'Capitalization':1, 'Redundant Phrases':.5, 'Possible Typo':0.25}

	tool = language_check.LanguageTool('en-US')

	query = list(open('query.txt', 'r'))[0]

	doc_no = -1; result = list(); a = list(); to_JSON = list()

	with open(query + '.txt') as f:
		for i, line in enumerate(f):
			if(len(line) < 10):
				continue
				
			if(line[:10] == "Data from:"):
				doc_no+=1; result.append(100); continue;
			
			# print("Line" + str(i)) #PLEASE COMMENT IN FINAL
			matches = tool.check(line)
			# print(doc_no)
			for j in matches:
				try:
					result[doc_no]-=error_dict[j.category]
				except:
					continue

	return(result)
	for i, score in enumerate(result):
		to_JSON.append({"score":score, "index":i})

	print(json.dumps(to_JSON))
	
if __name__ == "__main__":
	lang_check()