import codingame
from sys import argv

client = codingame.Client()
coc = client.get_pending_clash_of_code()
coc = client.get_clash_of_code(argv[1])
res = {};
for i in coc.players:
    res[i.pseudo] = i.rank
res = sorted(res.items(), key=lambda x: x[1])
for i in res:
    print(i[0])
