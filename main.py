import argparse, sys
from gensim.models import KeyedVectors

parser = argparse.ArgumentParser()
parser.add_argument("keyword", help="最初の言葉")
parser.add_argument("--num", help="何個出力するか", default=10, type=int)
args = parser.parse_args()

wv = KeyedVectors.load_word2vec_format('wiki.model', binary=True)
try:
    r = wv.most_similar(positive=args.keyword, topn=args.num)
except KeyError:
    sys.exit("word not found")
for w, _ in r:
    print(f"https://ja.wikipedia.org/wiki/{w}")
