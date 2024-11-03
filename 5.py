f1 = open("raqamlar.txt", "rt")
harflar = f1.read()
unli = 0
for i in harflar:
    if i.isalpha():
        if i == 'a' or i == 'A' or i == 'i' or i == 'I' or i == 'e' or i == 'E' or i == 'o' or i == 'O' or i == 'u' or i == 'U':
            unli += 1
print("unli harflar soni ==> ", unli)   
f1.close()