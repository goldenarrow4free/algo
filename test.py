import subprocess
from random import shuffle, randint

def check(input, output) :
	# out = subprocess.run(['python3', 'main.py'],
	out = subprocess.run(['./a.out'],
		stdout=subprocess.PIPE,
		input=input, encoding="ascii")
	return out.stdout == output
first_line = "11 10\n"
links = [
	[0, 0, 1],
	[1, 1, 2],
	[0, 2, 6],
	[0, 6, 10],
	[0, 6, 8],
	[0, 9, 7],
	[0, 7, 5],
	[1, 5, 4],
	[0, 4, 3],
	[1, 3, 0]
]
exp = "YES\n"*10 + "6\n"

for _ in range(500) :
	shuffle(links)
	for i in range(len(links)):
		if randint(0,1):
			continue
		links[i][1], links[i][2] = links[i][2], links[i][1]

	i = first_line + "\n".join([" ".join([str(c) for c in l]) for l in links])
	if not check(i, exp):
		print(i)
		input()