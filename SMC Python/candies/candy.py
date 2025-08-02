class Candy:

    def __init__(self, name, calories, fat):
        self.name = name
        self.calories = calories
        self.fat = fat

    def __str__(self):
        return f"Candy Name: {self.name}, Calories: {self.calories}, Fat: {self.fat}g"


def read_candy_file():
    candies = []

    with open("/Users/ankurnahar/Documents/projects/slither/SMC Python/candies/mycandy.txt", "r") as file:
        lines = file.readlines()

    for line in lines[1:]:
        attributes = line.split(",") 
        if len(attributes) == 3:
            name = attributes[0]
            calories = int(attributes[1])
            fat = int(attributes[2])
            candy = Candy(name, calories, fat)
            candies.append(candy)

    for candy in candies:
        print(candy)

#read_candy_file()


def append_candy():
    with open("/Users/ankurnahar/Documents/projects/slither/SMC Python/candies/mycandy.txt", "a") as file:
        file.write("Hershey's,190,10")

    with open("/Users/ankurnahar/Documents/projects/slither/SMC Python/candies/mycandy.txt", "r") as file:
        content = file.read()
        print(content)

append_candy()