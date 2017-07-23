'''Make MOD's to the crawler to write each links data to a different file'''
import pprint
import gensim
import collections
from collections import defaultdict
from gensim import corpora, models, similarities
from pprint import pprint
import os 

def topic_model():
	result = {}
	list_of_documents = []
	query = list(open('query.txt', 'r'))[0]
	lines = list(open(query + '.txt', 'r'))
	file_no = 0
	f = open("sep/1.txt", 'w')
	for line in (lines):
		if(line[:10] == "Data from:"):
			f.close()
			file_no+=1
			f = open("sep/"+str(file_no)+".txt", 'w')
			continue
		print(line, file = f)

	for files in os.listdir("./sep/"):
		f = open("./sep/"+files, "r")
		list_of_documents.append(f.read().replace('\n', ' ').strip())
	#print("Number of Documents:", end = ' ')
	#print(len(list_of_documents))
	stoplist = set('for a of the and to in'.split())
	texts = [[word for word in document.lower().split() if word not in stoplist] for document in list_of_documents]
	#print(stoplist)
	#print(texts)
	frequency = defaultdict(int)
	for text in texts:
		for token in text:
			frequency[token] += 1
	texts = [[token for token in text if frequency[token] > 1] for text in texts]
	''' test '''
	#print("Words which are semantically checked.....")
	#pprint(texts)
	dictionary = corpora.Dictionary(texts)
	#print(dictionary)
	#print(dictionary.token2id)
	new = open("query.txt", "r")
	query = new.read()
	#print(query)
	new_query_vec = dictionary.doc2bow(query.lower().split())
	#print(new_query_vec)
	corpus = [dictionary.doc2bow(text) for text in texts]
	#corpora.MmCorpus.serialize('/home/lorick/Desktop/Topic.mm', corpus)
	tfidf = models.TfidfModel(corpus)
	corpus_tfidf = tfidf[corpus]
	lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=250)
	corpus_lsi = lsi[corpus_tfidf]
	#print(lsi.print_topics(2))
	vec_lsi = lsi[new_query_vec]
	#print(vec_lsi)
	index = similarities.MatrixSimilarity(lsi[corpus])
	sims = index[vec_lsi]
	#print(list(enumerate(sims)))
	sims = sorted(enumerate(sims), key=lambda item: -item[1])
	#print(sims)
	#lda_model = models.LdaModel(corpus, id2word=dictionary, num_topics=100)
	#print(lda_model.print_topics(20))
	result = dict(sims)
	#print(result_json)
	result_json = {}
	for key in result:
		key += 1
		result_json[key] = result[key-1] 
	actual_result = []
	for i in result_json:
		actual_result.append(result_json[i]*100)
		#actual_result["index"] = i
	print(actual_result)
if __name__ == "__main__":
	topic_model()
