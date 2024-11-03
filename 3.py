f1 = open("raqamlar.txt", "w")
f1.write("1,2,3,4,5,6,7,8,9,10")
f1.close()

f1 = open("raqamlar.txt", "rt")
sonlar = f1.read()
soni = 0
for i in sonlar:
    if i.isdigit():
        soni += 1
        
print("nechi raqam borligi", soni)
f1.close()