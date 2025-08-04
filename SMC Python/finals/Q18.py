def calculateLast2BMIs(heights, weights):

    second_last_height = heights[-2]
    second_last_weight = weights[-2]
    second_last_bmi = second_last_weight/(second_last_height ** 2)

    last_height = heights[-1]
    last_weight = weights[-1]
    last_bmi = last_weight/(last_height ** 2)

    return round(second_last_bmi, 2), round(last_bmi, 2)

heights = [1.47, 1.5, 1.52, 1.55, 1.57, 1.6, 1.63, 1.65, 1.68, 1.7, 1.73, 1.75, 1.78, 1.8, 1.83, 1.81, 2.20]
weights = [52.21, 53.12, 54.48, 55.84, 57.2, 58.57, 59.93, 61.29, 63.11, 64.47, 66.28, 68.1, 69.92, 72.19, 74.46, 49.12, 85.65]
second_last_bmi, last_bmi = calculateLast2BMIs(heights, weights)

print(f"second last BMI: {second_last_bmi}")
print(f"last BMI: {last_bmi}")