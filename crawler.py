'''
This is a crawler for "Акселератор адаптации" in HSE
'''

from urllib import parse
from urllib import request
from lxml import html
from bs4 import BeautifulSoup

ROOT = 'https://www.hse.ru/firstyear/'

def root_walker():
	sections = ['fees', 'knowledge', 'diploma', 'transfer', 'dorms', 'library']
	sections = ['fees']
	for sec in sections:
		print(sec + '\n\n')
		content = one_page(ROOT + sec)
		with open(sec, 'w') as f:
			f.write(content)


def one_page(link):
	page = request.urlopen(link).read().decode('utf-8')
	tree = html.fromstring(page)
	cnt = tree.xpath('.//div[@class="content"]')
	pars = cnt[0].xpath('.//p')
	cont = []
	for p in pars[2:]:
		p = html.tostring(p, encoding= 'utf-8')
		txt = BeautifulSoup(p, 'html.parser').get_text()
		print(txt)
		print('--*--')
		cont.append(txt)
	return '\n\n'.join(cont)


def plain_page_parse(): # TODO: socsupport, entertainment
	page = request.urlopen(ROOT + 'majordiff').read().decode('utf-8')
	tree = html.fromstring(page)
	cnt = tree.xpath('.//div[@class="content"]')
	pars = cnt[0].xpath('.//p')
	cont = []
	for p in pars[2:]:
		p = html.tostring(p, encoding= 'utf-8')
		txt = BeautifulSoup(p, 'html.parser').get_text()
		print(txt)
		print('--*--')
		cont.append(txt)
	with open('majordiff', 'w') as f:
			f.write('\n--*--\n'.join(cont))


root_walker()