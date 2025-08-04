import pandas as pd

height = [1.47, 1.5, 1.52, 1.55, 1.57, 1.6, 1.63, 1.65, 1.68, 1.7, 1.73, 1.75, 1.78, 1.8, 1.83]
weight = [52.21, 53.12, 54.48, 55.84, 57.2, 58.57, 59.93, 61.29, 63.11, 64.47, 66.28, 68.1, 69.92, 72.19, 74.46]
bmi = [24.16, 23.61, 23.58, 23.24, 23.21, 22.88, 22.56, 22.51, 22.36, 22.31, 22.15, 22.24, 22.07, 22.28, 22.23]

bmi_table = pd.DataFrame({"height": height, "weight": weight, "bmi": bmi})

def get_sample_mean(sample_size, data):
    sample_data = data.sample(n=sample_size)  
    sample_mean = sample_data.mean()          
    return sample_mean

print("Sample mean of height:", round(get_sample_mean(5, bmi_table['height']), 3))
print("Sample mean of weight:", round(get_sample_mean(5, bmi_table['weight']), 3))
print("Sample mean of bmi:", round(get_sample_mean(5, bmi_table['bmi']), 3))