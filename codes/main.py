import os
from collections import defaultdict

with open('Bive-main/badword.txt', encoding='utf-8') as infile:
    badwords = infile.read().split('\n')


os.chdir("Bive-main/kurdish news data")
output = ''
for file in os.listdir():
    wordcount=defaultdict(int)
    with open(file, encoding='utf-8') as infile:
        words = infile.read()
        words.replace('\n', '')
        words = words.split(' ')
        for word in words:
            wordcount[word] += 1
    
    output += file + '\n'
    for badword in badwords:
        output += f'\t{badword}: {wordcount[badword]}\n'
    output += '\n'

    with open('../output.txt', 'w', encoding='utf-8') as o:
        o.write(output)