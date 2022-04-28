word = input()
count = 0

if (word.find('c=') != -1):
    count += word.count('c=')
    word = word.replace('c=','1')
if (word.find('c-') != -1):
    count += word.count('c-')
    word = word.replace('c-','1')
if (word.find('dz=') != -1):
    count += word.count('dz=')
    word = word.replace('dz=','1')
if (word.find('d-') != -1):
    count += word.count('d-')
    word = word.replace('d-','1')
if (word.find('lj') != -1):
    count += word.count('lj')
    word = word.replace('lj','1')
if (word.find('nj') != -1):
    count += word.count('nj')
    word = word.replace('nj','1')
if (word.find('s=') != -1):
    count += word.count('s=')
    word = word.replace('s=','1')
if (word.find('z=') != -1):
    count += word.count('z=')
    word = word.replace('z=','1')

word = word.replace('1','')
count += len(word)
print(count)