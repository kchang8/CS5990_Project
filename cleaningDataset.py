import pandas as pd
import re
import string

data_cols = ['score', 'review']

trainDf = pd.read_csv('finalDatasets/smallerCleanTestDataset.csv', usecols=data_cols)

scoreList = []
reviewList = []

cleanTrainList = []
newTrainData = []
newString = ""

for score in trainDf['score']:
    if score != None:
        scoreList.append(score)
for review in trainDf['review']:
    if review != None:
        reviewList.append(review)

for review in reviewList:
    tempString = str(review)
    pattern = r'['+ string.punctuation + ']'
    tempString = re.sub(pattern, '', tempString)

    for i in tempString:
        if i.isalpha() is False and i != " ":
            newString = tempString.replace(i, "")

    cleanTrainList.append(newString)

newTrainData = list(zip(scoreList, cleanTrainList))

csvTrainColumns = ['score', 'review']
trainingData = pd.DataFrame(newTrainData, columns=csvTrainColumns)
trainingData.to_csv('datasets/finalSmallerTestDataset.csv', index=False)
