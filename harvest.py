import csv
import codingame
from sys import argv

if  len(argv) != 3:
    print("Usage: ./harvest.sh \"Contest handle\" \"Output file name\"")
    print("The contest handle is the last 39 digits of the contest URL")
    exit()
client = codingame.Client()
try:
    coc = client.get_clash_of_code(argv[1])
except ValueError:
    print("Contest handle not well formatted, --h for help")
    exit()
res = {};
j = 0
for i in coc.players:
    if j > 20:
        break
    res[i.pseudo] = i.rank
    j += 1
res = sorted(res.items(), key=lambda x: x[1])
try:
    with open(argv[2] + ".csv", 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerows(res)
except PermissionError:
    print("Cannot open \"{}.csv\"".format(argv[2]))
    exit()
for i in res:
    print(i[1], ":", i[0])
print("You will find this round top 20 in \"{}.csv\"".format(argv[2]))
