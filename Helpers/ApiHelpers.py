import requests
from Data.Driver import Member


def getApiData():
    print("Getting the data from API...")
    request = requests.get("https://fantasy-api.formula1.com/partner_games/f1/players")
    data = request.json()
    return data['players']


def generateMembersList(api_data):
    members = []
    print("Creating drivers and teams profile...")
    for i in range(30):
        price_history = createPriceHistory(api_data[i]['season_prices'])
        name = getMemberName(api_data[i])
        members.append(Member(name, api_data[i]['price'], api_data[i]['season_score'], price_history,
                              api_data[i]['season_score'], api_data[i]['is_constructor']))
    return members


def createPriceHistory(price_list):
    final_list = []
    for i in range(len(price_list)):
        final_list.append(price_list[i]['price'])
    return final_list


def getMemberName(member):
    if member['is_constructor']:
        name = member['team_name']
    else:
        name = member['last_name']
    return name