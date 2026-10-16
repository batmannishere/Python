import numpy as np

ages = np.array([
    [12, 16, 18, 25, 35, 65],
    [14, 17, 22, 30, 55, 70]
])

adult = ages >= 18
teenager = (ages >= 13) & (ages <= 17)
senior = ages >= 60

print("Ages:")
print(ages)

print("Adults:")
print(ages[adult])

print("Teenagers:")
print(ages[teenager])

print("Seniors:")
print(ages[senior])