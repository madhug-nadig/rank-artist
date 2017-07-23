import urllib.request
from urllib import parse
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re
import json
from check import lang_check
from compute_score_luhn import luhn_compute
from compute_score_text_sum import text_compute
from pre_process import pre_process_sum
from topic_modelling import topic_model

def get_url(query):
        qarr = query.split()
        q = [x for x in qarr]
        query = "http://duckduckgo.com/html/?q=" + '+'.join(q)
        return query

def get_links(query):
        search_url = get_url(query)
        site = urllib.request.urlopen(search_url)
        data = site.read()
        the_links = []
        parsed = BeautifulSoup(data)
        for links in parsed.findAll('div', {'class': re.compile('links_main*')}):
                the_links.append(links.a['href'])
        return the_links

def file_write(qry,u ,op, i):
        i =  qry+ ".txt"
        file = open(i, "a", encoding='utf-8')
        file.write('\nData from: ' + u + '\n \n')
        file.write(op)
        file.write('\n \n')
        file.close()

def get_data(qry,u, i):
		if u[28] == 'F':
			u = "https://" + u[29:]
		else:
			u = "http://" + u[28:]
		u=parse.unquote(u)
		print(u)
		op = ""
		try:
			theurl = Request(u, headers = {'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' })
			html=urllib.request.urlopen(theurl)
			data = html.read().decode('utf-8', 'ignore')
			soup=BeautifulSoup(data, 'html.parser')
			res = [i.text.replace('\n', ' ').strip() for i in soup.find_all('p')]
			for p in res:
					op = op + p + '\n'
			file_write(qry, u,op, i)
			return BeautifulSoup(data).title.string
		except Exception as e:
			print("Execption: ", e)

def get_queries():
        try:
            f = open('query.txt', 'r')
            qs = f.readlines()
            f.close()
            qs = list(map(lambda s: s.strip(), qs))
            print(qs)
            return qs
        except IOError as e:
            print("\nPlease choose the correct path for query.txt! ")

def main():
	queries = get_queries()
	all_titles = list()
	if queries:
		for iter in range(len(queries)):
				query = queries[iter]
				url = get_links(query)
				for i in range(16):
					if i< len(url):
						all_titles.append(get_data(query, url[i], i))
	return all_titles

if __name__ == "__main__":
	titles = main()
	lang_res = lang_check()
	luhn_res = luhn_compute()
	text_res = text_compute()
	topic_res = topic_model()
	
	result_JSON = list()
	
	query = list(open('query.txt', 'r'))[0]
	lines = list(open(query + '.txt', 'r'))
	doc_no = -1; link = ''; content = ''; flag = 0
	for line in lines:
		if(len(line) < 5):
			continue
		if(line[:10] == "Data from:"):
			flag = 0
			content = '';
			doc_no+=1
			link = line[10:].strip()
			continue
		content = content + line.strip()
		if(len(content) > 90 and flag!=1):
			flag = 1
			result_JSON.append({"content":content, "link":link, "title":titles[doc_no], "score":(lang_res[doc_no]*.2 + luhn_res[doc_no]*.2 + text_res[doc_no]*.2 + topic_res[doc_no]*.4)})
	print(json.dumps(result_JSON))
	
	
	
	