from apiFunctions import *
import pandas as pd

# datasets for testing
trainingAppList = []    # list that holds all the training app details
testingAppList = []     # list that holds all the test app details

# gets all app ids
app_ids = get_available_apps_id(steam_key)
appIdTraining = app_ids[:50]
print("id 42: " + appIdTraining[42])
appIdTesting = app_ids[50:100]
# print(appIdTesting)

# prev = get_data_keys((get_app_details(app_ids[0])))
# print(prev)

# steam_appid, detailed_description, genre
# gets TRAINING app id details
for data in range(0, len(appIdTraining)):
    trainingAppList.append(get_app_details(appIdTraining[data]))
    # if k != prev:
    #   print(k)

# gets TESTING app id details
for data in range(0, len(appIdTesting)):
    testingAppList.append(get_app_details(appIdTesting[data]))


# writing to training csv files
csvTrainColumns = ['Name', 'Detailed Description', 'Genres']
trainingData = pd.DataFrame.from_dict(trainingAppList)
trainingData.to_csv('trainingDataset.csv', index=False, columns=csvTrainColumns)

# writing to testing csv files
csvTestColumns = ['Name', 'Detailed Description', 'Genres']
testingData = pd.DataFrame.from_dict(testingAppList)
testingData.to_csv('testingDataset.csv', index=False, columns=csvTestColumns)

# for i in range (0, len(app_ids[:10])):
#   reviews = get_reviews(app_ids[i])
#   print(reviews)
