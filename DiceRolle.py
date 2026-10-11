import random

dice = [1, 2, 3, 4, 5, 6,7,8,9]
print("Randomly selecting same number of a dice")
for i in range(8):
    random.seed(29)
    print(random.choice(dice))
