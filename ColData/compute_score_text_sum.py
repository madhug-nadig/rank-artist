import re
import json
from pre_process import pre_process_sum

def text_compute():
	doc_no = pre_process_sum(1)

	regex = r"(?<=\@)(.*?)(?=\$)"

	all_matches_text = list(); to_JSON = list()
	scores = dict.fromkeys(range(doc_no+1), 0)

	for i in range(doc_no):
		scores[i] = (doc_no+2-i)*2

	# print(scores)

	# TEXT_SUM SCORES
	with open('text_sum') as f:
		for i, line in enumerate(f):
			matches = re.findall(regex, line)
			all_matches_text.extend(matches)

	# print(all_matches_text)

	for i in all_matches_text:
		try:
			scores[int(i)]+=1
		except:
			continue

	# print(scores)
	return list(scores.values())

	for index, score in scores.items():
		to_JSON.append({"score":scores[index], "index":index+1})

	print(json.dumps(to_JSON))
	
if __name__ == "__main__":
	text_compute()