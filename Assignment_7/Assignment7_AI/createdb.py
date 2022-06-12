import random

# FIRST STEP
# a. Create a distribution of 1000 random points in the domain [-10,10]^2

n = 1000
matrix = []

for i in range(n):
    x = random.random() * 20 - 10
    y = random.random() * 20 - 10
    matrix.append((x, y))

# save the database into the file myDataset.dat
with open("myDataset.csv", "w") as file:
    file.write(f"{n}\n")
    for line in matrix:
        file.write(f"{line[0]},{line[1]}\n")