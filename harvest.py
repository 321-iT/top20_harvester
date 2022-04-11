import csv
import codingame
from time import sleep
from sys import argv
from api import *

def init_list():
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

	return res

def map_score_and_pseudo(res):
	try:
		with open("score.cfg", 'r', encoding='UTF8') as f:
			reader = csv.reader(f)
			j = 0
			for i in reader:
				if j >= 20:
					break
				res[j] = list(res[j])
				res[j].append(i[1])
				j += 1
	except FileNotFoundError:
		print("No score configuration file, going to next step")
		pass
	except PermissionError:
		print("Cannot open the score configuration file")
		print("\tThis harvesting wont output score in the result")
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
		print("Cannot open the pseudo configuration file")

	return 

def map_coalitions(res, api):
	print("Dealing with 42 API... This operation can take some time.")
	for i in range(len(res)):
		sleep(0.5)
		coalition = call(api, "/users/{}/coalitions".format(res[i][1]))
		coalition = json.loads(coalition)
		for j in coalition:
			if (j['id'] in range(45,49) or j['id'] in range(1,5)):
				res[i].append(j['name'])

def list_to_csv(res):
	try:
		with open(argv[2] + ".csv", 'w', encoding='UTF8') as f:
			writer = csv.writer(f)
			writer.writerows(res)
			error = 0
			return 0
	except PermissionError:
		print("\nCannot open \"{}.csv\": the output cant be saved\n".format(argv[2]))
		return 1

def print_res(res, error):
	for i in res:
		print(i[0], ":", i[1])
	if (error != 1):
		print("You will find this round top 20 in \"{}.csv\"".format(argv[2]))


if __name__ == "__main__":
	try:
		if  len(argv) != 3:
			print("Usage: ./harvest.sh \"Contest handle\" \"Output file name\"")
			print("The contest handle is the last 39 digits of the contest URL:")
			print("Example: 21499132d096a88cf6d6bcdf606295e28bcd6c0")
			exit()
		api = init_api()
		res = init_list()
		map_score_and_pseudo(res)
		map_coalitions(res, api)
		error = list_to_csv(res)
		print_res(res, error)
		exit()
	except KeyboardInterrupt:
		exit()
