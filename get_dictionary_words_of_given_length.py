
import enchant
import itertools


MIN_LEN = 3
uk = enchant.Dict("en_UK")
us = enchant.Dict("en_US")


def gen_permutations(ent):
   tuples = map(lambda i: itertools.permutations(ent, i), range(MIN_LEN, len(ent)+1))
   arrr = [["".join(j) for j in i] for i in tuples]
   return list(itertools.chain(*arrr))


def filter_dict(words):
   return [x for x in words if uk.check(x) or us.check(x)]


word = "eollybb"
word_len = 4
word_start = "b"

words = set()
for i in filter_dict(gen_permutations(word)):
   if len(i) >= word_len and i.startswith(word_start):
    words.add(i)

print words