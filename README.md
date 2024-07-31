# collect-knowledge
## 使い方
### 試行済環境
windows 11 (x86_64)  
rye 0.34.0
### シェルでの実行例
```sh
git clone https://github.com/shizukani-cp/collect_knowledge.git
cd collect_knowledge
rye sync -f
rye run python ck.py 単語
rye run python ck.py 単語 --num 20
```