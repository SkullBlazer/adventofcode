s = input()
L = s.split()
forward = 0
depth = 0
aim = 0
for i in range(len(L)):
    if L[i] == "forward":
        forward += int(L[i+1])
        depth += aim*int(L[i+1])
    elif L[i] == "up":
        aim -= int(L[i+1])
    elif L[i] == "down":
        aim += int(L[i+1])
        
print(forward*depth)
