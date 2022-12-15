import re
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import TreebankWordTokenizer

dataset = {}
usernamelist = []

with open('chatlogs.csv', 'r', encoding='utf-8') as log:

    log.readline()

    for line in log:
        colList = line.split(',', 4)
        username = colList[2]
        username = username.replace('"', "")

        if username not in dataset:
            usernamelist.append(username)
            dataset[username] = [colList[4]]
        else:
            dataset[username].append(colList[4])

for username in dataset:  #clean text data, remove links and characters left over from csv
    dataset[username] = list(map(lambda x: x.replace("'", ""), dataset[username]))
    dataset[username] = list(map(lambda x: x.replace('"', ""), dataset[username]))
    dataset[username] = list(map(lambda x: x.replace(',', ""), dataset[username]))
    dataset[username] = list(map(lambda x: x.replace('\n', ""), dataset[username]))
    dataset[username] = list(map(lambda x: re.sub(r'http\S+', '', x), dataset[username]))
   
with open('clean.txt', 'w', encoding='utf-8') as f:
    for username in dataset:
        if len(dataset[username]) > 100:
            for msg in dataset[username]:
                if len(msg) > 0:
                    f.write(username)
                    f.write(' ')
                    f.write(msg)
                    f.write(' ')
                    f.write('\n')


