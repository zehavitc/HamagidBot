# -*- coding: utf-8 -*-
import wikipedia
import random
from BeautifulSoup import BeautifulSoup
import urllib2
import codecs


def get_category(word):
    wikipedia.set_lang('He')
    res = wikipedia.search(word, 10, True)
    if len(res[0]) != 0:
        title = res[0][0]
        if is_category(title) is None:
            return random.choice(res[0])
        return get_catageories_helper(title)
    else:
        if res[1] is not None:
            return get_catageories_helper(res[1][0])

def is_category(title):
    try:
        page = wikipedia.WikipediaPage(title)
        return page
    except:
        return None

def get_catageories_helper(title):
    try:
        catagories = wikipedia.WikipediaPage(title).categories
        if len(catagories) != 0:
            catagories = filter(lambda a:  u'קצרמר' not in a and u'ערכים' not in a and u'דפים עם' not in a, catagories)
            # lens = []
            # for category in catagories:
            # res = wikipedia.page(category)
            # lens = [len(res.links)]
            # max_len = max(lens)
            # idx = [i for i, x in enumerate(lens) if x == max(max_len)]
            # max_category = catagories[random.choice(idx)]
            if len(catagories) != 0:
                return random.choice(catagories).replace(u'קטגוריה', u'').replace(u':', u'')
        return "זה"
    except:
        return title



def get_info_box_data(word):
    wikipedia.set_lang('He')
    res = wikipedia.search(word, 10, True)
    title = res[0][0]
    html_page = wikipedia.page(title).html()
    soup = BeautifulSoup(html_page)
    info_table = soup.find("table", {"class": "infobox"})
    info = []
    current_tuple = tuple()
    rows = info_table.findChildren(['th', 'tr', 'td'])

    for row in rows:
        result = ""
        row_title = get_title(row)
        values = row.findChildren('a')
        if len(values) == 0: continue
        for value in values:
            # value = cell['content']
            # print "The value in this cell is %s" % value
            for content in value.contents:
                if 'img' in content: continue
                result += " " + (str)(content)
        if 'img' in result: continue
        print(row_title)
        print(result)
        print("-------------------")


def get_title(element):
    children = element.findChildren()
    for child in children:
        if child.string is not None:
            return child.string


# word = "כלי עבודה"
#word = "שחקני קולנוע וטלוויזיה אמריקאים"
#print(get_category(word))
#get_category(word)
# get_info_box_data('בראד פיט')
# res=wikipedia.suggest('ביבי')
# print(res)
# get_info_box_data('אלברט איינשטיין')

