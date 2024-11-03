f1 = open("raqamlar.txt", "w")
f1.write("1,2,3,4,5,6,7,8,9,10, salom yaxshimisan nima gaolar assalomu alekum")
f1.close()

f1 = open("raqamlar.txt", "rt")
sonlar = f1.read()
yig = 0
ls = []
for i in sonlar:
    if i.isdigit():
        ls.append(int(i))
print(ls)

for i in ls:
    if i % 2 == 0:
        yig = yig + i
print("juft sonlar yigindisi", yig)
f1.close()