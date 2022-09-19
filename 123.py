import json
import collections
import xml.etree.ElementTree as ET

def read_json(path, max_len_word=6, top_words=10):
	with open(path, encoding='utf-8') as news_file:
		news = json.load(news_file)
		description_words = []
		for item in news['rss']['channel']['items']:
			description = [word for word in item['description'].split(' ') if len(word) > max_len_word]
			description_words.extend(description)
			counter_words = collections.Counter(description_words)
		print(counter_words.most_common(top_words))

def read_xml(path, max_len_word=6, top_words=10):
	parser = ET.XMLParser(encoding='utf-8')
	tree = ET.parse(path, parser)
	root = tree.getroot()
	description_words = []
	xml_descriptions = root.findall('channel/item')
	for xmli in xml_descriptions:
		description = [word for word in xmli.find('description').text.split(' ') if len(word) > max_len_word]
		description_words.extend(description)
		counter_words = collections.Counter(description_words)
	print(counter_words.most_common(top_words))

					
if __name__ == '__main__':
	read_json('newsafr.json')
	read_xml('newsafr.xml')
