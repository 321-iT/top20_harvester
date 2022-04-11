import csv
from sys import argv

def my_sort(sub_li):
    l = len(sub_li)
    for i in range(0, l):
        for j in range(0, l-i-1):
            if (sub_li[j][1] < sub_li[j + 1][1]):
                tempo = sub_li[j]
                sub_li[j]= sub_li[j + 1]
                sub_li[j + 1]= tempo
    return sub_li

def init_res():
    res = []
    coalitions = []
    for file in argv:
        try:
            with open(file, 'r') as f:
                reader = csv.reader(f)
                error = 0
                for elem in reader:
                    for i in res:
                        if elem[1] == i[0]:
                            error = 1
                    if error != 1:
                        res.append([elem[1]])
                        coalitions.append([elem[3], elem[2]])
                    error = 0
        except FileNotFoundError:
            if file == "./round*":
                exit("No \"roundX.csv\" files found, exiting")
            print("\n\tFile {} not found, trying the next one\n".format(file))
            pass
        except PermissionError:
            print("Cannot open file {}, trying the next one".format(file))
        
    return res, coalitions

def read_rounds(res):
    for file in argv:
        try:
            with open(file, 'r') as f:
                tmp = []
                reader = csv.reader(f)
                for elem in reader:
                    for i in range(len(res)):
                        if (res[i][0] == elem[1]):
                            res[i].append(elem[2])
                        i += 1
        except FileNotFoundError:
            print("\n\tFile {} not found, trying the next one\n".format(file))
            pass
        except PermissionError:
            print("Cannot open file {}, trying the next one".format(file))

def compile_and_sort_ranking(res):
    for elem in res:
        score = 0
        for i in elem[1:]:
            score += int(i)
        del(elem[2:])
        elem[1] = score
    res = my_sort(res)
    i = 1
    for elem in res:
        score = elem[1]
        name = elem[0] 
        elem[0] = i
        elem[1] = name
        elem.append(score)
        i += 1

def compile_and_sort_coalitions(coalitions):
    final = {'The Alliance' : 0, 'The Assembly' : 0, 'The Order' : 0, 'The Federation' : 0}
    for elem in coalitions:
        final[elem[0]] += int(elem[1])
    coalitions = []
    for i in final.items():
        coalitions.append([i[0], i[1]])
    coalitions = my_sort(coalitions)
    return coalitions

def ranking_to_csv(res):
    try:
        with open("ranking.csv", 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerows(res)
            error = 0
    except PermissionError:
        print("\nCannot open \"{}.csv\": the output cant be saved\n".format(argv[2]))
        error = 1
    for i in res:
        print(i[0], ":", "{} ({})".format(i[1], i[2]))
    if (error != 1):
        print("You will find the final ranking in \"ranking.csv\"")

if __name__ == "__main__":
    try:
        argv = argv[1:]
        res, coalitions = init_res()
        read_rounds(res)
        compile_and_sort_ranking(res)
        ranking_to_csv(res)
        coalitions = compile_and_sort_coalitions(coalitions)
        print(coalitions)
    except KeyboardInterrupt:
        exit()
