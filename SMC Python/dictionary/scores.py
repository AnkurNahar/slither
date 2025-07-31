students_scores = {
    "Brian": [94, 89, 92],
    "Rachel": [100, 90, 65],
    "Jon": [67.5, 95, 100],
    "Brit": [0, 78, 80],
    "Greg": [65, 100, 78],
    "Andrea": [55.5, 67, 79]
}

print('problem 1: ')
def showScores(score_dict):
    for name, scores in score_dict.items():
        print(f"{name}: {scores}")

showScores(students_scores)

print('\nproblem 2: ')
def showScoresUsingKey(score_dict):
    keys = list(score_dict.keys())
    for i in range(len(keys)):
        name = keys[i]
        print(f"{name}: {score_dict[name]}")

showScoresUsingKey(students_scores)


print('\nproblem 3: ')
def showStudetsSedondScore(score_dict, name):
    print(f"{name}'s second score: {score_dict[name][1]}")

showStudetsSedondScore(students_scores, "Rachel")


print('\nproblem 4:')
def createAverageDict(score_dict):
    avg_dict = {}
    for name, scores in score_dict.items():
        avg_dict[name] = sum(scores) / len(scores)

    for name, avg in avg_dict.items():
        print(f"{name}: {avg}")

createAverageDict(students_scores)