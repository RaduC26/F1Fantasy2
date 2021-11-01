from itertools import combinations
from Data.TeamExport import TeamExport


def calculateBestTeam(players_list, budget):
    print("Calculating best team...")
    best_score = 0
    best_combination = None
    all_combinations = combinations(players_list, 6)
    for combination in all_combinations:
        if validateCombination(combination, budget) and getCombinationScore(combination) > best_score:
            best_combination = combination
            best_score = getCombinationScore(combination)
    return best_combination


def bestTeams(players_list, budget, number):
    print("Calculating the best " + str(number) + " teams...")
    best_score = [0] * number
    best_combinations = [0] * number
    all_combinations = combinations(players_list, 6)
    for combination in all_combinations:
        if validateCombination(combination, budget):
            index = evaluateCombination(combination, best_score)
            if index >= 0:
                best_score = updateBestScore(best_score, index, getCombinationScore(combination))
                best_combinations[index] = combination
    return best_combinations


def evaluateCombination(combination, best_score):
    for i in range(len(best_score)):
        if getCombinationScore(combination) > best_score[i]:
            return i
    return -1


def updateBestScore(best_score, i, number):
    for j in range(i, len(best_score) - 1):
        best_score[j + 1] = best_score[j]
    best_score[i] = number
    return best_score


def validateCombination(combination, budget):
    no_of_teams = 0
    for i in range(len(combination)):
        if combination[i].isConstructor():
            no_of_teams += 1
    if (no_of_teams != 1) or (getCombinationPrice(combination) > budget):
        return False
    return True


def getCombinationScore(combination):
    score = 0
    for i in range(len(combination)):
        score += combination[i].getSeasonScore()
    return score


def getCombinationPrice(combination):
    price = 0
    for i in range(len(combination)):
        price += combination[i].getCurrentPrice()
    return price


def printCombination(combination):
    counter = 1
    print("__________________________________________________")
    for i in range(6):
        if not combination[i].isConstructor():
            print("Driver no." + str(counter) + ": " + combination[i].getName() + ". Current price: " + str(
                combination[i].getCurrentPrice()))
            counter += 1
        else:
            temp = combination[i]

    print("Constructor: " + temp.getName() + ". Current price: " + str(temp.getCurrentPrice()))
    print("Combination price: " + str(getCombinationPrice(combination)))


def exportTeam(combination):
    counter = 1
    names = []
    prices = []
    for i in range(len(combination)):
        if not combination[i].isConstructor():
            names.append(combination[i].getName())
            prices.append(round(float(combination[i].getCurrentPrice()), 1))
            counter += 1
        else:
            temp = combination[i]
    names.append(temp.getName())
    prices.append(round(float(temp.getCurrentPrice()), 1))
    return TeamExport(names, prices, round(float(getCombinationPrice(combination)), 1), round(float(getCombinationScore(combination)), 1))
