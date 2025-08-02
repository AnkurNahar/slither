def calculateFatCalories(fat_grams):
    return fat_grams * 9

def calculateCarbCalories(carb_grams):
    return carb_grams * 4

def getCals():
    fat_grams = float(input("Enter fat grams: "))
    carb_grams = float(input("Enter carbohydrate grams: "))

    fat_calories = calculateFatCalories(fat_grams)
    carb_calories = calculateCarbCalories(carb_grams)

    return fat_calories, carb_calories


def main():
    fat_calories, carb_calories = getCals()
    print(f"\nFat calories: {fat_calories}")
    print(f"Carbohydrates calories: {carb_calories}")
    print(f"Total calories: {fat_calories + carb_calories}")

if __name__ == "__main__":
    main()