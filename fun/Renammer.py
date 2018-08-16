import os
import csv as csv
from os import rename, listdir

# directory for the questions
fnames = listdir('/Users/liarch29/Desktop/Practice Sheet Generator/questions')

labels = []
# directory for the question classification sheet
with open(
        '/Users/liarch29/Desktop/Practice Sheet Generator/question_classification/Sheet 1-Question classification.csv',
        'rb') as csvfile:
    spamReader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamReader:
        label = ""
    thing = row[0].split(",", 4)
    if len(thing) == 5:
        label += 'Question ' + thing[0] + ' '

        if thing[2] == '-':
            label += 'C '
        else:
            label += 'NC '

        if thing[3] == '-':
            label += "grid-in "

        if "A" in thing[4]:
            label += "Algebra "

        if "G" in thing[4]:
            label += "Geometry "

        if "T" in thing[4]:
            label += "Trigonometry "

        if "P" in thing[4]:
            label += "Passport "

        if "D" in thing[4]:
            label += "Data Analysis "

    if label != 'Question  NC ':
        labels.append(label)  # os.path.abspath('')
# os.rename("/Users/liarch29/Desktop/Practice Sheet Generator/questions/hello.tex","question_0001.tex")

for x, label in enumerate(labels):
    FileName = '/Users/liarch29/Desktop/Practice Sheet Generator/questions/' + fnames[x + 1]
    NewFileName = label

    print(FileName)
    print(NewFileName.strip() + ".tex")
    # os.path.abspath('/Users/liarch29/Desktop/Practice Sheet Generator/questions')
    # print(fnames[x+2])
    # print(labels[x+1])
    os.rename(FileName, NewFileName.strip() + ".tex")
