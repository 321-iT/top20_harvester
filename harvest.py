import csv
import codingame
from sys import argv

if  len(argv) != 3:
    print("Usage: ./harvest.sh \"Contest handle\" \"Output file name\"")
    print("The contest handle is the last 39 digits of the contest URL:")
    print("Example: 21499132d096a88cf6d6bcdf606295e28bcd6c0")
    exit()
client = codingame.Client()
try:
    coc = client.get_clash_of_code(argv[1])
except ValueError:
    print("Contest handle not well formatted, --h for help")
    exit()
except codingame.exceptions.ClashOfCodeNotFound:
    print("Contest not found. Please check the handle you entered (--h for help)")
    exit()
res = {};
j = 0
for i in coc.players:
    if j >= 20:
        break
    res[i.rank] = i.pseudo
    j += 1
res = sorted(list(res.items()))
try:
    with open("points.cfg", 'r', encoding='UTF8') as f:
        reader = csv.reader(f)
        j = 0
        for i in reader:
            if j >= 20:
                break
            res[j] = list(res[j])
            res[j].append(i[1])
            j += 1
except FileNotFoundError:
    print("No points configuration file, going to next step")
    pass
except PermissionError:
    print("Cannot open the configuration file")
    print("\tThis harvesting wont output points in the result")
try:
    with open("pseudo.cfg", 'r', encoding='UTF8') as f:
        reader = csv.reader(f)
        j = 0
        for pseudo in reader:
            for i in range(len(res)):
                if res[i][1] == pseudo[0]:
                    res[i][1] = pseudo[1]
                i += 1
except FileNotFoundError:
    print("No pseudo configuration file, going to next step")
    pass
except PermissionError:
    print("Cannot open the configuration file")
    print("\tThis harvesting wont output points in the result")

try:
    with open(argv[2] + ".csv", 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerows(res)
        error = 0
except PermissionError:
    print("\nCannot open \"{}.csv\": the output cant be saved\n".format(argv[2]))
    error = 1
for i in res:
    print(i[0], ":", i[1])
if (error != 1):
    print("You will find this round top 20 in \"{}.csv\"".format(argv[2]))
