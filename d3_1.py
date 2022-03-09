s = input()
L = s.split()
most = ""
for i in range(12):
    temp = ""
    count0 = 0
    count1 = 0
    for j in range(len(L)):
        temp += L[j][i]
    for k in temp:
        if k == "0":
            count0 += 1
        else:
            count1 += 1
    if count0 > count1:
        most += "0"
    else:
        most += "1"
        
print(most)
