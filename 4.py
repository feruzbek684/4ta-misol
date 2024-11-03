import random

def son_file():
    raqam = open("raqamlar.txt", "w")
    for i in range(int(input("N: "))):
        son = random.randint(5, 60)
        raqam.write(str(son))
        raqam.write(" ")
    print("Faylga ma'lumot yozildi")
    raqam.close()

son_file()

ls = []
f = open("raqamlar.txt")
data = f.read()
for i in data.split():
    ls.append(int(i))
f.close()

tub = open("tubsonlar.txt", "w")
for i in ls:
    soni = 0
    index = 1
    while index <= i:
        if i % index == 0:
            soni += 1
        index += 1
    if soni == 2:
        tub.write(str(i))
        tub.write(" ")
tub.close()
