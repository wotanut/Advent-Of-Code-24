leftlist = []
rightlist = []

input = open('input.txt')

similartiy = 0

# process the data

for line in input.readlines():
    split = line.split(' ')
    leftlist.append(int(split[0]))
    rightlist.append(int(split[3]))

# Sort it
# leftlist.sort()
# rightlist.sort()

index = 0
for i in leftlist:
    similartiy += i * rightlist.count(i)

    index += 1

print(similartiy)