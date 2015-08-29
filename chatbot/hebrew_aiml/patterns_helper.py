# -*- coding: utf-8 -*-
__author__ = 'zehavitc'


def ngrams(input, n):
    input = clean_input(input).split()
    output = []
    for i in range(len(input) - n + 1):
        output.append(' '.join(c for c in input[i:i + n]))
    return output

def ngrams_old(input, n):
  input = input.split()
  output = []
  for i in range(len(input)-n+1):
    output.append(' '.join(c for c in input[i:i+n]))
  return output

def clean_input(input):
    characters_to_remove = [u',', u'.', u'?', u':', u';']
    return ''.join(c for c in input if c not in characters_to_remove)

n = ngrams_old(u"ביבי הזה",1)
n = ngrams(u"ביבי הזה",1)
print(n)
