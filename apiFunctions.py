import requests
from tqdm import tqdm
import time
import pandas as pd
import string
import steamspypi

steam_key = "4C5D8272E8335F6CDCCE5693E6E8F152"

# data_request = dict()
# data_request['request'] = 'all'
# data_request['page'] = '0'
#
# data = steamspypi.download(data_request)
# print(data)

# Functions goes here:
def get_available_apps_id(steam_key):
  response = requests.get("https://api.steampowered.com/ISteamApps/GetAppList/v2/?key={0}&format=json?json=1".format(steam_key)).json()

  # gets the first 1000 responses, can chnage
  list_response = response['applist']['apps'][:4000]
  result = []
  i = 0
  j = len(list_response) - 1
  pbar = tqdm(total = len(list_response)//2)
  while i <= j:
    app_top = list_response[i]
    app_bot = list_response[j]
    datat = steamspypi.download({'request': 'appdetails', 'appid': app_top['appid']})
    datab = steamspypi.download({'request': 'appdetails', 'appid': app_bot['appid']})
    if datat['price'] is not None:
      result.append(str(app_top['appid']))

    if datab['price'] is not None:
      result.append(str(app_bot['appid']))
    pbar.update(1)
    i += 10
    j -= 10

  return result

def get_app_details(appid):
  res = requests.get("https://store.steampowered.com/api/appdetails?appids={0}".format(appid))
  data = res.json()

  if data is None:
    return None

  if data[appid]['success'] is True:
      try:
        value = data[appid]['data']

        genreList = []
        name = value['name']
        description = value['detailed_description']
        genre = value['genres']

        for x in genre:
            genreList.append(x['description'])
    except KeyError:
        print(appid)
        name = 'None'
        description = 'None'
        genreList.append('None')

    return {
        'Name': name,
        'Detailed Description': description,
        'Genres': genreList,
    }

  return data[appid]['data'] if data[appid]['success'] is True else None

def get_data_keys(input_data):
  if input_data is None:
    return []
  else:
    return input_data.keys()

def get_reviews(appid):
  res = requests.get("https://store.steampowered.com/appreviews/{0}?json=1".format(appid))
  return res.json()

def get_n_reviews(appid, n=50):
  # follow https://andrew-muller.medium.com/scraping-steam-user-reviews-9a43f9e38c92
    reviews = []
    cursor = '*'
    params = {
      'json' : 1,
      'filter' : 'all',
      'language' : 'english',
      'day_range' : 9223372036854775807,
      'review_type' : 'all',
      'purchase_type' : 'all'
    }

    while n > 0:
        params['cursor'] = cursor.encode()
        params['num_per_page'] = min(50, n)
        n -= 50

        response = get_reviews(appid, params)
        cursor = response['cursor']
        reviews += response['reviews']

        if len(response['reviews']) < 50: break

    return reviews

# Pipelines to get data
final_data = {}
def get_reviews_pipeline(steam_key, all_id):
  for ai in tqdm(all_id):
    review = get_n_reviews(ai, 100)
    if len(review) == 100:
      final_data[ai] = review
  return final_data

def get_descriptions_pipeline(final_data):
  for key in final_data.keys():
    description = get_app_details(key)
    if len(review) == 500:
      final_data[ai] = review
  return final_data
