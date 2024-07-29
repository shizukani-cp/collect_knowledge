import argparse, sys
import requests
from gensim.models import KeyedVectors

parser = argparse.ArgumentParser()
parser.add_argument("keyword", help="最初の言葉")
parser.add_argument("--num", help="何個出力するか", default=10, type=int)
args = parser.parse_args()

wv = KeyedVectors.load_word2vec_format('wiki.model', binary=True)
try:
    r = wv.most_similar(positive=args.keyword, topn=args.num - 1)
except KeyError:
    sys.exit("word not found")
r = [args.keyword] + r

datas = ""
for w, _ in r:
    url = "https://ja.wikipedia.org/api/rest_v1/page/summary/" + w
    try:
        # APIにリクエストを送信してデータを取得
        response = requests.get(url)
        data = response.json()

        # サマリーの取得
        if 'extract' in data:
            datas += data['extract']
            print(data["extract"])
        else:
            sys.exit(f"{w}の情報が見つかりませんでした。")

    except requests.exceptions.RequestException as e:
        sys.exit("エラーが発生しました: " + str(e))
