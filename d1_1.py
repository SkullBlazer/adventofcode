s = input()
L = s.split(" ")
counts = []
count = 0
for i in range(len(L)-2):
    counts.append(int(L[i]) + int(L[i+1]) + int(L[i+2]))
    
for i in range(len(counts)):
    if i == 0:
        continue
    if counts[i] > counts[i-1]:
        count += 1
        
print(count)
