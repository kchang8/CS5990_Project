from apiFunctions import *
import pandas as pd

# datasets for testing
trainingAppList = []    # list that holds all the training app details
testingAppList = []     # list that holds all the test app details

tempTrainDescList = []
tempTestDescList = []
tempTrainReviewList = []
tempTestReviewList = []

allTrainAppDetails = []
allTrainReviews = []

allTestAppDetails = []
allTestReviews = []

# gets all app ids
app_ids = get_available_apps_id(steam_key)
appIdTraining = app_ids[20:30]
appIdTesting = app_ids[30:40]
# print(appIdTesting)

# prev = get_data_keys((get_app_details(app_ids[0])))
# print(prev)

# steam_appid, detailed_description
# gets TRAINING app id details
for data in range(0, len(appIdTraining)):
    print("Training id: " + str(appIdTraining[data]))
    allTrainAppDetails.append(get_app_details(appIdTraining[data]))
    allTrainReviews.append(get_reviews(appIdTraining[data]))
    # if k != prev:
    #   print(k)
#
# # gets TESTING app id details
for data in range(0, len(appIdTesting)):
    print("Testing id: " + str(appIdTesting[data]))
    allTestAppDetails.append(get_app_details(appIdTesting[data]))
    allTestReviews.append(get_reviews(appIdTesting[data]))

for i in allTrainAppDetails:
    if i is not None:
        tempTrainDescList.append(i.get('Detailed Description'))
for i in allTrainReviews:
    if i is not None:
        tempTrainReviewList.append(i.get('Review'))

for i in allTestAppDetails:
    if i is not None:
        tempTestDescList.append(i.get('Detailed Description'))
for i in allTrainReviews:
    if i is not None:
        tempTestReviewList.append(i.get('Review'))

trainingAppList = list(zip(tempTrainDescList, tempTrainReviewList))
testingAppList = list(zip(tempTestDescList, tempTestReviewList))


# writing to training csv files
csvTrainColumns = ['GameDescription', 'Review']
trainingData = pd.DataFrame(trainingAppList, columns=csvTrainColumns)
trainingData.to_csv('trainingDataset.csv', index=False)

# writing to testing csv files
csvTestColumns = ['GameDescription', 'Review']
testingData = pd.DataFrame(testingAppList, columns=csvTestColumns)
testingData.to_csv('testingDataset.csv', index=False)
