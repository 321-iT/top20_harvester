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
                        res.append([elem[1], elem[3]])
                    error = 0
        except FileNotFoundError:
            if file == "./round*":
                exit("No \"roundX.csv\" files found, exiting")
            print("\n\tFile {} not found, trying the next one\n".format(file))
            pass
        except PermissionError:
            print("Cannot open file {}, trying the next one".format(file))
    return res

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
        for i in elem[2:]:
            score += int(i)
        del(elem[3:])
        elem[2] = elem[1]
        elem[1] = score
    res = my_sort(res)
    i = 1
    for elem in res:
        score = elem[2]
        name = elem[0]
        coa = elem[1]
        elem[0] = i
        elem[1] = name
        elem[2] = coa
        elem.append(score)
        i += 1

def compile_and_sort_coalitions(res):
    final = {'The Alliance' : 0, 'The Assembly' : 0, 'The Order' : 0, 'The Federation' : 0}
    for elem in res:
        if (elem[3] == "Unknown user or Coalition"):
            continue
        final[elem[3]] += int(elem[2])
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
    
    return error

def print_ranking(res):
    for i in res:
        if (int(i[2]) == 0):
            break
        spaces_name = ""
        spaces_number = ""
        spaces_score = ""
        if (len(i[1]) < 8):
            for j in range(8 - len(i[1])):
                spaces_name += " "
        if (i[0] < 10):
            spaces_number = " "
        if (i[2] < 1000):
            spaces_score = " "
        print(i[0],":",spaces_number,"{}{} - {} {}- ({})".format(i[1],spaces_name,i[2],spaces_score,i[3]))

def print_coa(coalitions):
    print(" == Coalitions ranking : == \n")
    for elem in coalitions:
        print("\t{} : {} points".format(elem[0], elem[1]))

if __name__ == "__main__":
    try:
        argv = argv[1:]
        res = init_res()
        read_rounds(res)
        compile_and_sort_ranking(res)
        error = ranking_to_csv(res)
        print_ranking(res)
        coalitions = compile_and_sort_coalitions(res)
        print_coa(coalitions)
        if (error != 1):
            print("\nYou will find the final ranking in \"ranking.csv\"")
    except KeyboardInterrupt:
        exit()
