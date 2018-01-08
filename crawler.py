'''
This is a crawler for "Акселератор адаптации" in HSE
'''

from urllib import parse
from urllib import request
from lxml import html
from bs4 import BeautifulSoup

ROOT = 'https://www.hse.ru/firstyear/'

def root_walker():
	sections = ['majordiff', 'fees', 'knowledge', 'diploma', 'transfer',
	'dorms', 'library', 'socsupport', 'entertainment']
	content = one_page(ROOT + sections[0])
	# print(content)


def one_page(link):
	page = request.urlopen(link).read().decode('utf-8')
	tree = html.fromstring(page)
	cnt = tree.xpath('.//div[@class="content"]')
	# cnt = html.tostring(cnt[0], encoding='utf-8')
	# txt = BeautifulSoup(cnt, 'html.parser').get_text()
	# print(txt)
	pars = cnt[0].xpath('.//p')
	for p in pars[2:]:
		p = html.tostring(p, encoding= 'utf-8')
		txt = BeautifulSoup(p, 'html.parser').get_text()
		print(txt)
		print('--*--')
	return page

root_walker()