d = {}
d[0] = ["0"]
d[1] = ["1"]
d[2] = ["A", "B", "C"]
d[3] = ["D", "E", "F"]
d[4] = ["G", "H"]
d[5] = ["J", "K", "L"]
d[6] = ["M", "N"]
d[7] = ["P", "Q", "R", "S"]
d[8] = ["T", "U", "V"]
d[9] = ["W", "X", "Y", "Z"]

print("Enter your phone number:")
try:
	ph_no = str(int(input()))
except:
	ph_no = "2345678910"

l = []
for i in ph_no:
	l1 = []
	flag= 0
	for j in l:
		a = ["", "", "", ""]
		flag = 1
		for k in range(len(d[int(i)])):
			a[k] = j + d[int(i)][k]
			l1.append(a[k])
	if flag == 0:
		for k in range(len(d[int(i)])):
			l1.append(d[int(i)][k])
	l = l1

print("All possible Words: ")
for i in l:
	print(i)
print("No of Words: " + str(len(l)))
