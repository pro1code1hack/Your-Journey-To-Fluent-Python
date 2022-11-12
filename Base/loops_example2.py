years = int(input("input years"))
population = 2048
for i in range(years):
    population *= 0.5
print("population after", years, "years will be", int(population))
