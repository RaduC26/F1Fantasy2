from Helpers.ApiHelpers import getApiData, generateMembersList
from Helpers.CombinationHelpers import calculateBestTeam, bestTeams, printCombination, exportTeam


def calculate():
    api_data = getApiData()
    members = generateMembersList(api_data)

    best_combination = calculateBestTeam(members, 103.1)

    best_combinations = bestTeams(members, 103.1, 3)
    for i in range(3):
        printCombination(best_combinations[i])
    return exportTeam(best_combination)


def calculateBestTeams(budget, number_of_teams):
    api_data = getApiData()
    members = generateMembersList(api_data)

    list_of_best_teams = []
    best_combinations = bestTeams(members, budget, number_of_teams)
    for i in range(number_of_teams):
        list_of_best_teams.append(exportTeam(best_combinations[i]))

    return list_of_best_teams
