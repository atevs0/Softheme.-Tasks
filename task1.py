line = []
with open('INPUT.txt') as f:
        line = f.read()

count = 0
ones = '1'

for i in range(len(line)):
    if ones in line:
        count += 1
    else:
        break
    ones += '1'

fout = open('OUTPUT.txt', 'w')
fout.write("The length of the longest continuous sequence of units = ")
fout.write(str(count))
fout.close()
    
