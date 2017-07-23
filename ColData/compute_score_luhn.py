import re
import json
from pre_process import pre_process_sum

def luhn_compute():
	doc_no = pre_process_sum(0)

	regex = r"(?<=\@)(.*?)(?=\$)"

	all_matches_luhn = list(); to_JSON = list()
	scores = dict.fromkeys(range(doc_no+1), 0)

	for i in range(doc_no):
		scores[i] = (doc_no+1-i)*2

	# print(scores)

	# LUHN SCORES
	with open('luhn_sum') as f:
		for i, line in enumerate(f):
			matches = re.findall(regex, line)
			all_matches_luhn.extend(matches)

	# print(all_matches_luhn)

	for i in all_matches_luhn:
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
	luhn_compute()