leftlist = []
rightlist = []

input = open('input.txt')

distance = 0

# process the data

for line in input.readlines():
    split = line.split(' ')
    leftlist.append(int(split[0]))
    rightlist.append(int(split[3]))

# Sort it
leftlist.sort()
rightlist.sort()

index = 0
for i in leftlist:
    diff = abs(i - rightlist[index])
    distance += diff
    index += 1

print(distance)