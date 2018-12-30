from random import shuffle

pairs = []
for i in range(0, 1000):
	pairs.append([str(i), str(i * 2)])

shuffle(pairs)

f1 = open('multiplication_input.csv', 'w')
f2 = open('multiplication_output.csv', 'w')

for item in pairs:
	f1.write(item[0] + '\n')
	f2.write(item[1] + '\n')

f1.close()
f2.close()