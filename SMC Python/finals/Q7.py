import math

def calculateZScore(score, mean, standard_deviation):
    return (score - mean) / standard_deviation

def calculateStandardError(standard_deviation, n):
    return standard_deviation / math.sqrt(n)

def main():
    score = 190
    mean = 150
    standard_deviation = 25
    n = 10

    z_score = calculateZScore(score, mean, standard_deviation)
    print(f"z-score: {z_score:.2f}")

    standard_error = calculateStandardError(standard_deviation, n)
    print(f"standard error: {standard_error:.2f}")

if __name__ == "__main__":
    main()